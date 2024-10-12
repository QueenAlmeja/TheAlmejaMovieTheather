"""
Usando los fundamentos de programacion orientada a objetos de Python, vamos a crear un catalogo de peliculas que permitirá a un 
usuario buscar, agregar, listar o borrar las peliculas que se mostraran. 

Nuestro programa requerira que la logica que permitirá ejecutar el programa se ejecute en 2 archivos .py

En el primer archivo estará escrita la lógica de la class Pelicula que se encargara de representar una película con sus atributos y uno 
de estos atributos debe ser privado. Por ahora solo le pondremos el atributo de nombre, pero podríamos ir a agregando otros como: 
["Nombre de Director", "Genero", "Año de extreno"].

En el segundo archivo estará la lógica que permitirá ejecutar el programa. Este archivo se encargará de leer la lista de películas que 
hemos creado en un archivo txt. Además, es en este archivo donde desarrollaremos la lógica para que el usuario pueda :
a. Buscar
b. Agregar
c. Listar
d. Borrar

Empleando un menu de opciones que será lo primero que el programa muestre al momento de ejecutarse.

Vamos con lo primero, el archivo que contengan la class Pelicula
"""

#🔴Primero archivo.

#Lo primero que haremos es definir la class Pelicula para organizar el código  
#El nombre de la clase puede ser cualquier nombre que el programador considere, pero dado el ejercicio, es conveniente que siga la logica del programa empleando palabras que se puedan relacionar
class Pelicula:
    #declaramos un constructor empleando __int__
    def __init__(self, nombre): #self es un metodo que se emplean cuando se construyen clases para acceder a la propiedades que asiganamos a la clase
        self.__nombre = nombre  #Creamos un atributo privado empleando dos guines bajos. Los atributos privados permiten proteger la informacion de este atributo y que no sea de facil acceso

    def obtener_nombre(self):
        return self.__nombre  # Método para acceder al nombre
    
#Seria bueno explicar mejor algunas parte del codigo
#podria agregar el atributo genero a def __int__(self, nombre, genero)

