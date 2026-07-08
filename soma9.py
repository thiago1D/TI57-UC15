# Entrada dos dados 
preco_pao = float(input("Digite o preço do pão: "))
quantidade_pao = int (input("Digite a quantidade de pães: "))

preco_leite = float(input("Digite o preço do leite: "))
quantidade_leite = int(input("Digite a quantalide de litros de leite: "))

#Cálculos
total_paes = preco_pao * quantidade_pao 
total_leite = total_paes * quantidade_leite

valor_total = total_paes + total_leite

#Resultado 
print(f"Valor total da compra: R$", valor_total)