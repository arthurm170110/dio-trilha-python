def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    if numero_saques < limite_saques:
        valor = float(input("Digite o valor do saque: "))
        if saldo >= valor:
            if valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Limite de saque permitido é de R$ 500.00! Por favor tente novamente.")
        else:
            print("Saldo insuficiente! Por favor tente novamente.")
    else:
        print("Limite de saques diários atingido! Por favor tente novamente amanhã.")
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! Por favor tente novamente.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    if extrato:
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")


def cadastrar_cliente(nome, data_nascimento, cpf, endereco, clientes):
    if not clientes:
        clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("\nCliente cadastrado com sucesso!")
    else:
        for cliente in clientes:
            if cpf == cliente["cpf"]:
                print("\nCliente com esse CPF já cadastrado!")
                return clientes
        clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("\nCliente cadastrado com sucesso!")
    return clientes


def cadastrar_conta(clientes, contas, agencia, numero_conta, cpf):
    for cliente in clientes:
        if cpf == cliente["cpf"]:
            numero_conta += 1
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente})
            print("\nConta criada com sucesso!")
            return contas, numero_conta
    print("\nCliente não encontrado! Por favor tente novamente.")
    return contas, numero_conta


def menu():
    menu = """

    [u] Cadastrar Cliente
    [l] Listar Clientes
    [c] Criar Conta Corrente
    [z] Listar Contas Correntes
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu).lower()


def main():
    clientes = []
    contas = []
    AGENCIA = "0001"
    numero_conta = 0
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = menu()

        if opcao == "d":
            print("----------Depósito-----------")
            valor = float(input("Digite o valor do depósito: "))
            informacoes_deposito = depositar(saldo, valor, extrato)
            saldo = informacoes_deposito[0]
            extrato = informacoes_deposito[1]
            

        elif opcao == "s":
            print("-----------Saque------------")
            informacoes_saque = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            saldo = informacoes_saque[0]
            extrato = informacoes_saque[1]
            numero_saques = informacoes_saque[2]

        elif opcao == "e":
            print("----------Extrato-----------")
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            print("----------Cadastrar Cliente-----------")
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento(dd/mm/yyyy): ")
            cpf = str(input("CPF: "))
            endereco = input("Endereço: ")
            clientes = cadastrar_cliente(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, clientes=clientes)

        elif opcao == "l":
            print("----------Lista de Clientes-----------")
            if clientes:
                for cliente in clientes:
                    print(f"Nome: {cliente['nome']}\nData de Nascimento: {cliente['data_nascimento']}\nCPF: {cliente['cpf']}\nEndereço: {cliente['endereco']}\n")
                    print("-"*50)
            else:
                print("Não há clientes cadastrados.")

        elif opcao == "c":
            print("----------Cadastrar Conta Corrente-----------")
            cpf = input("Digite o CPF do cliente: ")
            informacoes_conta = cadastrar_conta(clientes, contas, AGENCIA, numero_conta, cpf)
            contas = informacoes_conta[0]
            numero_conta = informacoes_conta[1]

        elif opcao == "z":
            print("----------Lista de Contas Correntes-----------")
            if contas:
                for conta in contas:
                    print(f"Agência: {conta['agencia']}\nNúmero da Conta: {conta['numero_conta']}\nCliente: {conta['cliente']['nome']}\nCPF: {conta['cliente']['cpf']}\n")
                    print("-"*50)
            else:
                print("Não há contas correntes cadastradas.")
            
        elif opcao == "q":
            print("Saindo...")
            break

        else:
            print("Operação inválida! Por favor selecione novamente a operação desejada.")


main()