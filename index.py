import tkinter as tk

def on_button_click():
    user_input = entry.get()
    result_label.config(text="Olá, " + user_input + "!")

def input(root: tk):
    texEncrypted = tk.Label(root, text="Digite seu texto encriptado: ")
    texEncrypted.pack()

    entry = tk.Entry(root)
    entry.pack()

root = tk.Tk()
root.geometry("600x400")
root.title("Encriptador")

input(root)
input(root)

# Cria um botão
button = tk.Button(root, text="Revelar", command=on_button_click)
button.pack()

# Cria um rótulo para exibir o resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Inicia a interface gráfica
root.mainloop()
