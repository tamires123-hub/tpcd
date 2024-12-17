#Classe Abstrata:
# - Refere-se a uima classe que não pode ser instanciada diretamente, mas serve como base para outras classes. 
# - Ela pode definir métodos que serão implementados pelas sub classes; 
# - Garantido que todas as subclasses compartilhem uma interface em comum.
    # - Em Python, são implementadas através do módulo abc.
from abc import ABC, abstractmethod
class ContaAbstrata(ABC):
    def __init__(self, numero):
        self.__numero = numero
        self.__saldo = 0.0
    
    def creditar(self, valor: float) -> None:
        self.__saldo += valor
    
    @abstractmethod
    def debitar(sef, valor: float) -> None:
        pass

    def get_numero(self) -> str:
        return self.__numero
    
    #Esse método funciona como uma função pois possui um retorno
    def get_saldo(self) -> float:
        return self.__saldo

class Conta(ContaAbstrata):
    #__init__: método construtor da classe.
    #self: é uma referência à instancia da classe (obrigatória como 1° parâmetro em métodos de classe).
    #parâmetro: são valores passados na hora da criação do objeto e usados para inicializar os atributos.
    #atributos protegidos começam com (_) e não devem ser acessados fora da classe ou subclasse, mas ainda são acessíveis se necessário.
    #atributos privados começam com (__) e não devem ser acessados fora da classe ou subclasse em nenhuma hipótese.
    def __init__(self, numero: str):
        super().__init__(numero)
        
    #Esse método é um procedimento pois que não retorna nenhum valor.  
    def debitar(self, valor: float) -> None:
        self.__saldo -= valor
    
class Banco:
    def __init__(self, taxa_poupanca: float = 0.001, taxa_imposto: float = 0.001):
        self.__contas = []
        self.__taxa_poupanca = taxa_poupanca
        self.__taxa_imposto = taxa_imposto

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
            conta.render_juros(self.__taxa_poupanca)
        else:
            print(f"A conta {numero} não é uma conta poupança")
            
    def get_taxa_poupanca(self) -> float:
        return self.__taxa_poupanca
    
    def set_taxa_poupanca(self, taxa_poupanca: float) -> None:
        self.__taxa_poupanca = taxa_poupanca

    def render_bonus(self, numero: str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaEspecial):
            conta.render_bonus()
        else: 
            print(f"A conta {numero} não é uma conta especial")

    def get_taxa_imposto(self) -> float:
        return self.get_taxa_imposto
    
    def set_taxa_imposto(self, taxa_imposto: float) -> None:
        self.set_taxa_imposto = taxa_imposto
    
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

class ContaImposto(ContaAbstrata):
    def __init__(self, numero: str):
        super().__init__(numero)
        self.__taxa = 0.001

    def debitar(self, valor: float) -> None:
        self.__saldo = self.__saldo - (valor + (valor * self.__taxa))

    def get_taxa(self) -> float:
        return self.__taxa
    
    def set_taxa(self, taxa: float) -> None:
        self.set__taxa = taxa


