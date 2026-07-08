# Programa de aprovação de alunos

# 1. Solicita as notas primeiro
nota1 = float(input("Entre com sua primeira nota: "))
nota2 = float(input("Entre com sua segunda nota: "))

# 2. Valida se as notas são permitidas (entre 0 e 10)
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Nota inválida. As notas devem estar entre 0 e 10.")
else:
    # Tudo o que depende das notas corretas fica aqui dentro do 'else'
    
    # 3. Calcula a média das duas notas
    media = (nota1 + nota2) / 2
    
    print("-" * 30)
    print(f"Sua média foi: {media:.1f}")

    # 4. Verifica a aprovação (considerando média 6.0 como corte)
    if media >= 6.0:
        print("Parabéns, você foi aprovado!")
    else:
        print("Estude um pouco mais, você ficou de recuperação.")