# ler o arquivo e exibir o texto e letras maiusculas 

with open('mensagem.txt','r') as arquivo:
    for linha in arquivo: # aqui percorremos as lnhas do aquivo
        print(linha.strip().upper()) # imprimimos cada linha em letra maiuscula e 
# triamos os espaços 