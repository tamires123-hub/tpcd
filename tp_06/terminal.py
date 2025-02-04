from sisbanco import *
from excecoes import *

def terminal():
   sisbanco = Banco()
   while(True):
      print("SisBanco::Bem-Vindo!")
      print(".::Opcoes::.")
      print("[0] Cadastrar Conta")
      print("[1] Creditar")
      print("[2] Debitar")
      print("[3] Transferir")
      print("[4] Consultar Saldo")
      print("[5] Render Juros")
      print("[6] Render Bonus")
      print("[7] Alterar Taxa_Juros")      
      print("[8] Alterar Taxa_Imposto")
      print("[9] Sair")
      opcao = int(input("Digite:"))
      
      if opcao == 0:
         tp_conta = input("Qual o tipo de conta você deseja criar? S - Simples  | P - Poupanca | E - Especial | I - Imposto")
         numero = input("Digite o número da conta: ")

         if tp_conta == "S":
            conta = Conta.cadastrar(numero)
         if tp_conta == "P":
            conta = ContaPoupanca.cadastrar(numero)
         if tp_conta == "E":
            conta = ContaEspecial.cadastrar(numero)
         if tp_conta == "I":
            conta = ContaImposto.cadastrar(numero)

         try:
            sisbanco.cadastrar(conta)
         except VIException as e:
            e.print_mensagem_erro()

      elif opcao == 1:
         #solicite o numero da conta alvo
         #solicite o valor a ser creditado
         #realize a operacao de credito no sisbanco

         numero = input("Digite o número da conta: ")
         valor = float(input("Digite o valor a ser creditado: "))

         try:
            sisbanco.creditar(numero, valor)
         except CIException as e:
            e.print_mensagem_erro()

      elif opcao == 2:
         #solicite o numero da conta alvo
         #solicite o valor a ser debitado
         #realize a operacao de debito no sisbanco
         
         numero = input("Digite o número da conta: ")
         valor = float(input("Digite o valor a ser debitado: "))

         try:
            sisbanco.debitar(numero, valor)
         except CIException as e:
            e.print_mensagem_erro()


      elif opcao == 3:
         #solicite o numero da conta origem
         #solicite o numero da conta destino
         #solicite o valor a ser transferido
         #realize a operacao de transferencia no sisbanco

         origem = input("Digite o número a conta de origem: ")
         destino = input("Digite o número a conta de destino: ")
         valor_trans = float(input("Digite o valor a ser transferido: "))
         
         try:
            sisbanco.transferir(origem, destino, valor_trans)
         except CIException as e:
            e.print_mensagem_erro()


      elif opcao == 4:
         #solicite o numero da conta alvo
         #realize a operacao de obtencao de saldo no sisbanco
         #exiba o saldo na tela

         numero = ("Digite o número a conta: ")

         try:
            sisbanco.saldo(numero)
         except CIException as e:
            e.print_mensagem_erro()
      
      elif opcao == 5:
         #solicite o numero da conta alvo
         #realize a operacao correcao da poupanca no sisbanco

         numero = ("Digite o número a conta: ")

         try:
            sisbanco.render_juros(numero)
         except CIException as e:
            e.print_mensagem_erro()
      
      elif opcao == 6:
         #solicite o numero da conta alvo
         #realize a operacao conversao/rendimento de bonus no sisbanco
         numero = ("Digite o número a conta: ")

         try:
            sisbanco.render_bonus(numero)
         except CIException as e:
            e.print_mensagem_erro()
      
      elif opcao == 7:
         #solicite a nova taxa de correcao da poupanca
         #realize a operacao de alteracao da taxa no sisbanco
         nova_taxa = float(input("Digite a nova taxa de correção da Conta Poupança: "))
         sisbanco.set_taxa_poupanca(nova_taxa)

      elif opcao == 8:
         #solicite a nova taxa de imposto
         #realize a operacao de alteracao da taxa no sisbanco
         nova_taxa = float(input("Digite a nova taxa de correção da Conta Imposto: "))
         sisbanco.set_taxa_imposto(nova_taxa)
         
      elif opcao == 9:
         print("SisBanco::Bye!")
         break

if __name__ == "__main__":

   terminal()