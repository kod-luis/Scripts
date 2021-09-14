from os import system

def executarPS(cmd):
    import subprocess
    return subprocess.run(['powershell','-Command' ,cmd], capture_output=True)

listapcs = list()

#PS script to get a list of AD computers
script = 'Get-ADComputer -Filter * -properties *|select Name, OperatingSystem'
ret = executarPS(script)
ret_list = ret.stdout.split(b'\n')

#Get the PCs hostnames
for i, reg in enumerate(ret_list):
    if i > 2:
        regformat = str(reg[str(reg).find("'")-1:str(reg).find('\r')]).replace("b'", '').replace("'","").replace("\\xa9", "").strip()
        if len(regformat) > 0:
            listapcs.append(regformat.replace(' ','|',1).replace(' W','|W').replace(' ', '').split('|'))

#Remove white spaces
for index, info in enumerate(listapcs):
    for i, p in enumerate(info):
        if p == '':
            listapcs[index].remove(p)

#PS scripts to get hardware info based on hostname
for i, reg in enumerate(listapcs):
    scripts = [f'Get-WmiObject -Class Win32_Processor -ComputerName {reg[0]}',
               f'Get-WmiObject -Class Win32_LogicalDisk -ComputerName {reg[0]}',
               f'Get-WmiObject -Class MSFT_PhysicalDisk -ComputerName {reg[0]} -Namespace root\\Microsoft\\Windows\\Storage | Select FriendlyName, MediaType',
               f'Get-WmiObject win32_VideoController -ComputerName {reg[0]} | Select-Object Name',
               f'Get-WmiObject -Class Win32_physicalmemory -ComputerName {reg[0]} | Select-Object BankLabel,Capacity']
    for s in scripts:
        ret = executarPS(s)
        if ret.returncode != 0:
                print(f'Ocorreu um erro ao consultar o computador: {reg[0]}')
                print('-='*15)
        else:
            listapcs[i].append(str(ret.stdout).split('\\n'))
    #Formating
    for e, spec in enumerate(listapcs[i]):
        if e > 1:
            r = list()
            for coisas in spec:
                fim = coisas.replace("b'","").replace('\\r','').replace("'","").replace('\\\\','\\').strip()
                r.append(fim)
            listapcs[i][e] = r

#Create a file with data collected
try:
    import os
    from pathlib import Path
    caminho = os.path.join(str(Path.home())+'\\desktop', 'listapcs.txt')
    with open(caminho,'at') as arq:
        arq.write('-=-'*15+'\n')
        for listapc in listapcs:
            for i, pc in enumerate(listapc):
                if i == 0 or i == 1:
                    arq.write(pc)
                    arq.write('      -      ' if i == 0 else '\n')
                else:
                    arq.write('-'*45+'\n')
                    for spec in pc:
                        arq.write(spec+'\n')
            arq.write('='*45+'\n')
except Exception as erro:
    print('Houve um Erro: '+str(erro)+'\n')
else:
    print('Arquivo gerado com sucesso!'+'\n')
finally:
    system('PAUSE')
