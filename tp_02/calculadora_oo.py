#class: 
# - grupo de objetos com os mesmos atributos e os mesmos comportamentos.
  ###o def __init__(): é usado para configurar ou inicializar atributosespecíficos de cada obj.
    #métodos:
    # - funções associadas a uma classe ou a um objeto.
    # - Eles definem os comportamentos que os objetos dessa classe podem realizar.
class calculadora:
    def soma(self, operando_a, operando_b):
        return operando_a + operando_b
        
    def subtracao(self, operando_a, operando_b = None):
        return operando_a - operando_b
     
    def multiplicacao(self, operando_a, operando_b = None):
        return operando_a * operando_b

    def divisao(self, operando_a, operando_b = None): 
        try: 
            return operando_a/operando_b
        except ZeroDivisionError:
                print("Não é possível realizar divisão por zero")