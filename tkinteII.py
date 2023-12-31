#Calculadora Simples (com exibição no terminal) Desenvolva uma calculadora
#simples utilizando o Tkinter que permita ao usuário realizar operações matemáticas
#básicas, como adição, subtração, multiplicação e divisão. O programa deve exibir
#botões para os números e as operações, e ao realizar o cálculo, o resultado deve ser
#exibido no terminal.

#importando a biblioteca
from tkinter import *

class Calculadora:
    def __init__(self):
        janela = Tk()
        janela.title("Calculadora")

        # Criando os botões
        self.botao1 = Button(janela, text="1", width=10)
        self.botao2 = Button(janela, text="2", width=10)
        self.botao3 = Button(janela, text="3", width=10)
        self.botao4 = Button(janela, text="4", width=10)
        self.botao5 = Button(janela, text="5", width=10)
        self.botao6 = Button(janela, text="6", width=10)
        self.botao7 = Button(janela, text="7", width=10)
        self.botao8 = Button(janela, text="8", width=10)
        self.botao9 = Button(janela, text="9", width=10)
        self.botao0 = Button(janela, text="0", width=10)

        self.botaoMais = Button(janela, text="+", width=10)
        self.botaoMenos = Button(janela, text="-", width=10)
        self.botaoMult = Button(janela, text="*", width=10)
        self.botaoDiv = Button(janela, text="/", width=10)

        self.botaoIgual = Button(janela, text="=", width=10)
        self.botaoClear = Button(janela, text="C", width=10)
        
        # Posicionando os botões
        self.botao1.grid(row=1, column=0)
        self.botao2.grid(row=1, column=1)
        self.botao3.grid(row=1, column=2)
        self.botao4.grid(row=2, column=0)
        self.botao5.grid(row=2, column=1)
        self.botao6.grid(row=2, column=2)
        self.botao7.grid(row=3, column=0)
        self.botao8.grid(row=3, column=1)
        self.botao9.grid(row=3, column=2)
        self.botao0.grid(row=4, column=1)

        self.botaoMais.grid(row=1, column=3)
        self.botaoMenos.grid(row=2, column=3)
        self.botaoMult.grid(row=3, column=3)
        self.botaoDiv.grid(row=4, column=3)

        self.botaoIgual.grid(row=4, column=2)
        self.botaoClear.grid(row=4, column=0)

        janela.mainloop()

    def somar(self):
        pass

    def subtrair(self):
        pass

    def multiplicar(self):
        pass
    
    def dividir(self):
        pass

    def limpar(self):
        pass

    def calcular(self):
        pass

if __name__ == "__main__":

    c = Calculadora()
    c.calcular()