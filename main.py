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

def new_user(usuario):
    cpf = input("Digite o cpf [somente número]")

    #verificar se usuario existe
    for i in usuario:
        if i["cpf"] == cpf:
            print("Usuario já existe\n")
            return None

    #se não existe criar um dic e adicionar a lista
    nome = str(input("Digite o nome do usuario\n"))
    data_nasc = (input("Digite sua data de nascimento (dd-mm-aaaa)\n"))
    endereco = input("Informe seu endereço\n")

    usuario.append({"nome": nome, "data_nascimento": data_nasc, "cpf" : cpf, "endereco": endereco})
    print("Usuario criado com sucesso\n")

def new_account(n_conta, contas, AGENCIA, usuario):
    cpf = input("Digite o cpf do usuario\n")

    ver = 0
    #verificar se usuario exite
    for i in usuario:
        if i["cpf"] == cpf:
            ver = 1

            n_conta = n_conta + 1
            contas.append({"agencia": AGENCIA, "numero_conta": n_conta, "usuario": i})

            print("Conta cadastrada com sucesso")

            break

    if ver == 0:
        print("Não existe usuario cadastrado\n")
        return None

    return n_conta

def list_acc(contas):
    for i in contas:
        print(f"Agencia: {i['agencia']}")
        print(f"Numero da conta: {i['numero_conta']}")
        print(f"Usuario: {i['usuario']['nome']}")
        print("-"*20)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    usuario = []
    n_conta = 0
    contas = []


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

        elif (opcao == "nu"):
            new_user(usuario)

        elif (opcao == "nc"):
            n_conta = new_account(n_conta, contas, AGENCIA, usuario)

        elif (opcao == "lc"):
            list_acc(contas)

        elif (opcao == "q"):
            break

        else:
            print("Opção invalida, por favor selecione novamente")

main()