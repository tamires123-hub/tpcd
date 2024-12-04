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

        if opcao == 1:
            numero = input("Digite o número da conta: ")
            valor_add = float(input("Digite o valor a ser creditado: "))
            Banco.creditar(numero, valor_add)

        if opcao == 2:
            numero = input("Digite o número da conta: ")
            valor_sub = float(input("Digite o valor a ser debitado: "))
            Banco.debitar(numero, valor_sub)
        
        if opcao == 3:
            num_origem = input("Digite o número da conta de origem: ")
            num_destino = input("Digite o número da conta de destino: ")
            valor_trans = float(input("Digite o valor a ser transferido: "))
            Banco.transferir(num_origem, num_destino, valor_trans)
        
        if opcao == 4:
            numero = input("Digite o número da conta: ")
            Banco.saldo(numero)

        if opcao == 5:
            numero = input("Digite o número da conta: ")
            Banco.render_juros(numero)
        
        if opcao == 6:
            numero = input("Digite o número da conta: ")
            Banco.render_bonus(numero)

        if opcao == 7:
            pass
        #Falta implementar essa parte 

        elif opcao == 8:
            print("SisBanco::Bye!")
            return

if __name__ == "__main__":
    terminal()