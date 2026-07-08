# Sistema de Radar de Velocidade

# 1. Entrada de dados: lê a velocidade do carro
velocidade = float(input("Digite a velocidade do carro (em km/h): "))

# 2 e 3. Processamento e Saída (Condição)
if velocidade > 80:
    print(" Você foi MULTADO por excesso de velocidade!")
    
    # Calcula quantos km/h o motorista passou do limite
    km_acima = velocidade - 80
    
    # Calcula o valor da multa (R$ 7.00 por cada km acima)
    multa = km_acima * 7
    
    print(f"Você passou {km_acima:.1f} km/h acima do limite de 80 km/h.")
    print(f"O valor da multa a pagar é: R$ {multa:.2f}")
else:
    print("Boa viagem! Dirija com segurança. ")