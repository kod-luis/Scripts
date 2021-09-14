from os import walk, path, system

menu = ['pdf', 'word', 'text', 'excel']
list_log = []
file_types = []

#menu creation
print('-='*15)
print(f'{"DOC SEARCHER":^30}')
print('-='*15)
for i, f in enumerate(menu):
    print(f'[ {i+1} ] - {f.upper()}')
opt = '0'
while not type(opt) == int or int(opt) not in range(1, len(menu)+1):
    print('-'*30)
    try:
        opt = int(input('Opção: '))
    except Exception as erro:
        print('-'*30)
        print('Opção Inválida')

#setting the chosen option
if int(opt) == 1:
    file_types = ['.pdf']
elif int(opt) == 2:
    file_types = ['.doc', '.dot', '.wbk']
elif int(opt) == 3:
    file_types = ['.txt']
elif int(opt) == 4:
    file_types = ['.xls', '.xlt', '.xlm', '.xla', '.xll', '.xlw']

#going through every file starting at the script location
for dirpath, dir, filename in walk(path.dirname(__file__)):
    if len(filename) > 0:
        for file in filename:
            for ftype in file_types:
                #saving only the files with the type chosen
                if ftype in file:
                    list_log.append(f'{dirpath}\\{file}')

#creating a log file with the listed files
try:
    arq = open(path.dirname(__file__)+'\\log.txt', 'wt')
    for l in list_log:
        arq.write(l+'\n')
    arq.close()
except Exception as erro:
    print('-'*30)
    print(f'Erro ao gerar o arquivo: {erro}')
else:
    print('-'*30)
    print(f'Log gerado com sucesso em {path.dirname(__file__)}\\log.txt')
    print('-='*20)
    system('pause')
