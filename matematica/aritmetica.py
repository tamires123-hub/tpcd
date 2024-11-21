''' Somando e Subtraindo '''

def soma(operando_a, operando_b = None):
        if operando_b is None:
           acumulador += operando_a
        else: 
           acumulador = operando_a + operando_b
        
        return acumulador

def subtrai(operando_a, operando_b = None):
        if operando_b is None:
           acumulador *= operando_a
        else: 
           acumulador = operando_a - operando_b
        
        return acumulador