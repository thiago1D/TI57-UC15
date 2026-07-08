num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
num3 = float(input('Digite a terceira nota: '))
num4 = float(input('Digite a quarta nota: '))

# Calcula a soma e a média
soma = num1 + num2 + num3 + num4
media = soma / 4

# Mostra os resultados de forma organizada
print(f'A soma das notas é: {num1} + {num2} + {num3} + {num4} = {soma}')
print(f'A média final do aluno é: {media}')