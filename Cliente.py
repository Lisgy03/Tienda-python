class Cliente:
    def __init__(self,nombre, apellido, id_cliente):
        self.__nombre= nombre
        self.__apellido= apellido
        self.__id_cliente= id_cliente

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self,apellido):
        self.__apellido= apellido

    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self,id_cliente):
        self.__id_cliente = id_cliente

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} {self.__apellido}, ID: {self.__id_cliente}"