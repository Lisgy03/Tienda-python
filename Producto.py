class Producto:
    def __init__(self, nombre, precio, categoria):
        self.__nombre = nombre
        self.__precio = precio
        self.__categoria = categoria

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def mostrar_info(self):
        return f"Producto: {self.__nombre}, Precio: {self.__precio}, Categoría: {self.__categoria}"
