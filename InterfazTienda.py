import tkinter as tk
from tkinter import messagebox, simpledialog
from Producto import Producto
from Cliente import Cliente
from Orden import Orden
from Categoria import Categoria
from Tienda import Tienda
from ItemOrden import ItemOrden

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.tienda = Tienda()
        self.root.title("Caja")

        self.color_fondo = "#D8BFD8"
        self.color_boton = "#9370DB"
        self.color_registrar = "#BA55D3"

        self.frame = tk.Frame(root, bg=self.color_fondo)
        self.frame.pack(padx=20, pady=20)

        image_path = "Tienda.png"
        self.image = tk.PhotoImage(file=image_path)

        self.image_label = tk.Label(self.frame, image=self.image, bg=self.color_fondo)
        self.image_label.grid(row=0, column=0, columnspan=2)

        tk.Label(self.frame, text="Registrar Producto", bg=self.color_fondo, fg="#333333").grid(row=1, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Nombre del Producto:", bg=self.color_fondo, fg="#333333").grid(row=2, column=0, sticky="e")
        self.nombre_producto_entry = tk.Entry(self.frame)
        self.nombre_producto_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Precio del Producto:", bg=self.color_fondo, fg="#333333").grid(row=3, column=0, sticky="e")
        self.precio_producto_entry = tk.Entry(self.frame)
        self.precio_producto_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Categoría del Producto:", bg=self.color_fondo, fg="#333333").grid(row=4, column=0, sticky="e")
        self.categoria_producto_entry = tk.Entry(self.frame)
        self.categoria_producto_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="Registrar Cliente", bg=self.color_fondo, fg="#333333").grid(row=5, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Nombre del Cliente:", bg=self.color_fondo, fg="#333333").grid(row=6, column=0, sticky="e")
        self.nombre_cliente_entry = tk.Entry(self.frame)
        self.nombre_cliente_entry.grid(row=6, column=1)

        tk.Label(self.frame, text="Apellido del Cliente:", bg=self.color_fondo, fg="#333333").grid(row=7, column=0, sticky="e")
        self.apellido_cliente_entry = tk.Entry(self.frame)
        self.apellido_cliente_entry.grid(row=7, column=1)

        tk.Label(self.frame, text="ID del Cliente:", bg=self.color_fondo, fg="#333333").grid(row=8, column=0, sticky="e")
        self.id_cliente_entry = tk.Entry(self.frame)
        self.id_cliente_entry.grid(row=8, column=1)

        self.boton_crear_orden = tk.Button(self.frame, text="Crear Orden", bg=self.color_boton, fg="white", command=self.crear_orden)
        self.boton_crear_orden.grid(row=9, column=0, columnspan=2, pady=10)

    def registrar_producto(self):
        nombre = self.nombre_producto_entry.get()
        if not nombre:
            messagebox.showerror("Error", "Debe ingresar un nombre de producto.")
            return

        try:
            precio = float(self.precio_producto_entry.get())
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número.")
            return

        categoria = self.categoria_producto_entry.get()
        if not categoria:
            messagebox.showerror("Error", "Debe ingresar una categoría de producto.")
            return

        producto = Producto(nombre, precio, categoria)
        self.tienda.registrar_producto(producto)
        messagebox.showinfo("Producto:", f"Producto registrado: {nombre}, Precio: {precio}, Categoría: {categoria}")

    def registrar_cliente(self):
        nombre = self.nombre_cliente_entry.get()
        if not nombre:
            messagebox.showerror("Error", "Debe ingresar un nombre de cliente.")
            return

        apellido = self.apellido_cliente_entry.get()
        if not apellido:
            messagebox.showerror("Error", "Debe ingresar un apellido de cliente.")
            return

        id_cliente = self.id_cliente_entry.get()
        if not id_cliente:
            messagebox.showerror("Error", "Debe ingresar un ID de cliente.")
            return

        cliente = Cliente(nombre, apellido, id_cliente)
        self.tienda.registrar_cliente(cliente)
        messagebox.showinfo("Registro de Cliente", f"Cliente registrado: {nombre} {apellido}, ID: {id_cliente}")

    def crear_orden(self):
        self.registrar_producto()
        self.registrar_cliente()

        if not self.tienda.get_clientes():
            messagebox.showerror("Error", "No hay clientes registrados.")
            return

        cliente = self.tienda.get_clientes()[-1]
        self.orden_actual = Orden(cliente)

        productos = self.tienda.get_productos()
        if not productos:
            messagebox.showinfo("Productos", "No hay productos registrados.")
            return

        for producto in productos:
            cantidad = simpledialog.askinteger("Cantidad", f"Ingrese la cantidad de {producto.get_nombre()}:")
            if not cantidad:
                messagebox.showerror("Error", "Debe ingresar una cantidad válida.")
                continue

            item_orden = ItemOrden(producto, cantidad)
            self.orden_actual.agregar_item(item_orden)

        self.orden_actual.calcular_total()
        self.tienda.crear_orden(self.orden_actual)
        messagebox.showinfo("Creación de Orden", f"Orden creada para cliente {cliente.get_nombre()} {cliente.get_apellido()} con total a pagar: {self.orden_actual.get_total()}")

if __name__ == "__main__":
    root = tk.Tk()
    menu = Interfaz(root)
    root.mainloop()
