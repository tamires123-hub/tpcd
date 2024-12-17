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
    def __init__(self, taxa: float):
        self.__contas = []
        self.__taxa = taxa
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

    def render_juros(self, numero: str) -> None:
        conta = self.procurar(numero)
        #isinstance(objeto, classe) verifica se um objeto pertence a uma classe ou subclasse específica.
            # - considera a herança
        if isinstance(conta, ContaPoupança):
            conta.render_juros(self.__taxa)
        else:
            print(f"A conta {numero} não é uma conta poupança")
            
    def get_taxa(self) -> float:
        return self.get_taxa
    
    def set_taxa(self, taxa: float) -> None:
        self.set_taxa = taxa

    def render_bonus(self, numero: str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaEspecial):
            conta.render_bonus()
        else: 
            print(f"A conta {numero} não é uma conta especial")
    
#A classe ContaPoupança herda os atributos de Conta, recebendo ela como parâmetro.
#Herança: permite que uma classe (chamada de filha ou subclasse) herde atributos e métodos de outra classe ( chamada de classe pai ou superclasse)
    # - A ideia prncipal é reutilizar o código e permitir que a classe filha herde funcionalidades ou modifiquemo comportamento da superclasse, sem precisar reescrever tudo.
#O super(). é utilizado para chamar o construtor e inicilizar os atributos da classe pai.
class ContaPoupança(Conta):
    def __init__(self, numero: str):
        super().__init__(numero)

    def render_juros(self, taxa: float) -> None:
        self.creditar(self.get_numero() * taxa)

#Na class ContaEspecial estamos sobrescrevendo o método creditar da classe Conta.
class ContaEspecial(Conta):
    def __init__(self, numero: str):
        super().__init__(numero)
        self.__bonus = 0

    def render_bonus(self) -> None:
        super().creditar(self.__bonus)
        self.__bonus = 0
    
    def creditar(self, valor: float) -> None:
        self.__bonus += valor * 0.01
        super().creditar(valor)