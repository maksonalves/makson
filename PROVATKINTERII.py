import tkinter as tk
from tkinter import messagebox

def fazer_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if len(senha) <= 6:
        messagebox.showerror("Erro", "A senha deve ter mais de seis dígitos!")
    elif '@' not in email:
        messagebox.showerror("Erro", "O e-mail deve conter o caractere '@'!")
    else:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

root = tk.Tk()
root.title("Login")
root.geometry("300x200")

label_email = tk.Label(root, text="E-mail:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

button_login = tk.Button(root, text="Login", command=fazer_login)
button_login.pack()

root.mainloop()