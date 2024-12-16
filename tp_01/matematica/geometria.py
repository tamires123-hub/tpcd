# Função para calcular a área de uma circunferência
def area_circulo(raio):
    if raio < 0:
        raise ValueError("O raio deve ser um valor positivo.")
    pi = 3.14159 
    return pi * (raio ** 2)

def area_retangulo(base, altura):
    if base < 0 or altura < 0:
        raise ValueError("Base e altura devem ser valores positivos.")
    return base * altura
