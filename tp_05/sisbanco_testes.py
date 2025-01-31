import unittest
from sisbanco import Conta, ContaPoupanca, ContaEspecial, ContaImposto, Banco

class TestConta(unittest.TestCase):
    def test_debitar(self):
        conta = Conta("123-X")
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), -5.0)

        conta.creditar(5)
        self.assertEqual(conta.get_saldo(), 0.0)

    def test_get_numero(self):
        conta = Conta("124-Y")
        self.assertEqual(conta.get_numero(), "124-Y")

    def test_get_saldo(self):
        conta = Conta("125-T")
        self.assertEqual(conta.get_saldo(), 0.0)

class TestContaPoupanca(unittest.TestCase):
    def test_render_juros(self):
        conta = ContaPoupanca("253-I")
        taxa = 0.01
        conta.creditar(10)
        conta.render_juros(taxa)
        self.assertEqual(conta.get_saldo(), 10.1)

class TestContaEspecial(unittest.TestCase):
    def test_render_bonus(self):
        conta = ContaEspecial("234-T")
        conta.get_saldo()
        conta.creditar(20)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 20.2)

class TestContaImposto(unittest.TestCase):
    def test_debitar(self):
        conta = ContaImposto("964-G")
        conta.debitar(40)
        self.assertEqual(conta.get_saldo(), -40.04)

class TestBanco(unittest.TestCase):
    def test_cadastrar(self):
        conta = Conta("432-I")
        banco = Banco()
        banco.cadastrar(conta)
        self.assertEqual(conta.get_numero(), "432-I")

    def test_procurar(self):
        conta = Conta("438-I")
        banco = Banco()
        banco.cadastrar(conta)
        banco.procurar(conta)
        self.assertEqual(conta.get_numero(), "438-I")

    def test_saldo(self):
        conta = Conta("438-I")
        banco = Banco()
        banco.saldo(conta)
        self.assertEqual(conta.get_saldo(), 0.0)

    def test_transferir(self):
        origem = Conta("076-U")
        destino = Conta("867-G")
        banco = Banco()
        banco.cadastrar(origem)
        banco.cadastrar(destino)
        banco.creditar(origem, 40)
        banco.transferir(origem, destino, 5.0)
        self.assertEqual(banco.saldo("076-U"), origem.get_saldo())
        self.assertEqual(banco.saldo("867-G"), destino.get_saldo())

if __name__ == "__main__":
    unittest.main()

        