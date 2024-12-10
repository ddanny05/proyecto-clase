import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://127.0.0.1:8000/api/productos/"

# Crear la ventana principal
root = tk.Tk()
root.title("CRUD de Productos")
root.geometry("600x400")


def listar_productos():
    respuesta = requests.get(API_URL)
    if respuesta.status_code == 200:
        lista.delete(0, tk.END)
        for producto in respuesta.json():
            lista.insert(tk.END, f"{producto['id']} - {producto['nombre']}")

def agregar_producto():
    datos = {
        "nombre": entrada_nombre.get(),
        "descripcion": entrada_descripcion.get(),
        "precio": entrada_precio.get(),
        "stock": entrada_stock.get()
    }
    respuesta = requests.post(API_URL, json=datos)
    if respuesta.status_code == 201:
        messagebox.showinfo("Éxito", "Producto agregado")
        listar_productos()
    else:
        messagebox.showerror("Error", "No se pudo agregar el producto")

def eliminar_producto():
    seleccion = lista.get(tk.ACTIVE)
    if seleccion:
        producto_id = seleccion.split(" - ")[0]
        respuesta = requests.delete(f"{API_URL}{producto_id}/")
        if respuesta.status_code == 204:
            messagebox.showinfo("Éxito", "Producto eliminado")
            listar_productos()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el producto")

# Configurar la ventana
ventana = tk.Tk()
ventana.title("CRUD de Productos")
ventana.geometry("500x500")

# Campos de entrada
tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Descripción:").pack()
entrada_descripcion = tk.Entry(ventana)
entrada_descripcion.pack()

tk.Label(ventana, text="Precio:").pack()
entrada_precio = tk.Entry(ventana)
entrada_precio.pack()

tk.Label(ventana, text="Stock:").pack()
entrada_stock = tk.Entry(ventana)
entrada_stock.pack()

# Botones
tk.Button(ventana, text="Agregar Producto", command=agregar_producto).pack(pady=5)
tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto).pack(pady=5)

# Lista de productos
lista = tk.Listbox(ventana)
lista.pack(fill=tk.BOTH, expand=True)

tk.Button(ventana, text="Listar Productos", command=listar_productos).pack(pady=5)

ventana.mainloop()
