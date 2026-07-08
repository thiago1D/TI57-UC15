import requests
 
def painel_cambio_global():
    print("--- PAINEL DE INVESTIMENTOS GLOBAIS ---")
   
    # 1. Entrada de Dados
    try:
        reais = float(input("Digite o valor em Reais (R$) para conversão: "))
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido.")
        return
 
    # 2. URL com todas as moedas combinadas
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL,JPY-BRL,ARS-BRL"
 
    try:
        # Requisição Única
        resposta = requests.get(url)
       
        # 3. Tratamento de Erro de Conexão/Status
        if resposta.status_code == 200:
            dados = resposta.json()
           
            # 4. Lógica de Câmbio Inverso (Extração das cotações 'bid')
            cotacao_usd = float(dados["USDBRL"]["bid"])
            cotacao_eur = float(dados["EURBRL"]["bid"])
            cotacao_btc = float(dados["BTCBRL"]["bid"])
            cotacao_gbp = float(dados["GBPBRL"]["bid"])
            cotacao_jpy = float(dados["JPYBRL"]["bid"])
            cotacao_ars = float(dados["ARSBRL"]["bid"])
           
            # 5. Formatação Personalizada de Saída
            print("\n=================== RESULTADO DA CONVERSÃO ===================")
            print(f"Valor inicial informado: R$ {reais:.2f}\n")
           
            print(f"Dólar (USD):   Cotação: R$ {cotacao_usd:.2f}  | Você terá: $ {reais / cotacao_usd:.2f}")
            print(f"Euro (EUR):    Cotação: R$ {cotacao_eur:.2f}  | Você terá: € {reais / cotacao_eur:.2f}")
            print(f"Libra (GBP):   Cotação: R$ {cotacao_gbp:.2f}  | Você terá: £ {reais / cotacao_gbp:.2f}")
            print(f"Iene (JPY):    Cotação: R$ {cotacao_jpy:.2f}  | Você terá: ¥ {reais / cotacao_jpy:.2f}")
            print(f"Peso (ARS):    Cotação: R$ {cotacao_ars:.2f}  | Você terá: $ {reais / cotacao_ars:.2f}")
            # Bitcoin com destaque de 8 casas decimais como exigido
            print(f"Bitcoin (BTC): Cotação: R$ {cotacao_btc:.2f}  | Você terá: ₿ {reais / cotacao_btc:.8f}")
            print("==============================================================")
           
        else:
            print(f"Erro ao acessar a API. Status Code: {resposta.status_code}")
           
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão com o servidor da API: {e}")
 
# Executa o painel
painel_cambio_global()