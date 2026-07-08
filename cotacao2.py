import requests
 
moeda = input("Digite a sigla da moeda estrangeira (ex: USD, EUR, BTC): ").upper()
valor = float(input("Digite o valor que deseja converter: "))
 
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
 
resposta = requests.get(url)
 
if resposta.status_code == 200:
    dados = resposta.json()
   
    chave_moeda = f"{moeda}BRL"
   
    detalhes = dados[chave_moeda]
   
    nome = detalhes['name']      
    valor_atual = float(detalhes['bid'])
    conversao=valor_atual*valor
 
    print("\n" + "="*40)
    print(f"Dados da Cotação ({moeda}):")
    print(f"Moeda: {nome}")
    print(f"Valor Atual: R$ {float(valor_atual):.2f}")
    print(f"O valor a receber é R$ {conversao:.2f}")
    print("="*40)
 
else:
 
    print(f"\nErro ao buscar cotação. Verifique se a sigla '{moeda}' está correta.")