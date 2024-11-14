class calculadora():
    #criando um atributo privado interno chamado acumulador
    def __init__(self):
        self.__acumulador = 0.0

    def soma(self, operando_a, operando_b = None):
        if operando_b is None:
           self.__acumulador += operando_a
        else: 
           self.__acumulador = operando_a + operando_b
        
        return self.__acumulador

    
    def subtrai(self, operando_a, operando_b = None):
        if operando_b is None:
           self.__acumulador *= operando_a
        else: 
           self.__acumulador = operando_a - operando_b
        
        return self.__acumulador
    
    def multiplica(self, operando_a: None, operando_b: None):
        if operando_b is None:
           self.__acumulador /= operando_a
        else: 
           self.__acumulador = operando_a * operando_b
        
        return self.__acumulador

    def dividi(self, operando_a: None, operando_b: None):
        try:
            if operando_b is None:
                self.__acumulador += operando_a
            else: 
                self.__acumulador = operando_a / operando_b
        
            return self.__acumulador
        except:
            print('Divisão por zero não existe.')


