# Controle de Níveis de Água

Sistema simples de monitoramento de reservatório de água executado no terminal.

## Como funciona
O sistema simula 5 níveis do reservatório com cores diferentes usando a biblioteca colorama.

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Requisitos atendidos
- Lista para armazenar os níveis
- Importação da biblioteca colorama
- Função para definir a cor conforme o nível
- Exibição com cor correspondente
- Restauração do estilo com Style.RESET_ALL

## Como executar
pip install colorama
python controle_agua.py
