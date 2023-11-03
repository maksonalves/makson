'''from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Janela Principal")

        self.notebook = ttk.Notebook(self.janela)

        self.guia1()
        self.guia2()
        self.guia3()

        self.notebook.pack(padx=10, pady=10)

        self.janela.mainloop()

    def guia1(self):
        guia1 = ttk.Frame(self.notebook)
        self.notebook.add(guia1, text="Guia 1")

        dias_semanas = ["Domingo", "Segunda", "Terça", 
                        "Quarta", "Quinta", "Sexta", "Sábado"]
        
        combobox = ttk.Combobox(guia1, values=dias_semanas)
        combobox.pack(padx=10, pady=10)
    
    def guia2(self):
        guia2 = ttk.Frame(self.notebook)
        self.notebook.add(guia2, text="Guia 2")

        self.label2 = Label(guia2, text="Label 2")
        self.entry = Entry(guia2)

        self.label2.pack(padx=10, pady=10)
        self.entry.pack(padx=10, pady=10)
    
    def guia3(self):
        guia3 = ttk.Frame(self.notebook)
        self.notebook.add(guia3, text="Guia 3")

        self.button = Button(guia3, text="Button 3")
        self.button.pack(padx=10, pady=10)

app = Application()'''

'''from tkinter import *
from tkinter import ttk

def comeca_progresso():
    botao_iniciar.configure(state=DISABLED)
    preenche_progresso(2)

def preenche_progresso(value):
    barra_de_progresso["value"] = value

    if value < 100:
        value += 1
        janela.after(20, preenche_progresso, value)
    else:
        botao_iniciar.configure(state=NORMAL)

janela = Tk()
janela.title("escolha")

barra_de_progresso = ttk.Progressbar(janela, length=300, mode="indeterminate")
barra_de_progresso.pack(pady=10)

botao_iniciar = Button(janela, text="iniciar", command=comeca_progresso)

botao_iniciar.pack(pady=10)

janela.mainloop()'''

'''
from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("escolha")

label1 = ttk.Label(janela, text="text1")
label1.pack(pady=10)

separador = ttk.Separator(janela, orient=HORIZONTAL)
separador.pack(padx=50, pady=30)

label2 = ttk.Label(janela, text="text2")
label2.pack(pady=10)

janela.mainloop()'''


from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("exemplo de sizegrip")

janela.resizable(True,True)

sizegrip = ttk.Sizegrip(janela)
sizegrip.pack(anchor=SE, padx=3, pady=3, expand=True)

janela.mainloop()

