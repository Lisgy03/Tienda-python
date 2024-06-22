class Tienda:
    def __init__(self):
        self.__productos = []
        self.__clientes = []
        self.__ordenes = []
        self.__categorias = []

    def get_clientes(self):
        return self.__clientes

    def get_productos(self):
        return self.__productos

    def get_ordenes(self):
        return self.__ordenes

    def get_categorias(self):
        return self.__categorias

    def set_clientes(self, clientes):
        self.__clientes = clientes

    def set_productos(self, productos):
        self.__productos = productos

    def set_ordenes(self, ordenes):
        self.__ordenes = ordenes

    def set_categorias(self, categorias):
        self.__categorias = categorias

    def registrar_producto(self, producto):
        self.__productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.__productos:
            self.__productos.remove(producto)

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        return None

    def registrar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def eliminar_cliente(self, cliente):
        if cliente in self.__clientes:
            self.__clientes.remove(cliente)

    def buscar_cliente_por_nombre(self, nombre):
        for cliente in self.__clientes:
            if cliente.get_nombre() == nombre:
                return cliente
        return None

    def crear_orden(self, orden):
        orden.calcular_total()
        self.__ordenes.append(orden)

    def mostrar_productos(self):
        for producto in self.__productos:
            print(producto.mostrar_info())

    def mostrar_ordenes(self):
        for orden in self.__ordenes:
            print(orden.mostrar_info())

    def agregar_categoria(self, categoria):
        self.__categorias.append(categoria)

    def eliminar_categoria(self, categoria):
        if categoria in self.__categorias:
            self.__categorias.remove(categoria)

    def mostrar_categorias(self):
        for categoria in self.__categorias:
            print(categoria.mostrar_info())
