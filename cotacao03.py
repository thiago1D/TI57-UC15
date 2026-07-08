import requests


def painel_multi_moedas():
    print("=" * 50)
    print("      PAINEL MULTI-MOEDAS DE CÂMBIO INVERSO      ")
    print("=" * 50)

    # 1. Entrada de Dados
    try:
        valor_brl = float(
            input("Digite o valor em Reais (R$) disponível para conversão: ")
        )
        if valor_brl <= 0:
            print("Por favor, insira um valor maior que zero.")
            return
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números e use ponto para decimais.")
        return

    # 2. Otimização de API (Requisição Única)
    url = (
        "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
    )

    try:
        response = requests.get(url)

        # 3. Tratamento de Erros (Status Code 200)
        if response.status_code == 200:
            dados = response.json()

            # 4. Lógica de Câmbio Inverso e Extração do 'bid'
            # Extraindo as cotações
            cotacao_usd = float(dados["USDBRL"]["bid"])
            cotacao_eur = float(dados["EURBRL"]["bid"])
            # O Bitcoin na AwesomeAPI geralmente vem multiplicado por 1000 dependendo da formatação antiga,
            # mas o campo 'bid' atual reflete o valor real em BRL.
            cotacao_btc = float(dados["BTCBRL"]["bid"])

            # Efetuando os cálculos (Valor em Reais / Cotação)
            total_usd = valor_brl / cotacao_usd
            total_eur = valor_brl / cotacao_eur
            total_btc = valor_brl / cotacao_btc

            # 5. Formatação Personalizada de Saída
            print("\n" + "-" * 50)
            print(f" VALOR INFORMADO: R$ {valor_brl:,.2f}")
            print("-" * 50)
            print(
                f" DÓLAR (USD)\n"
                f"   > Cotação: R$ {cotacao_usd:.2f}\n"
                f"   > Poder de Compra: $ {total_usd:.2f}\n"
            )
            print(
                f" EURO (EUR)\n"
                f"   > Cotação: R$ {cotacao_eur:.2f}\n"
                f"   > Poder de Compra: € {total_eur:.2f}\n"
            )
            print(
                f" BITCOIN (BTC)\n"
                f"   > Cotação: R$ {cotacao_btc:,.2f}\n"
                f"   > Poder de Compra: ₿ {total_btc:.8f}"
            )
            print("-" * 50)

        else:
            print(
                f"Erro ao acessar a API. Status Code: {response.status_code}"
            )

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ou falha na requisição: {e}")


if __name__ == "__main__":
    painel_multi_moedas()