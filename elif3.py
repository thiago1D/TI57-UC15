vagas_ocupados = int(input('digite a quantidade de vagas ocupadas'))
vagas_diponiveis = int(input( ))
if vagas_ocupados < 0 or vagas_ocupados < 0 or vagas_ocupados > 100:
    print('erro: quantitade invalida')
elif vagas_ocupados ==0:
    print('estacionamento vazio')
elif vagas_ocupados ==100:
    print('estacionamento lotado')
else:
    #se chegou ate aqui, sgnifica que esta entre 1 e 99 (vagas disponiveis)
    print('vagas disponiveis')

    print("total de vagas disponiveis")
