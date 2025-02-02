from abc import ABC, abstractmethod
from excecoes import *

class ContaAbstrata(ABC):
   def __init__(self, numero:str):
      self.__numero = numero
      self._saldo = 0.0

   def creditar(self, valor:float) -> None:
         if valor is None or valor < 0:
            raise VIException(self.__numero, valor)
         self._saldo += valor

   @abstractmethod
   def debitar(self, valor:float) -> None:
      pass
   
   def get_numero(self) -> str:
      return self.__numero 
   
   def get_saldo(self) -> float:
      return self._saldo


class Conta(ContaAbstrata):
   def __init__(self, numero:str):
      super().__init__(numero)

   def debitar(self, valor:float) -> None:
      if valor is None or valor < 0:
         raise VIException(self.get_numero(), valor)
      self._saldo -= valor

class ContaPoupanca(Conta):
   def __init__(self, numero:str):
      super().__init__(numero)

   def render_juros(self, taxa:float) -> None:
      if taxa is None or taxa <= 0:
         raise TJIException(self.get_numero(), taxa)
      self.creditar(self.get_saldo() * taxa)


class ContaEspecial(Conta):
   def __init__(self, numero:str):
      super().__init__(numero)
      self.__bonus = 0 

   def render_bonus(self) -> None:
      super().creditar(self.__bonus)
      self.__bonus = 0

   def creditar(self, valor:float) -> None:
      self.__bonus += valor * 0.01
      super().creditar(valor)

class ContaImposto(ContaAbstrata):
   def __init__(self, numero:str):
      super().__init__(numero)
      self.__taxa = 0.001

   def debitar(self, valor:float) -> None:
      if (valor + (valor * self.__taxa)) > self._saldo:
         raise SIException(self.get_numero(), self.get_saldo())
      self._saldo -= (valor + (valor * self.__taxa))

   def get_taxa(self) -> float:
      return self.__taxa

   def set_taxa(self, taxa:float) -> None:
      self.__taxa = taxa


class Banco:
   def __init__(self, taxa_poupanca:float=0.001, taxa_imposto:float=0.001):
      self.__contas = []
      self.__taxa_poupanca = taxa_poupanca
      self.__taxa_imposto = taxa_imposto

   def cadastrar(self, conta: ContaAbstrata) -> None:
      if conta is None or not isinstance(conta, ContaAbstrata):
         raise VIException(conta.get_numero(), 0.0)
      
      if self.procurar(conta.get_numero()) is not None:
         raise CEException(conta.get_numero())
      
      if isinstance(conta, ContaImposto):
            conta.set_taxa(self.__taxa_imposto)
      self.__contas.append(conta)


   def procurar(self, numero:str) -> ContaAbstrata:
      for conta in self.__contas:
         if conta.get_numero() == numero:
            return conta
      return None

   def creditar(self, numero:str, valor:float) -> None:
      conta = self.procurar(numero)
      if conta is None:
         raise CIException(numero)
      conta.creditar(valor)

   def debitar(self, numero:str, valor:float) -> None:
      conta = self.procurar(numero)
      if conta is None:
         raise CIException(numero)
      conta.debitar(valor)

   def saldo(self, numero:str) -> float:
      conta = self.procurar(numero)
      if conta is None:
         raise CIException(numero)
      return conta.get_saldo()

   def transferir(self, origem:str, destino:str, valor:float) -> None:
      conta_origem = self.procurar(origem)
      conta_destino = self.procurar(destino)
      if conta_origem is None: 
         raise CIException(origem)
      if conta_destino is None:
         raise CIException(destino)
      conta_origem.debitar(valor)
      conta_destino.creditar(valor)

   def get_taxa_poupanca(self) -> float:
      return self.__taxa_poupanca
      
   def set_taxa_poupanca(self, taxa:float) -> None:
      self.__taxa_poupanca = taxa

   def get_taxa_imposto(self) -> float:
      return self.__taxa_imposto
      
   def set_taxa_imposto(self, taxa:float) -> None:
      self.__taxa_imposto = taxa
      for conta in self.__contas:
         if isinstance(conta, ContaImposto):
            conta.set_taxa(self.__taxa_imposto)

   def render_juros(self, numero:str) -> None:
      conta = self.procurar(numero)
      if conta is None or not isinstance(conta, ContaPoupanca):
         raise CIException(numero)
      conta.render_juros(self.__taxa_poupanca)      

   def render_bonus(self, numero:str) -> None:
      conta = self.procurar(numero)
      if conta is None or not isinstance(conta, ContaEspecial):
         raise CIException(numero)
      conta.render_bonus()
