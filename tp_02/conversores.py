'''
    Converte medidas
'''

''' Converte celsius em fahrenheit '''
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

''' Converte fahrenheit em celsius '''
def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

''' Converte metro em pés '''
def metro_para_pes(metro):
    return metro * 3.28 

''' Converte pés em metros '''
def pes_para_metro(pes):
    return pes/3.28

''' Converte quilometros em milhas '''
def quilometro_para_milhas(quilometro: float) -> float:
    return quilometro/ 1.6

''' Converte milhas em quilometros '''
def milhas_para_quilometro(milhas):
    return milhas * 1.6

''' Converte dias em horas '''
def dia_para_horas(dia):
    return dia * 24
