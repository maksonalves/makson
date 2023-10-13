class Cachorro:
    def __init__(self, nome, raça, peso):
        self.nome = nome 
        self.raça = raça
        self.peso = peso
    def comer(self):
        return "Croc croc croc"

akita = Cachorro("Rex", "Akita", 20)
        
beagle = Cachorro("Toto", "Baegle", 10)

print(f"O chachorro {akita.nome} da raça {akita.raça} pesa {akita.peso}kg e come:" 
      f"{akita.comer()}")

print(f"O chachorro {beagle.nome} da raça {beagle.raça} pesa {beagle.peso}kg e come:"
      f"{beagle.comer()}")

class Gato:
    def __init__(self, nome, raça, peso):
        self.nome = nome
        self.raça = raça
        self.peso = peso

    def derrubarcoisas(self):
        return print(f"O gato {self.nome} derruba coisas")

gato = Gato(nome ="jason", raça="cisanês", peso=3.2)

print(gato.derrubarcoisas())

