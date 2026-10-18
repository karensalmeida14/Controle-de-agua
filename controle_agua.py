from colorama import Fore, Style, init

# Inicia o colorama (necessário no Windows)
init(autoreset=True)

# 1. Lista com as situações do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# 2. Função que define a cor conforme o nível (de 1 a 5)
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# 3. Simulação - exibe todos os níveis
print("--- Sistema de Monitoramento do Reservatório ---\n")

for i, situacao in enumerate(niveis, start=1):
    cor = definir_cor(i)
    # Exibe com a cor correspondente
    print(f"{cor}Nível {i}: {situacao}{Style.RESET_ALL}")

print("\n--- Fim da simulação ---")

# Exemplo de situação atual (pode mudar o número aqui)
nivel_atual = 3
print(f"\nSituação ATUAL:")
print(f"{definir_cor(nivel_atual)}Reservatório em nível {nivel_atual} - {niveis[nivel_atual-1]}{Style.RESET_ALL}")
