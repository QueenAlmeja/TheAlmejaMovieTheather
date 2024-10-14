#Los archivos no tendran comentarios explicativos y se trataron de simplificar lo mejor posible la declaracion de funciones
class Pelicula:
    def __init__(self, nombre, genero):
        self.__nombre = nombre
        self.genero = genero

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f'La consultada es película: {self.__nombre}, y el género es: {self.genero}'
