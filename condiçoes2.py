idade = int(input("Digite a sua idade: "))
atual = int(input("digite o ano atual:"))
dif = atual - idade
# Verifica a maioridade
if dif >= 18:
    print("Liberado")
else:
    print("Negado")