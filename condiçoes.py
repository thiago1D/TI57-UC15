# Pedindo o número inteiro ao usuário
numero = int(input("Digite um número inteiro qualquer: "))

# Realizando a divisão inteira por 2
resultado_divisao = numero % 2

# Exibindo o resultado da divisão inteira
print(f"A divisão inteira de {numero} por 2 é: {resultado_divisao}")

# Verificando se o número original é par ou ímpar
# Se o resto da divisão por 2 for 0, é par. Caso contrário, é ímpar.
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")