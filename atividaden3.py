soma = 0
quantidade_numeros = 5
 
print("Digite 5 números POSITIVOS (Ou 999 para parar o programa):")
 
for i in range(quantidade_numeros):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    # # 1. Testando o BREAK: Se digitar 999, o programa para na hora
    if numero == 999:
        print("\n⛔ Operação cancelada pelo usuário (Código 999).")
        break
        
    # # 2. Testando o CONTINUE: Se for negativo, ignora e vai para o próximo
    if numero < 0:
        print("⚠️ Números negativos não são aceitos. Pulando este...")
        continue
        
    # # Se passou pelas condições acima, acumula a soma
    soma += numero
 
# # 3. Testando o ELSE: Só roda se o loop terminar os 5 giros sem nenhum 'break'
else:
    print("\n✅ Todos os números foram processados com sucesso!")
    media = soma / quantidade_numeros
    print(f"Soma dos números válidos: {soma}")
    print(f"Média dos números válidos: {media}")
 
print("Fim do programa.")