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

        elif opcao == 1:
            numero = input("Digite o número da conta: ")
            valor_add = float(input("Digite o valor a ser creditado: "))
            sisbanco.creditar(numero, valor_add)

        elif opcao == 2:
            numero = input("Digite o número da conta: ")
            valor_sub = float(input("Digite o valor a ser debitado: "))
            sisbanco.debitar(numero, valor_sub)
        
        elif opcao == 3:
            num_origem = input("Digite o número da conta de origem: ")
            num_destino = input("Digite o número da conta de destino: ")
            valor_trans = float(input("Digite o valor a ser transferido: "))
            sisbanco.transferir(num_origem, num_destino, valor_trans)
        
        elif opcao == 4:
            numero = input("Digite o número da conta: ")
            sisbanco.saldo(numero)

        elif opcao == 5:
            numero = input("Digite o número da conta: ")
            sisbanco.render_juros(numero)
        
        elif opcao == 6:
            numero = input("Digite o número da conta: ")
            sisbanco.render_bonus(numero)

        elif opcao == 7:
            try:
                nova_taxa = float(input('Determine a nova taxa:'))
                sisbanco.set_taxa(nova_taxa)

            except ValueError:
                print("Erro: A taxa informada não é válida. Por favor, insira um número.")

        elif opcao == 8:
            print("SisBanco::Bye!")
            return

if __name__ == "__main__":
    terminal()