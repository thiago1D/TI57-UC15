

# 1. Recebendo as duas entradas do usuário (números inteiros)
cristais_coletados = int(input("Digite a quantidade total de cristais coletados: "))
capacidade_maxima = int(input("Digite a capacidade máxima de cada caixa: "))
 
# 2. Calculando o número total de caixas cheias (divisão inteira)
caixas_cheias = cristais_coletados // capacidade_maxima
 
# 3. Calculando a quantidade de cristais que restaram (resto da divisão)
cristais_restantes = cristais_coletados % capacidade_maxima
 
# 4. Calculando a projeção de energia da sonda (caixas_cheias ao quadrado)
projecao_energia = caixas_cheias ** 2
 
# 5. Exibindo os resultados na tela
print("\n--- Relatório da Sonda Espacial ---")
print(f"Número total de caixas cheias enviadas à Terra: {caixas_cheias}")
print(f"Quantidade de cristais que restaram: {cristais_restantes}")
print(f"Projeção de consumo de energia estimado: {projecao_energia} unidades de energia")
