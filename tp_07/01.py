import math
#1.1. Soma Simples
soma = lambda x, y: x + y

#1.2. Verificação de Paridade
paridade = lambda e: True if e%2 == 0 else False

#1.3. Elevar ao Quadrado
num = [2,3,4,5,6,7,8]
quadrado = list(map((lambda num: num**2), num))

#1.4. Composição de Funções

#2.1. Converter para Maiúsculas
palavras = ["python", "lambda", "map"]
maior = list(map(lambda palavras: palavras.upper(), palavras)) 

#2.2 Raiz Quadrada
num = [2,3,4,5,6,7,8]
raiz_quadrada = list(map(lambda x: math.sqrt(x), num))

#2.3 Análise de Strings
frases = ["Python é incrível", "Lambda são úteis", "Map é funcional"]
resultado = list(map(lambda frase: {"palavras": len(frase.split()), "caracters": len(frase)}, frases))

#3.1 Filtrar Números Positivos
list_num = [-10, 15,-20, 25, 0, 30]
resul = list(filter(lambda x: True if x >= 0 else False, list_num))
print(resul)