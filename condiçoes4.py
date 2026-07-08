valor_total = float(input("digite o valor total da compra:"))

if valor_total > 150.00:
    print('desconto de 10%')
    valor = valor_total - (valor_total * 0.10)
    print(f'o valor a pagar com desconto e: {valor :.2f}')
else:
    print('sem desconto')
    print(f' o valor a pagar e : {valor_total :.2f}')