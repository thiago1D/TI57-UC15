// BANCO DE DADOS DE AMOSTRA DE UM COMANDE DE AVIAÇÃO (50 ITENS DETALHADOS)
const dadosPerfilAvançado = {
    "Nome Completo": "Comandante Carlos Henrique Silva Santos",
    "Registro Profissional ANAC": "ANAC-BR-994821-X",
    "Código de Membro Crew IATA": "IATA-CREW-7732",
    "Licença de Voo": "ATPL(A) - Licença de Piloto de Linha Aérea",
    "Tipo de Habilitação Ativa": "Boeing 777 / 787 Dreamliner Intercontinental",
    "Status Médico Militar (CMA)": "Classe 1 - Válido até 18/12/2026",
    "Horas de Voo Totais Registradas": "14.250 Horas Computadas",
    "Horas de Voo Noturno": "4.120 Horas",
    "Nível de Proficiência em Inglês (ICAO)": "Nível 5 (Excelente)",
    "Passaporte Aeronáutico": "PA-BR-88392-11",
    "Visto de Tripulante EUA": "C1/D - Ativo",
    "Base Operacional Fixa": "Aeroporto Internacional de Guarulhos (GRU)",
    "Companhia Aérea Empregadora": "SkyPass Linhas Aéreas S.A.",
    "Data de Contratação": "12 de Março de 2015",
    "Setor de Operação": "Voo de Longo Curso (Long-Haul International)",
    "Última Reciclagem em Simulador": "05/04/2026 (Aprovado com Excelência)",
    "Validação de Treinamento em Cabine sob Stress": "Válido até 2027",
    "Fator RH Sanguíneo": "O Positivo (O+)",
    "Token Biométrico de Segurança": "BIO-9923-FF-88",
    "Chave de Criptografia do Console": "AES256-SKY-771239841",
    "Terminal Físico de Acesso Atual": "Galeão Cargo Terminal / GRU T3",
    "Endereço IP de Conexão": "192.168.42.105",
    "MAC Address do Dispositivo": "00:1A:3F:F1:4C:C2",
    "Sistema Operacional de Voo Integrado": "SkyOS Enterprise v9.4.2",
    "Nível de Autorização no Sistema": "Nível 5 - Administrador de Rota / Master",
    "Acesso a Portões de Segurança": "Permitido (Áreas Restritas A, B, C, D)",
    "Código de Rádio (Callsign Padrão)": "SKY-COMMANDER-CHARLIE",
    "Frequência de Rádio Preferencial": "121.5 MHz (Emergência Guard)",
    "Status de Vacinação Internacional": "Certificado Digital OMS Atualizado",
    "Seguro de Vida Aeronáutico": "Ativo - Apólice #88231-AIG",
    "Último Teste de Fadiga Humana (FRMS)": "Score: 0.12 (Apto para decolagem)",
    "Próxima Escala Escalonada": "GRU -> CDG (Paris) em 14h 30m",
    "Histórico de Incidentes em Linha": "Zero Registros (Registro Limpo)",
    "Certificação ETOPS": "Aprovado para 180 minutos",
    "Curso de Pouso em Visibilidade Zero (CAT III)": "Certificado Ativo",
    "Pontuação de Pouso Suave (G-Force Média)": "1.12G (Excelente)",
    "Consumo Médio de Combustível em Rota": "Otimizado (Top 5% da Frota)",
    "Cargo em Solo Extra": "Instrutor de Voo de Ala Boeing",
    "Equipamento de Voo Vinculado": "EFB (Electronic Flight Bag) iPad Pro #992",
    "Assinatura Digital ICP-Brasil": "Validada e Ativa",
    "Vencimento do Contrato de Trabalho": "Indeterminado",
    "Regime de Escala Semanal": "36 Horas Semanais em Turno Variável",
    "Código de Diária Internacional": "DIAR-USD-992",
    "Acesso ao Sistema de Meteorologia": "Acesso Total (WSI / NOAA Pro)",
    "Permissão de Despacho Operacional": "Autorizado Autônomo",
    "Segurança Anti-Terrorismo TSA": "Cleared (Aprovado)",
    "Status de Bagagem de Tripulação": "Etiqueta Eletrônica Ativa #9912",
    "Ponto de Entrada Biométrico": "Portal Biométrico T3 GRU",
    "Último Check de Bagagem de Mão": "Realizado em 11/06/2026",
    "Dispositivo de Emergência Pessoal": "Rádio Baliza Ativo #771"
};

// BANCO DE DADOS DE LOGS DE ESCANEAMENTO (QUEM FEZ O QUÊ)
const logsEscaneamento = [
    { data: "11/06/2026 08:22:10", operador: "Cmt. Carlos Silva", acao: "Escaneamento de Passaporte de Passageiro", terminal: "Gate 302-GRU", status: "Aprovado/Embarcado" },
    { data: "11/06/2026 08:15:43", operador: "Agente Letícia M.", acao: "Escanear Bagagem de Mão - Tag #8821", terminal: "Raio-X Central", status: "Liberado" },
    { data: "11/06/2026 07:55:00", operador: "Cmt. Carlos Silva", acao: "Autenticação Biométrica no Sistema", terminal: "Console Principal", status: "Sessão Aberta" },
    { data: "11/06/2026 07:42:19", operador: "Sistema Automático", acao: "Varredura Antivírus e Logs de Segurança", terminal: "Servidor Nuvem Cloud", status: "Seguro" },
    { data: "11/06/2026 06:12:05", operador: "Supervisor Pedro H.", acao: "Abertura de Portão de Embarque Internacional", terminal: "Gate 305-GRU", status: "Sucesso" }
];

// BANCO DE DADOS DOS VOOS ATIVOS
const voosAtivos = [
    { rota: "GRU ➔ JFK", cia: "LATAM", partida: "20:30", preco: "R$ 4.250", status: "No Horário", classeStatus: "status-ontime" },
    { rota: "CGH ➔ SSA", cia: "GOL", partida: "14:15", preco: "R$ 890", status: "Embarcando", classeStatus: "status-boarding" },
    { rota: "GRU ➔ CDG", cia: "Air France", partida: "22:05", preco: "R$ 6.100", status: "No Horário", classeStatus: "status-ontime" }
];

// FUNÇÃO PARA INJETAR OS DADOS AUTOMATICAMENTE NA TELA
document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Coloca o nome principal
    document.getElementById("user-nome").innerText = dadosPerfilAvançado["Nome Completo"];
    
    // 2. Monta o Grid com os 50 Metadados
    const gridContainer = document.getElementById("perfil-info-grid");
    gridContainer.innerHTML = ""; // Limpa estrutura anterior
    
    Object.entries(dadosPerfilAvançado).forEach(([chave, valor]) => {
        const bloco = document.createElement("div");
        bloco.className = "info-block";
        
        bloco.innerHTML = `
            <span class="info-label">${chave}</span>
            <span class="info-value">${valor}</span>
        `;
        gridContainer.appendChild(bloco);
    });

    // 3. Monta o Painel de Voos dinamicamente
    const flightBoard = document.getElementById("flight-board");
    flightBoard.innerHTML = "";
    voosAtivos.forEach(voo => {
        const item = document.createElement("div");
        item.className = "flight-item";
        item.innerHTML = `
            <div>
                <span class="flight-route">${voo.rota}</span> <small style="color:#64748b">(${voo.cia})</small><br>
                <span class="flight-meta">Partida Prevista: ${voo.partida}</span>
            </div>
            <div style="text-align: right">
                <div style="font-weight: bold; color: #3b82f6; margin-bottom:4px">${voo.preco}</div>
                <span class="status-badge ${voo.classeStatus}">${voo.status}</span>
            </div>
        `;
        flightBoard.appendChild(item);
    });

    // 4. Monta a Tabela de Logs de Escaneamento
    const logBoard = document.getElementById("log-board");
    logBoard.innerHTML = "";
    logsEscaneamento.forEach(log => {
        const linha = document.createElement("tr");
        linha.innerHTML = `
            <td style="color: #60a5fa; font-family: monospace;">${log.data}</td>
            <td><strong>${log.operador}</strong></td>
            <td>${log.acao}</td>
            <td><code style="background:#1e293b; padding:2px 6px; border-radius:4px">${log.terminal}</code></td>
            <td><span style="color: #4ade80">${log.status}</span></td>
        `;
        logBoard.appendChild(linha);
    });
});