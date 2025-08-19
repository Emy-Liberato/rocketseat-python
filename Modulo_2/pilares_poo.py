#Exemplo de herança

print("\n Exemplo de herança")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return

    def emitir_som(self):
        pass #instrução vazia

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismos")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self._saldo = saldo # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor

    def consultar_saldo(self):
        return self._saldo

conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=2000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)

print("\nExemplo de abstração")
from abc import ABC, abstractmethod

# Todos os metodos com @abstractmethod, precisamo ser utilizados obrigatóriamente, nos objeto "filhos"
class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        # Ligação do carro
        return "Carro ligado usando a chave"

    def desligar(self):
        return "Carro desligado usando a chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())