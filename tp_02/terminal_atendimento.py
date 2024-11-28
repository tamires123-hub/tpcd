from sisbanco import Banco, Conta

def terminal():
    sisbanco = Banco()
    while(True):
        print("SisBanco:: Bem-Vindo!")
        print(".::Opções::.")
        print("[0] - CriarConta")
        print("[1] - Creditar")
        print("[2] - Debitar")
        print("[3] - Transferir")
        print("[4] - Saldo")
        print("[5] - Sair")
        opcao = input("Digite: ")

        if opcao == 0:
            numero = input("Digite o número da conta: ")
            conta = Conta(numero)
            conta.cadastrar()