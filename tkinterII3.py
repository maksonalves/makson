from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Janela Principal")

tree = ttk.Treeview(janela)

tree["columns"] = ("nome", "email", "telefone")

tree.column("#0", width=100, minwidth=100, anchor=CENTER)
tree.column("nome", width=150, minwidth=150, anchor=CENTER)
tree.column("email", width=150, minwidth=150, anchor=CENTER)
tree.column("telefone", width=150, minwidth=150, anchor=CENTER)

tree.heading("#0", text="ID", anchor=CENTER)
tree.heading("nome", text="Nome", anchor=CENTER)
tree.heading("email", text="E-mail", anchor=CENTER)
tree.heading("telefone", text="Telefone", anchor=CENTER)

tree.insert("", 0, text="1", values=("João", "joao.silva@gmail.com", "(11) 99999-9999"))
tree.insert("", 1, text="2", values=("Maria", "maria.santos@gmail.com", "(11) 99999-9999"))

tree.pack(padx=10, pady=10)

janela.mainloop()
