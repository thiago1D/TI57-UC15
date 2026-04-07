# Modelo Entidade-Relacionamento (MER) - Gestão Imobiliária

## 1. Entidades e Atributos

* **bancos**
    * `codigo_banco` (Texto, Chave Primária) - Ex: '104', '341'
    * `nome_banco` (Texto)
* **proprietarios**
    * `id_proprietario` (Inteiro, Chave Primária, Auto-incremento)
    * `nome` (Texto)
    * `cpf_cnpj` (Texto, Único)
    * `email` (Texto)
* **imoveis**
    * `id_imovel` (Inteiro, Chave Primária, Auto-incremento)
    * `id_proprietario` (Inteiro, Chave Estrangeira)
    * `endereco` (Texto)
    * `tipo` (Texto) - Ex: Casa, Apartamento
    * `valor_aluguel` (Decimal)
* **inquilinos**
    * `id_inquilino` (Inteiro, Chave Primária, Auto-incremento)
    * `nome` (Texto)
    * `cpf` (Texto, Único)
* **contratos**
    * `id_contrato` (Inteiro, Chave Primária, Auto-incremento)
    * `id_imovel` (Inteiro, Chave Estrangeira)
    * `id_inquilino` (Inteiro, Chave Estrangeira)
    * `codigo_banco` (Texto, Chave Estrangeira) - Banco para depósito do aluguel
    * `data_inicio` (Data)
    * `data_fim` (Data)

## 2. Relacionamentos (Regras de Negócio)

* Um **Proprietário** pode possuir vários **Imóveis** (1:N).
* Um **Imóvel** pertence a apenas um **Proprietário** (1:1).
* Um **Imóvel** pode ser objeto de vários **Contratos** ao longo do tempo (1:N).
* Um **Inquilino** pode assinar vários **Contratos** (1:N).
* Um **Contrato** utiliza apenas um **Banco** para direcionamento financeiro (1:1).