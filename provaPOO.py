class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print("Subindo")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print("Descendo")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print("Entrando uma pessoa")
        else:
            print(" elevador esta na sua capacidade maxima")
            
    def sair(self):
        if self.atualCapacidade >= 1 :
            self.atualCapacidade -= 1
            print(" saindo uma pessoa")
        else:
            ('ELEVADOR VAZIO')

elevador1 = Elevador(16, 5)

elevador1.subir()
elevador1.descer()
elevador1.entrar()
elevador1.sair()