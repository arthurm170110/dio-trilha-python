menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        print("----------Depósito-----------")
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido! Por favor tente novamente.")

    elif opcao == "s":
        print("-----------Saque------------")
        if numero_saques < LIMITE_SAQUES:
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

    elif opcao == "e":
        print("----------Extrato-----------")
        if extrato:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")