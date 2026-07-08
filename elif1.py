# 1. Entrada de dados direta 
opcao = input("Digite a letra correspondente: ")

# 2. Testando as duas opções com 'or'
if opcao == 'S' or opcao == 's':
    print("Você selecionou: Solteiro(a).")
elif opcao == 'C' or opcao == 'c':
    print("Você selecionou: Casado(a).")
elif opcao == 'D' or opcao == 'd':
    print("Você selecionou: Divorciado(a).")
elif opcao == 'N' or opcao == 'n':
    print("Você selecionou: Noivo(a).")
elif opcao == 'M' or opcao == 'm':
    print("Você selecionou: Namorando.")
elif opcao == 'O' or opcao == 'o':
    print("Você selecionou: Outros.")
else:
    print("Opção inválida!")