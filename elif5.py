# Solicita o valor total da carga ao usuário
valor_carga = float(input("Digite o valor total da carga (R$): "))
 
# Inicializa a variável do percentual de desconto
desconto_percentual = 0.0
 
# Aplica as regras de negócio baseadas nas faixas de valor
if valor_carga <= 1000.00:
    desconto_percentual = 0.0
elif valor_carga <= 5000.00:
    desconto_percentual = 0.05  # 5%
else:
    desconto_percentual = 0.10  # 10%
 
# Cálculos dos valores
valor_desconto = valor_carga * desconto_percentual
valor_final = valor_carga - valor_desconto
 
# Exibe os resultados formatados
print(f"\n--- Resumo do Frete ---")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a ser pago: R$ {valor_final:.2f}")