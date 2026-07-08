import math
 
# Solicita o raio permitindo valores decimais (float)
raio = float(input("Digite o raio da esfera (em centímetros): "))
 
# Realiza o cálculo do volume aplicando a fórmula
volume = (4/3) * math.pi * (raio ** 3)
 
# Exibe o resultado formatado com duas casas decimais utilizando f-string
print(f"O volume da esfera é: {volume:.2f} cm³")