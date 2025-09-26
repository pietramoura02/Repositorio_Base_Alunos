# criar um arquivo nomes.txt 

nomes = ['joão\n','maria\n','ana\n']

with open('nomes.txt', 'w', encoding='utf-8') as arquivo: # criamos uma lista com nomes para ser
# criando o arquivo 
    arquivo.writelines(nomes) # estamos pedindo para escrever 