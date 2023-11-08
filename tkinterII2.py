from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("escolha o dia da semana")

dias_semana = ["segunda feira", "terça feira", "quarta feira",
               "quinta feira", "sexta feira", "sabado"]

combobox = ttk.Combobox(janela, values=dias_semana)
combobox.pack(padx=75, pady=20)

janela.mainloop()