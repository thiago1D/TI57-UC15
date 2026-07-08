#contador para soma dos numeros
soma=0 #contador da soma dos 5 numeros
#loop for para rodar 5x
for soma_num in range(5):
    #input dos numeros.
    numero=float(input("digite o numero:"))
    #contador do loop for range
    soma_num=1
    #contador para somar os numeros do contador soma 
    soma+=numero
    media=soma/5 
    # calcular a media 
    #exibir o resultado da soma ae media
    print(f"soma dos numeros:{soma}")
    print(f"media e :{media}")



    #contador para soma dos números
soma=0 #contador da soma dos 5 números
#loop for para rodar 5 x
for soma_num in range(5):
 
    #input dos números.
    numero=float(input("Digite o número: "))
 
    #contador do loop for range
    soma_num=1
 
    #contador para somar os números do contador soma
   # soma = soma + numero
    soma += numero
 
    #calcular a média
media=soma/5
   
    #exibir o resultado da soma e média
print(f"Soma dos números: {soma}")
print(f"Média é : {media}")