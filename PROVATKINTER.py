import tkinter as tk

def converter():
    cm = float(entry_cm.get())
    metros = cm / 100
    label_resultado.config(text=f"Resultado: {metros} metros")

root = tk.Tk()
root.title("Conversor de Centímetros para Metros")

label_cm = tk.Label(root, text="Centímetros:")
label_cm.pack()

entry_cm = tk.Entry(root)
entry_cm.pack()

button_converter = tk.Button(root, text="Converter", command=converter)
button_converter.pack()

label_resultado = tk.Label(root)
label_resultado.pack()

root.mainloop()