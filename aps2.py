import tkinter as tk
from tkinter import simpledialog, messagebox

produtos = {
    "Whey Protein": 100.0,
    "BCAA": 50.0,
    "Creatina": 30.0,
    "Glutamina": 40.0,
    "Multivitamínico": 20.0
}

def comprar_produto():
    produto = lista_produtos.get(lista_produtos.curselection())
    quantidade = simpledialog.askinteger("Quantidade", f"Quantas unidades de {produto} você deseja comprar?")
    if quantidade:
        total = produtos[produto] * quantidade
        messagebox.showinfo("Compra", f"Você comprou {quantidade} unidades de {produto}. Total: R${total:.2f}")

root = tk.Tk()
root.title("Loja de Suplementos")

frame_titulo = tk.Frame(root, pady=10)
frame_titulo.pack(fill=tk.X)

frame_lista = tk.Frame(root, pady=10)
frame_lista.pack(fill=tk.BOTH, expand=True)

frame_comprar = tk.Frame(root, pady=10)
frame_comprar.pack(fill=tk.X)

lbl_titulo = tk.Label(frame_titulo, text="Loja de Suplementos", font=('Arial', 20))
lbl_titulo.pack()

lista_produtos = tk.Listbox(frame_lista)
for produto, preco in produtos.items():
    lista_produtos.insert(tk.END, f"{produto} - R${preco:.2f}")
lista_produtos.pack(fill=tk.BOTH, expand=True)

btn_comprar = tk.Button(frame_comprar, text="Comprar", command=comprar_produto)
btn_comprar.pack()

root.mainloop()
