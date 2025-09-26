# contar quantas lnhas tem no arquivo 

with open('pessoa.txt', 'r', encoding='utf-8') as arquivo: 
    linhas= arquivo.readlines() # aqiu estamos lendo o arquivo e armazenando 
    # a leitura na vriavel linhas 
    print('total linhas: ', len(linhas)) # a função len() cnta quantas 
    # linhas tem no arquivo lido  
    