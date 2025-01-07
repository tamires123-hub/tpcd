import unittest
from sisbanco import Conta, ContaPoupanca

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
        
       
        


if __name__ == "__main__":
    unittest.main()
        