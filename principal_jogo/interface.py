import tkinter as tk

def janela():
    janela = tk.Tk()

    janela.title("OPUS")
    janela.geometry("800x600")
    janela.configure(bg="#383838")

    titulo = tk.Label(janela, text="OPUS", font=("Times new roman", 50), bg="#383838", fg="white")

    titulo.pack(pady=20)
    janela.mainloop()

def nome():
    nome = tk.Entry(janela, font=("Times new roman", 16), bg="#999999", fg="black", width=30)
    return nome
nome.pack()
janela.mainloop()

def botao():
    botao = tk.Button(
            janela, text="INICIAR INVESTIGAÇÃO", font=("Arial", 12, "bold"),)
    return botao
    botao.pack(pady=10)
    janela.mainloop()


