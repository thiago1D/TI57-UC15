import requests
 
# 1. Pedir para o usuário qual moeda ele quer consultar
# Usamos .upper() para garantir que o texto fique em letras maiúsculas (ex: usd vira USD)
moeda = input("Digite a sigla da moeda estrangeira (ex: USD, EUR, BTC): ").upper()
 
# 2. Definir a URL da API usando a moeda digitada
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
 
# 3. Fazer a requisição do tipo GET
resposta = requests.get(url)
 
# 4. Verificar se a requisição deu certo
if resposta.status_code == 200:
    dados = resposta.json()
   
    # A API retorna um dicionário onde a chave é a combinação das moedas (ex: USDBRL)
    chave_moeda = f"{moeda}BRL"
   
    # Buscamos os dados específicos daquela moeda
    detalhes = dados[chave_moeda]
   
    # Extraímos as informações que queremos exibir
    nome = detalhes['name']       # Nome completo da moeda (ex: Dólar Americano/Real Brasileiro)
    valor_atual = detalhes['bid'] # Valor de compra atual
    maximo = detalhes['high']     # Maior valor do dia
    minimo = detalhes['low']      # Menor valor do dia
   
    print("\n" + "="*40)
    print(f"Dados da Cotação ({moeda}):")
    print(f"Moeda: {nome}")
    print(f"Valor Atual: R$ {float(valor_atual):.2f}")
    print(f"Máxima do dia: R$ {float(maximo):.2f}")
    print(f"Mínima do dia: R$ {float(minimo):.2f}")
    print("="*40)
 
else:
    # Se der erro 404, provavelmente a sigla da moeda está errada
    print(f"\nErro ao buscar cotação. Verifique se a sigla '{moeda}' está correta.")
 
 
 