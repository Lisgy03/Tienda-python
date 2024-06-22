class Orden:
    def __init__(self,cliente):
        self.__cliente= cliente
        self.__items= []
        self.__total= 0

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self,cliente):
        self.__cliente = cliente

    def get_items(self):
        return self.__items

    def set_items(self,items):
        self.__items= items

    def get_total(self):
        return self.__total

    def set_total(self,total):
        self.__total = total

    def agregar_item(self,item):
        self.__items.append(item)

    def calcular_total(self):
        total = 0
        for item in self.__items:
            total += item.calcular_subtotal()
        self.__total = total