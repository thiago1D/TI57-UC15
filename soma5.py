# Solicitando os dois números reais (float) ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
 
# Realizando as operações aritméticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
exponenciacao = num1 ** num2  # Em Python, o operador de potência é **
 
# Exibindo os resultados na tela
print("\n--- Resultados ---")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Exponenciação: {exponenciacao}")