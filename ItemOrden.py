class ItemOrden:
    def __init__(self,producto,cantidad):
        self.__producto= producto
        self.__cantidad= cantidad

    def get_producto(self):
        return self.__producto

    def set_producto(self,producto):
        self.__producto = producto

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self,cantidad):
        self.__cantidad= cantidad

    def calcular_subtotal(self):
        return self.__producto.get_precio() * self.__cantidad