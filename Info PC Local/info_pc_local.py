from os import system

def executarPS(cmd):
    import subprocess
    return subprocess.run(['powershell','-Command' ,cmd], capture_output=True)


list_pc = list()
#set the scripts
scripts = [f'Get-WmiObject -Class Win32_Processor',
           f'Get-WmiObject -Class Win32_LogicalDisk',
           f'Get-WmiObject -Class MSFT_PhysicalDisk -Namespace root\\Microsoft\\Windows\\Storage | Select FriendlyName, MediaType',
           f'Get-WmiObject win32_VideoController | Select-Object Name',
           f'Get-WmiObject -Class Win32_physicalmemory | Select-Object BankLabel,Capacity']

#execute the scripts
print(f'{"GERANDO DADOS":-^35}')
for s in scripts:
    ret = executarPS(s)
    if ret.returncode != 0:
            print(f'Ocorreu um erro ao consultar o computador')
            print('-='*15)
    else:
        list_pc.append(str(ret.stdout).split('\\n'))

#format the powershell string
for e, spec in enumerate(list_pc):
    r = list()
    for coisas in spec:
        fim = coisas.replace("b'","").replace('\\r','').replace("'","").replace('\\\\','\\').strip()
        r.append(fim)
    list_pc[e] = r

#format the data inside a txt file
while True:
    import os
    from pathlib import Path
    from socket import gethostname
    arquivo = f'{gethostname()}.txt'
    caminho = os.path.join(str(Path.home()),'Desktop')
    try:
        with open(os.path.join(caminho,arquivo),'wt') as arq:
            arq.write('-=-'*15+'\n')
            import platform
            sistema = f'{os.environ["COMPUTERNAME"]}   -   {platform.system()}{platform.release()} {platform.win32_edition()}'
            arq.write(str(sistema)+'\n')
            for infos in list_pc:
                arq.write('-'*45+'\n')
                for spec in infos:
                    arq.write(spec+'\n')
            arq.write('-=-'*15+'\n')
    except FileNotFoundError:
        os.mkdir(caminho)
    except Exception as erro:
        print('Houve um Erro: '+str(erro)+'\n')
        break
    else:
        print(f'Arquivo "{arquivo}" gerado com sucesso em {caminho}')
        break

print('-'*45)
system('PAUSE')
