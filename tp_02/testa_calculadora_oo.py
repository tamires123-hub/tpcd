from calculadora_oo import calculadora

def teste():
    #Instanciar:
    #-É o processo de criar um objeto a partir de uma classe.
    #-Isso é feito chamando a classe como se fosse uma função, usando parênteses ().
    calc = calculadora()
    res_soma = calc.soma(2,3)
    res_sub = calc.subtracao(24, 20)
    res_mult = calc.multiplicacao(24, 20)
    res_div = calc.divisao(24, 20)

    print(res_soma, res_sub, res_mult, res_div)

if __name__ == "__main__":
    teste()