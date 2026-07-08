
consumo_total = float(input('Digite o consumo total: '))
quantidade_de_pessoas = int(input('Digite a quantidade de pessoas: '))

consumo_por_pessoa = consumo_total + quantidade_de_pessoas  

if consumo_por_pessoa <= 50:
    print('consumo baixo')
elif consumo_por_pessoa <= 150:
    print('consumo medio')
else:
    print('consumo alto')
