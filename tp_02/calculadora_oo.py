#class: 
# - grupo de objetos com os mesmos atributos e os mesmos comportamentos.
  ###o def __init__(): é usado para configurar ou inicializar atributosespecíficos de cada obj.
    #métodos:
    # - funções associadas a uma classe ou a um objeto.
    # - Eles definem os comportamentos que os objetos dessa classe podem realizar.
class calculadora:
    def __init__(self):
        self.__acumulador = 0.0

    def soma(self, operando_a, operando_b = None):
        if operando_b is None:
           self.__acumulador += operando_a
        else: 
           self.__acumulador = operando_a + operando_b
        
        return self.__acumulador
        
    def subtracao(self, operando_a, operando_b = None):
        if operando_b is None:
           self.__acumulador *= operando_a
        else: 
           self.__acumulador = operando_a - operando_b
        
        return self.__acumulador
     
    def multiplicacao(self, operando_a, operando_b = None):
        if operando_b is None:
           self.__acumulador /= operando_a
        else: 
           self.__acumulador = operando_a * operando_b
        
        return self.__acumulador

    def divisao(self, operando_a, operando_b = None): 
        try:
            if operando_b is None:
                self.__acumulador += operando_a
            else: 
                self.__acumulador = operando_a / operando_b
        
            return self.__acumulador
        except:
            print('Divisão por zero não existe.')

