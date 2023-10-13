from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def beber(self):
        pass

    def respirar(self):
        print(f'{self.nome} está respirando.')

class Mamifero(Animal):
    def comer(self):
        print(f'{self.nome} está comendo com a boca.')

    def beber(self):
        print(f'{self.nome} está bebendo com a boca.')
    
class Ave(Animal):
    def comer(self):
        print(f'{self.nome} está comendo com o bico.')
    
    def beber(self):
        print(f'{self.nome} está bebendo com o bico.')


gato = Mamifero('Gato')
passaro = Ave('passaro')

gato.comer()
gato.beber()
gato.respirar()

passaro.comer()
passaro.beber()
passaro.respirar()