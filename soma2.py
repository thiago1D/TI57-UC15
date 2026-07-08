# Solicitando os dois números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro (divisor): "))
 
# Garantindo que não ocorra divisão por zero
if num2 != 0:
    # Realizando a divisão inteira
    divisao_inteira = num1 // num2
    print(f"A divisão inteira de {num1} por {num2} é: {divisao_inteira}")
else:
    print("Erro: Não é possível dividir por zero!")