import os

# Constantes
LIMITE_SAQUES = 3

# Variáveis
saldo = 0.0

limite = 500

extrato = []

numero_saques = 0

titulo = '''
 ██████╗  █████╗ ███╗   ██╗ ██████╗ ██████╗ 
 ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔═══██╗
 ██████╔╝███████║██╔██╗ ██║██║     ██║   ██║
 ██╔══██╗██╔══██║██║╚██╗██║██║     ██║   ██║
 ██████╔╝██║  ██║██║ ╚████║╚██████╗╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝
'''

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""
opcoes = ['1','2','3','4']

# Funções
def div(quant):
    print('+'+'-'*quant+'+')

def opcao_selecionada(opcao):
    match opcao:
        case '1':
            depositar()
        case '2':
            sacar()
        case '3':
            imprimir_extrato()
        case '4':
            sair()

def menu_de_opcoes():
    print(menu)
    opcao = input('Digite a opção desejada => ').strip()
    if (opcao not in opcoes):
        tela_principal_alt()
    else:
        opcao_selecionada(opcao)

def menu_de_opcoes_alt():
    print(menu)
    print('Opção inválida, tente novamente.\n')
    opcao = input('Digite a opção desejada => ').strip()
    if (opcao not in opcoes):
        tela_principal_alt()
    else:
        opcao_selecionada(opcao)

def tela_principal():
    os.system('cls')
    print(titulo)
    div(43)
    menu_de_opcoes()

def tela_principal_alt():
    os.system('cls')
    print(titulo)
    div(43)
    menu_de_opcoes_alt()

def voltar_tela_principal():
    opcoes2 = ['1','2']
    print('''
Gostaria de voltar à tela principal?
[1] Sim
[2] Sair
''')
    opcao2 = input('Digite a opção desejada => ').strip()
    while (opcao2 not in opcoes2):
        print('\nOpção inválida, tente novamente.')
        opcao2 = input('\nDigite a opção desejada => ').strip()
    match opcao2:
        case '1':
            tela_principal()
        case '2':
            sair()    

def sair():
    print('Encerrando o sistema...')
    os.system('exit') 

def depositar():
    global saldo, extrato
    os.system('cls')
    print('''
 ██████╗ ███████╗██████╗  ██████╗ ███████╗██╗████████╗ ██████╗ 
 ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝██║╚══██╔══╝██╔═══██╗
 ██║  ██║█████╗  ██████╔╝██║   ██║███████╗██║   ██║   ██║   ██║
 ██║  ██║██╔══╝  ██╔═══╝ ██║   ██║╚════██║██║   ██║   ██║   ██║
 ██████╔╝███████╗██║     ╚██████╔╝███████║██║   ██║   ╚██████╔╝
 ╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚═╝   ╚═╝    ╚═════╝ 
''')
    div(62)
    while True:
        try:
            valor = float(input("\nInforme o valor do depósito: "))
            if valor > 0.0:
                saldo += valor
                extrato.append(f'Depósito: R${valor:.2f}')
                print('\nOperação realizada com sucesso!')
                break
            else:
                print("\nOperação falhou! O valor informado é inválido.")
        except ValueError:
            print("\nOperação falhou! O valor informado é inválido.")
    voltar_tela_principal()

def sacar():
    global saldo, numero_saques, limite, extrato
    os.system('cls')
    print('''
 ███████╗ █████╗  ██████╗ ██╗   ██╗███████╗
 ██╔════╝██╔══██╗██╔═══██╗██║   ██║██╔════╝
 ███████╗███████║██║   ██║██║   ██║█████╗  
 ╚════██║██╔══██║██║▄▄ ██║██║   ██║██╔══╝  
 ███████║██║  ██║╚██████╔╝╚██████╔╝███████╗
 ╚══════╝╚═╝  ╚═╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝
          ''')
    div(44)
    while True:    
        try:
            valor = float(input("Informe o valor do saque: "))
            if (valor <= 0):
                print('Valor inserido inválido, tente novamente.')
            else:
                break
        except ValueError:
            print('Valor inserido inválido, tente novamente.')
            
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        voltar_tela_principal()
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
        voltar_tela_principal()
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
        voltar_tela_principal()
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        voltar_tela_principal()
    return 0

def imprimir_extrato():
    global saldo, extrato
    os.system('cls')
    print('''
 ███████╗██╗  ██╗████████╗██████╗  █████╗ ████████╗ ██████╗ 
 ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗
 █████╗   ╚███╔╝    ██║   ██████╔╝███████║   ██║   ██║   ██║
 ██╔══╝   ██╔██╗    ██║   ██╔══██╗██╔══██║   ██║   ██║   ██║
 ███████╗██╔╝ ██╗   ██║   ██║  ██║██║  ██║   ██║   ╚██████╔╝
 ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝                                                            
''')
    div(59)
    if (len(extrato)==0):
        print('Não foram realizadas movimentações até o momento.')
    else:
        for i in range(len(extrato)):
            print(extrato[i])
    div(59)
    print(f'Saldo: R${saldo:.2f}\n')
    voltar_tela_principal()
    return 0

# Main
tela_principal()