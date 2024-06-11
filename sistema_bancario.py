import os

def limpa_Terminal():
    os.system("cls")
    
def continuar():
    input("\nPressione 'Enter' para continuar")

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

->: """

saldo = 0
limite = 500
extrato = []
numeroDeSaques = 0
LIMITE_SAQUES = 3

while True:
    limpa_Terminal()
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            print(f"""\n_____________________
Saldo Anterior: R$ {saldo:.2f}
Depósito R$ {valor:.2f}
Saldo Atual R$ {saldo+valor:.2f}
_____________________\n""")
            extrato.append(f"""--> DEPOSITO
Saldo Anterior: R$ {saldo:.2f}
Depósito R$ {valor:.2f}
Novo Saldo R$ {saldo+valor:.2f}
_____________________""")
            saldo = saldo + valor
        
        else:
            print("A operação falhou!\nO valor informado é invalido.")
        continuar()
            
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeuSaldo = valor > saldo
        
        excedeuLimite = valor > limite
        
        excedeuSaques = numeroDeSaques >= LIMITE_SAQUES
        
        if excedeuSaldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeuLimite:
            print("Operação falhou! O valor do saque excede o limite.")
            
        elif excedeuSaques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            print(f"""\n_____________________
Saldo Anterior: R$ {saldo:.2f}
Saque R$ {valor:.2f}
Saldo Atual R$ {saldo-valor:.2f}
_____________________\n""")
            extrato.append(f"""--> SAQUE
Saldo Anterior: R$ {saldo:.2f}
Saque R$ {valor:.2f}
Novo Saldo R$ {saldo-valor:.2f}
_____________________""")
            saldo = saldo - valor
        
        else:
            print("A operação falhou!\nO valor informado é invalido.")
        continuar()
        
    elif opcao == "3":
        limpa_Terminal()
        print("\n================ EXTRATO ================\n")
        
        if len(extrato) <= 0:
            print("Não foram realizadas movimentações.")
            
        else:
            for movimentacao in extrato:
                print(movimentacao)
        print(f"\nSaldo Atual: R$ {saldo:.2f}")
        continuar()

    elif opcao == "4":
        break
    
    else:
        limpa_Terminal()
        print("ATENÇÃO!! Opção invalida\n")  
        continuar()
        