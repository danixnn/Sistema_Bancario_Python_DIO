def menu():
    menu = """\n
       ================ MENU ================
       [d]\tDepositar
       [s]\tSacar
       [e]\tExtrato
       [nc]\tNova conta
       [lc]\tListar contas
       [nu]\tNovo usuário
       [q]\tSair
       => """
    print(menu)

def depositar(saldo, extrato):
    valor = float(input("Escreva o valor que deseja depositar\n"))

    if(valor>0):
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Deposito feito com sucesso\n")
    else:
        print("Operação Invalida\n")

    return saldo, extrato

def sacar(saldo, extrato, numeros_saques, limite):
    valor = float(input("Digite o valor que deseja sacar\n"))

    if(valor <= limite and valor > 0):
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        print("Saque realizado com sucesso\n")
        numeros_saques += 1
    else:
        print("Saque invalido")

    return saldo, extrato, numeros_saques

def e_extrato(saldo, extrato):
    print("----Extrato----")
    if not extrato:
        print("Extrato vazio")
    else:
        print(extrato)
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("-"*15)
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    LIMITE_SAQUES = 3


    while True:
        menu()
        opcao = input()

        if (opcao == "d"):
            saldo, extrato = depositar(saldo, extrato)

        elif (opcao == "s"):
            if(numeros_saques < LIMITE_SAQUES):
               saldo, extrato, numeros_saques = sacar(saldo, extrato, numeros_saques,limite)

            else:
                print("Foi ultrapassado o limite de saque diario\n")

        elif (opcao == "e"):
            e_extrato(saldo, extrato)

        elif (opcao == "q"):
            break

        else:
            print("Opção invalida, por favor selecione novamente")

main()