import unittest
from sisbanco_bugs import *
#Está faltando detectar 1 erro

class TestConta(unittest.TestCase):
    def test_saldo(self):
        conta = Conta("432-K")
        self.assertEqual(conta.get_saldo(), 0.0)
        
    def test_debitar(self):
        conta = Conta("123-X")
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), -5.0)

    def test_creditar(self):
        conta = Conta("713-H")
        conta.creditar(5)
        self.assertEqual(conta.get_saldo(), 5.0)

    def test_get_numero(self):
        conta = Conta("124-Y")
        self.assertEqual(conta.get_numero(), "124-Y")

    def test_get_saldo(self):
        conta = Conta("125-T")
        self.assertEqual(conta.get_saldo(), 0.0)

class TestContaPoupanca(unittest.TestCase):
    def test_render_juros(self):
        conta = ContaPoupanca("253-I")
        conta.creditar(10)
        conta.render_juros(0.01)
        self.assertEqual(conta.get_saldo(), 10.1)

class TestContaEspecial(unittest.TestCase):
    def test_render_bonus(self):
        conta = ContaEspecial("234-T")
        conta.creditar(20)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 20.2)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 20.2)

class TestContaImposto(unittest.TestCase):
    def test_debitar(self):
        conta = ContaImposto("964-G")
        conta.debitar(40)
        self.assertEqual(conta.get_saldo(), -40.04)

class TestBanco(unittest.TestCase):
    def test_cadastrar_conta_comum(self):
        banco = Banco()
        conta = Conta("432-I")
        banco.cadastrar(conta)
        self.assertEqual(banco.procurar("432-I"), conta)
    
        contaI = ContaImposto("234-L")
        banco.cadastrar(contaI)
        self.assertEqual(contaI.get_taxa(), banco.get_taxa_imposto())

    def test_creditar(self):
        banco = Banco()
        conta = Conta("501-B")
        banco.cadastrar(conta)
        banco.creditar("501-B", 100.0)
        self.assertEqual(conta.get_saldo(), 100.0)

    def test_debitar_conta(self):
        banco = Banco()
        conta = Conta("502-D")
        banco.cadastrar(conta)
        banco.debitar("502-D", 50.0)
        self.assertEqual(conta.get_saldo(), -50.0)

    def test_saldo(self):
        conta = Conta("438-I")
        banco = Banco()
        banco.cadastrar(conta)
        self.assertEqual(banco.saldo("438-I"), conta.get_saldo())

    def test_transferir(self):
        banco = Banco()
        origem = Conta("076-U")
        destino = Conta("867-G")
        banco.cadastrar(origem)
        banco.cadastrar(destino)
        banco.creditar(origem, 40)
        banco.transferir(origem, destino, 5.0)
        self.assertEqual(banco.saldo("076-U"), origem.get_saldo())
        self.assertEqual(banco.saldo("867-G"), destino.get_saldo())
    
    def test_get_taxa_poupanca(self):
        banco = Banco()
        self.assertEqual(banco.get_taxa_poupanca(), 0.001)
    
    def test_set_taxa_poupanca(self):
        banco = Banco()
        banco.set_taxa_poupanca(0.07)
        self.assertEqual(banco.get_taxa_poupanca(), 0.07)

    def test_get_taxa_imposto(self):
        banco = Banco()
        self.assertEqual(banco.get_taxa_imposto(), 0.001)
    
    def test_set_taxa_imposto(self):
        banco = Banco()
        banco.set_taxa_imposto(0.003)
        self.assertEqual(banco.get_taxa_imposto(), 0.003)
    
    def test_render_juros(self):
        conta = ContaPoupanca("638-M")
        banco = Banco()
        banco.cadastrar(conta)
        banco.creditar("638-M", 10)
        banco.render_juros("638-M")
        self.assertEqual(conta.get_saldo(), 10.01)

    def test_render_bonus(self):
        conta = ContaEspecial("832-N")
        banco = Banco()
        banco.cadastrar(conta)
        banco.creditar("832-N", 12)
        banco.render_bonus("832-N")
        self.assertEqual(conta.get_saldo(), 12.12)

if __name__ == "__main__":
    unittest.main()    