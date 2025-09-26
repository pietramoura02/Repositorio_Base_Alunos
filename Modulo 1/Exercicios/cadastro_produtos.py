# cadastrar produtos com relatorio 
#crie um programa em python que permita cadastrar produtos 
# salvar essas informações em um arquivo chamado produtos.txt
# o programa dve permitir: 
# inserir o nome do produto e preço
# gravar os produtos no arquivo (um por linha)
# ler os dados do arquivo e gerar um relatorio com: 
# - lita de produtos cadastrados 
# - media dos peços 
# - o produto mais caro e o mais barato 

# criar o arquivo produtos.txt e escrever os produtos 
with open('produtos.txt', 'w', encoding='utf-8') as arquivo: 
    arquivo.write('café, 36.00\n')
    arquivo.write('chá, 10.00\n')
    arquivo.write('suco, 18.50\n')
    arquivo.write('refrigerante, 17.50\n')
    arquivo.write('agua, 5.50\n')
    
# ler os produtos do arquivo: 
produtos=[]
with open('produtos.txt', 'r', encoding='utf-8') as arquivo: 
    for linha in arquivo: 
         nome, preço = linha.strip().split(',') 
         produtos.append((nome,float (preço)))

# calcular a media, o mais caro e o mais barato 
total = 0 
mais_caro = produtos[0]
mais_barato = produtos[0] 

for nome, preco in produtos: 
    total +=preco # percorre a lista produto e soma cada preço encontrado 
    if preco > mais_caro[1]:
        mais_caro = (nome, preco)
        
    if  preco < mais_barato[1]:
        mais_barato = (nome, preco)
        
media= total/len(produtos) 

# Criar o relatório
with open('relatorio_produtos.txt', 'w', encoding='utf-8') as relatorio:
    relatorio.write('Lista de Produtos\n')
    for nome, preco in produtos:
        relatorio.write(f'{nome}: R${preco:.2f}')

        relatorio.write(f'\nPreço Médio: R$ {media:.2f}\n' )
        relatorio.write(f'Produto mais caro: {mais_caro[0]} R${mais_caro[1]:.2f}\n')
        relatorio.write(f'Produto mais barato: {mais_barato[0]}R${mais_barato[1]:.2f}\n')
