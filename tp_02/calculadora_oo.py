class calculadora():
    def soma(operando_a, operando_b):
       return operando_a + operando_b
    
    def subtrai(operando_a, operando_b):
        return operando_a - operando_b
    
    def multiplica(operando_a, operando_b):
        return operando_a * operando_b

    def dividi(operando_a, operando_b):
        try:
            return operando_a/operando_b
        except:
            print('Divisão por zero não existe.')


