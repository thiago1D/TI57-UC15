# fazer a variavel solicitando peso e altura
peso = float(input('entre com o seu peso: '))
altura = float(input('entre com sua altura: '))

#calculo do imc

imc= peso/(altura**2)

#clasificaçao do peso
if imc < 18.56:
    print(f'seu imc e {imc}, baixo peso!')
elif imc < 24.9:
    print(f'seu imc e {imc}, peso normal!')
else:
    print(f'seu imc e {imc}, voce esta sobre peso')    
