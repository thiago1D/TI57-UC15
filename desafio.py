soma_pesos = 0.0
pecas_validas = 0
 
# O programa usa obrigatoriamente um laço for com range() para 5 peças
for i in range(1, 6):
    # Entrada de Dados indicando a peça atual
    peso = float(input(f"Digite o peso da peça {i} em gramas: "))
   
    # Regra do break (Parada de Emergência)
    if peso == 999:
        print("ALERTA: Linha de produção interrompida imediatamente!")
        break
       
    # Regra do continue (Peças Leves Demais)
    if peso <= 0 or peso < 50:
        print("Aviso: Peça descartada por peso insuficiente. Pulando para a próxima...")
        continue
       
    # Acumulação dos dados válidos
    soma_pesos += peso
    pecas_validas += 1
 
# Regra do else (Relatório Final de Sucesso)
else:
    print("\nAuditoria de lote concluída com sucesso!")
    print(f"Soma total dos pesos das peças válidas aprovadas: {soma_pesos}g")
   
    # Cálculo da média (evitando divisão por zero caso nenhuma peça seja válida)
    if pecas_validas > 0:
        media = soma_pesos / pecas_validas
    else:
        media = 0.0
       
    print(f"Média de peso das peças válidas aprovadas: {media}g")
 