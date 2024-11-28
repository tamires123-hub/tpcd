class Conta:
    def __init__(self, numero: str):
        self.__numero__ = numero
        self.__saldo__ = 0.0

    def creditar(self, valor: float) -> None:
        self.__saldo += valor

    def debitar(self, valor: float) -> None:
        self.__saldo -= valor
    
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
            if conta.get_numero() == numero:
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
            return conta.get_saldo()
        
    def transferir(self, origem: str, destino: str, valor: float) -> None:
        origem = self.procurar(origem)
        destino = self.procurar(destino)
        if origem is not None and destino is not None:
            origem.debitar(valor)
            destino.creditar(valor)

