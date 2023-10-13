class cliente:
    def __init__(self, nome, endereço, cpf, genero):
        self.nome = nome
        self.endereço = endereço
        self.cpf = cpf
        self.genero = genero

    def __str__(self):
        return f"Nome: {self.nome}\nEndereço: {self.endereço}\nCPF: {self.cpf}\nGênero: {self.genero}"

nome= input('digite seu nome')

endereço= input('digite seu endereço')

cpf= input('digite seu cpf')

genero= input('digite seu genero')

cliente = cliente(nome, endereço, cpf, genero)

print(cliente)        