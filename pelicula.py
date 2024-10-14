#🔴Primero archivo.

class Pelicula:
    #declaramos un constructor empleando __int__
    def __init__(self, nombre, genero):
        self.__nombre = nombre  #self es un metodo que se emplean cuando se construyen clases para acceder a la propiedades que asiganamos a la clase
        self.genero = genero #nueva propiedad agregada

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return f'Película: {self.__nombre}, Género: {self.genero}'

"""
En resumen
Lo primero que hicimos fue definir la class Pelicula para organizar el código  
Creamos un atributo privado empleando dos guines bajos. Los atributos privados permiten proteger la informacion de este atributo y que no sea de facil acceso. En este ejercicio fue el atributo del nombre
Agregamos el atributo del genero ya que hemos creado varios catalogos de peliculas de diferentes generos
"""