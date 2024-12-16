acumulador = 0.0

def soma(operando_a, operando_b = None):
    global acumulador 
    if operando_b is None:
        acumulador += operando_a
    else: 
        acumulador = operando_a + operando_b
    return acumulador

def subtracao(operando_a, operando_b = None):
    global acumulador 
    if operando_b is None:
        acumulador -= operando_a
    else:
        acumulador = operando_a - operando_b
    return acumulador