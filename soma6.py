#declaçao de variaveis
nome_produto = input('digita o nome do produto: ')
preço = float(input('digita o preço do produto: '))
quantidade = int(input('digita a quantidade do produto: '))
total = preço * quantidade
print(f' o total a pagar pelo produto {nome_produto} e; {total}0 para formartar o total com 3 casas decimais')
