# Programa de validação de metas de vendas

# 1. Solicita as informações do usuário
vendas_primeira_quinzena = int(input("Digite a quantidade de vendas da primeira quinzena: "))
vendas_segunda_quinzena = int(input("Digite a quantidade de vendas da segunda quinzena: "))

# 2. Calcula o total de vendas
total_vendas = vendas_primeira_quinzena + vendas_segunda_quinzena

# 3. Exibe o total alcançado

print(f"Total de vendas no mês: {total_vendas} unidades.")

# 4. Verifica se atingiu exatamente a meta (50 unidades)
if total_vendas == 50:
    print("Parabéns! O funcionário atingiu EXATAMENTE a meta estipulada de 50 unidades.")
elif total_vendas > 50:
    print("O funcionário superou a meta de 50 unidades.")
else:
    print("O funcionário não atingiu a meta de 50 unidades.")
