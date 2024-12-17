class Conta:
    #__init__: método construtor da classe.
    #self: é uma referência à instancia da classe (obrigatória como 1° parâmetro em métodos de classe).
    #parâmetro: são valores passados na hora da criação do objeto e usados para inicializar os atributos.
    def __init__(self, numero: str):
        self.__numero = numero
        self.__saldo = 0.0
    #Esse método é um procedimento pois que não retorna nenhum valor.
    def creditar(self, valor: float) -> None:
        self.__saldo += valor
    
    def debitar(self, valor: float) -> None:
        self.__saldo -= valor
    #Esse método funciona como uma função pois possui um retorno
    def get_numero(self) -> str:
        return self.__numero
    
    def get_saldo(self) -> float:
        return self.__saldo

class Banco:
    def __init__(self):
        self.__contas = []
    
    def cadastrar(self, conta: Conta) -> None:
        self.__contas.append(conta)

    def procurar(self, numero: str) -> Conta:
        for conta in self.__contas:
            if conta.get_numero == conta:
                return conta
        return None

    def creditar(self, numero: str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.creditar(valor)

    def debitar(self, numero: str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)

    def saldo(self, numero: str) -> float:
        conta = self.procurar(numero)
        if conta is not None:
            conta.get_saldo()

    def transferir(self, origem: str, destino: str, valor: float) -> None:
        origem = self.procurar(origem)
        destino = self.procurar(destino)
        if origem is not None and destino is not None:
            origem.debitar(valor)
            destino.creditar(valor)