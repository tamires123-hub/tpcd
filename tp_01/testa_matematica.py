import matematica
from matematica.estatistica import media

def testa():
    print(matematica.soma(2,2))
    print(matematica.subtracao(3,2))
    print(matematica.area_circulo(5))
    print(matematica.area_retangulo(12, 23))
    print(media.media(list([1,2,3,4,5,6,7])))

if __name__ == "__main__":
    testa()