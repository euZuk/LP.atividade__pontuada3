import os

os.system('cls')

# --- ESTRUTURA DE DADOS (ARMAZENAMENTO) ---
# 'reservas' é a lista global. Cada reserva é um dicionário {aviao, passageiro}
# O limite de 20 é controlado pelo tamanho (len)
reservas = [] 

# Vetores para 4 aviões e seus respectivos assentos.
avioes = [0] * 4
assentos = [0] * 4

# Variável de controle para saber quantos aviões o usuário decidiu cadastrar
qtd_avioes = 0 

def registrar_avioes():
    global qtd_avioes # 'global' permite alterar a variável que está fora da função
    print("\n--- CADASTRO DE AERONAVES ---")
    i = 0
    qtd_avioes = 0 # Reinicia o contador para um novo cadastro
    
    while i < 4:
        avioes[i] = int(input(f"Informe o número do {i+1}º avião: "))
        qtd_avioes += 1 # Incrementa quantos aviões existem no sistema
        
        # Lógica para ESCOLHER se quer continuar ou não
        if i < 3: # Só pergunta se ainda houver espaço no vetor (máximo 4)
            continuar = input("Deseja cadastrar outro avião? (s/n): ").lower()
            if continuar != 's':
                break # Sai do laço while antes de chegar em 4
        i += 1

def registrar_assentos():
    # Validação: Não pode registrar assentos se não houver aviões
    if qtd_avioes == 0:
        print("Erro: Cadastre os aviões primeiro (Opção 1).")
        return

    print("\n--- QUANTITATIVO DE ASSENTOS ---")
    i = 0
    while i < qtd_avioes: # Percorre apenas os aviões que foram cadastrados
        assentos[i] = int(input(f"Assentos disponíveis para o avião {avioes[i]}: "))
        i += 1

def reservar_passagem():
    # REGRA GLOBAL: O sistema impede novas reservas se atingir 20 registros
    if len(reservas) >= 20:
        print("ALERTA: Limite de 20 reservas gerais atingido!")
        return

    if qtd_avioes == 0:
        print("Erro: Não há aviões disponíveis.")
        return

    num_procurado = int(input("\nDigite o número do avião para a reserva: "))
    
    # Busca manual (sem for) para encontrar o índice do avião
    indice = -1
    i = 0
    while i < qtd_avioes:
        if avioes[i] == num_procurado:
            indice = i
        i += 1
    
    # REGRAS DE NEGÓCIO DA RESERVA
    if indice == -1:
        print("Este avião não existe!")
    elif assentos[indice] <= 0:
        print("Não há assentos disponíveis para este avião!")
    else:
        nome = input("Nome do passageiro: ")
        assentos[indice] -= 1 # Reduz 1 vaga no vetor de assentos do avião específico
        
        # Adiciona o registro (dicionário) na lista global de reservas
        nova_reserva = {"aviao": num_procurado, "passageiro": nome}
        reservas.append(nova_reserva)
        print("Reserva realizada com sucesso!")

def consulta_por_aviao():
    num_procurado = int(input("\nConsultar qual avião? "))
    
    # Primeiro verifica se o avião informado existe nos registros
    existe = False
    i = 0
    while i < qtd_avioes:
        if avioes[i] == num_procurado:
            existe = True
        i += 1
    
    if not existe:
        print("Este avião não existe!")
        return

    # Se existir, percorre a lista global de reservas procurando passageiros
    print(f"Passageiros do avião {num_procurado}:")
    encontrou_reserva = False
    i = 0
    while i < len(reservas):
        if reservas[i]["aviao"] == num_procurado:
            print(f"- {reservas[i]['passageiro']}")
            encontrou_reserva = True
        i += 1
    
    if not encontrou_reserva:
        print("Não há reservas realizadas para este avião!")

def consulta_por_passageiro():
    nome_busca = input("\nNome do passageiro para consulta: ")
    encontrou = False
    
    # Percorre a lista global procurando o nome informado
    i = 0
    while i < len(reservas):
        if reservas[i]["passageiro"].lower() == nome_busca.lower():
            print(f"- Possui reserva no avião: {reservas[i]['aviao']}")
            encontrou = True
        i += 1
    
    if not encontrou:
        print("Não há reservas realizadas para este passageiro!")

def menu():
    opcao = "0"
    while opcao != "6":
        print("\n--- SWEET FLIGHT - SISTEMA DE GESTÃO ---")
        print(f"Reservas Atuais: {len(reservas)}/20")
        print("1. Registrar Aviões")
        print("2. Registrar Assentos")
        print("3. Reservar Passagem")
        print("4. Consulta por Avião")
        print("5. Consulta por Passageiro")
        print("6. Encerrar Sistema")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1": registrar_avioes()
        elif opcao == "2": registrar_assentos()
        elif opcao == "3": reservar_passagem()
        elif opcao == "4": consulta_por_aviao()
        elif opcao == "5": consulta_por_passageiro()
        elif opcao == "6": print("Sistema encerrado.")
        else: print("Opção inválida!")

# Inicia o programa chamando o menu
if __name__ == "__main__":
    menu()