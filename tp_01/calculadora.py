#Temos um módulo, arquivo com definições, que executa as operações elementares através de funções. 
#Decomposição procedural

def soma(operando_a, operando_b):
    return operando_a + operando_b

def subtracao(operando_a, operando_b):
    return operando_a - operando_b

def multiplicacao(operando_a, operando_b):
    return operando_a * operando_b

def divisao(operando_a, operando_b):
    try:
        return operando_a/operando_b
    except ZeroDivisionError:
        print("Não é possível realizar divisão por zero")
