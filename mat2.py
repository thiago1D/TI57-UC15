import requests

#cep = input("digite o cep (apenas numeros):")
#url = (f"https://viacep.com.br/ws/{cep}/json/")
#resposta =requests.get(url)

#if resposta.status_code ==200:
#    dados = resposta.json()
#    print("dados recebidos da apt:")
#    print(f"logradoura:{dados['logradouro']}")
#    print(f"bairro:{dados['bairo']}")
#    print(f"cidade: {dados['localidade']}")                      
                          
cep = input("Digite o CEP (apenas números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"
 
resposta = requests.get(url)
 
if resposta.status_code == 200:
    dados = resposta.json()
    print("Dados recebidos da API:")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")