#Arquivo teste que importa o módulo de decomposição procedural que chamado calculadora e testa suas funções.

import calculadora as calc

def testa():
    resul_soma = calc.soma(24)
    resul_subtracao = calc.subtracao(24, 20)
    resul_multiplicacao = calc.multiplicacao(24, 20)
    resul_divisao = calc.divisao(24, 20)
    print(resul_soma, resul_subtracao, resul_multiplicacao, resul_divisao)

if __name__ == "__main__":
    testa()