# Simulador de Sensor de Lixeira Inteligente

print("--- Lixeira Inteligente ---")
# Solicita o tipo de material e remove espaços extras
material = input("Digite o tipo de material descartado: ").strip().lower()

# Verifica o material e define a cor correspondente
if material == "plastico" or material == "plástico":
    print("Cor da lixeira: VERMELHO (Plástico)")
elif material == "papel":
    print("Cor da lixeira: AZUL (Papel)")
elif material == "metal":
    print("Cor da lixeira: AMARELO (Metal)")
elif material == "vidro":
    print("Cor da lixeira: VERDE (Vidro)")
else:
    print("Cor da lixeira: CINZA (Lixo orgânico/Não reciclável)")
