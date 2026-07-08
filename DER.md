erDiagram
    PREDIO {
        int id PK
        string nome
        string localizacao
        string status_obra
    }

    UNIDADE {
        int id PK
        int id_predio FK
        string numero_ap
        string status_ocupacao
    }

    CLIENTE {
        int id PK
        string nome
        string cpf UK
        string email
        string telefone
        string estado_civil
    }

    CONTRATO {
        int id PK
        int id_cliente FK
        int id_unidade FK
        decimal valor_total
        string metodo_pagamento
        date data_assinatura
    }

    LOG_SISTEMA {
        int id PK
        datetime timestamp
        string usuario
        string modulo
        string acao
        string endereco_ip
    }

    PREDIO ||--o{ UNIDADE : "contém"
    CLIENTE ||--o{ CONTRATO : "assina"
    UNIDADE ||--o| CONTRATO : "é alocada em"