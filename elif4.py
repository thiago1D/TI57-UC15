pontuaçao = int(input('Digite a pontuação (de 1 a 10): ' ))
if 1 >= pontuaçao <= 3:
    print("Alerta Baixo.")
elif 4 >= pontuaçao <= 7:
    print("Alerta Médio.")
elif 8 >= pontuaçao <= 10:
    print("Alerta Alto / Crítico.")
else:
    print("Pontuação inválida.")