"""
🔴Aqui estamos creando la logica del segundo archivo
Podria intentar preguntarle al usuario que genero el interesa antes de buscar
"""

# catalogo.py
from pelicula import Pelicula 
import os

class CatalogoPeliculas:
    def __init__(self, ruta):
        self.ruta = ruta

#Se crearon las funciones que permiten buscar, listar, organizar y elminar peliculas 
#Primera funcion
    def buscar_pelicula(self, nombre, genero):
        if os.path.exists(self.ruta):
            with open(self.ruta, 'r') as archivo:
                peliculas = archivo.readlines()
                #aqui deberia una linea con el nombre de la pelicula, genero 
                for pelicula in peliculas:
                    #if pelicula.strip().lower() == nombre.lower():
                    #debo intentar cambiar la linea anterior
                        return True
        return False
#Segunda funcion
    def agregar_pelicula(self, pelicula):
        with open(self.ruta, 'a') as archivo:
            archivo.write(f"{pelicula.obtener_nombre()}, {pelicula.genero} + '\n")
#Tercera funcion
    def listar_peliculas(self):
        if os.path.exists(self.ruta):
            with open(self.ruta, 'r') as archivo:
                peliculas = archivo.readlines()
                return [p.strip() for p in peliculas]
        return []
#Cuarta funcion 
    def organizar_peliculas(self):
        peliculas = self.listar_peliculas()
        peliculas.sort()
        with open(self.ruta, 'w') as archivo:
            for pelicula in peliculas:
                archivo.write(pelicula + '\n')
#Quinta funcion
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta):
            os.remove(self.ruta)

#Creamos una logica que muestre el menu de opciones 
def mostrar_menu():
    print("Menú del catálogo de películas:")
    print("1. Buscar una película")
    print("2. Agregar una película")
    print("3. Organizar todas las películas")
    print("4. Eliminar el catálogo actual para crear uno nuevo")
    print("5. Salir")

"""
Si el usuario elige la opcion 1, quiero mostrar un nuevo menu donde le pregunto si
desea buscar la pelicula por genero y le muestro la lista de generos

💡 Debo crear una nueva funcion que puede ser de la siguiente manera

def genero_pelicula(): 
    question = input = ("Quisieras buscar la pelicula por genero?").capitalize()
        if question = "Si"
            print("Bien, los generos que tenemos son los siguientes:")
            print("Romance, Terror, Ciencia Ficcion, Comedia)
            
            opciones = input("Escribe la opcion que mas te interesa: ").capitalize()
            genero = ["Romance", "Ciencia Ficcion", "Comedia","Terror"]
                if opciones in genero:
                    print(f"Buscando peliculas de genero: {opciones}")
                    #aqui falta logica, emplear el return y get 
        elif question = "No"
            print("Dejaremos que busques el catalogo escribiendo el nombre de la peliculo")
            
"""


def ejecutar_programa():
    catalogo = CatalogoPeliculas("C:/Users/Alejandra Sanchez/Desktop/ADA_Proyecto2/Catalogo.txt")
#aqui, dentro del ciclo while se encuentra la logica que viene despues de preguntar el genero, pero debo mejorarlo
#No logro que esto funciones 😭😭😭😭😭
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Introduce el nombre de la película que deseas buscar: ")
            if catalogo.buscar_pelicula(nombre):
                print(f"La película '{nombre}' está en el catálogo.")
            else:
                print(f"La película '{nombre}' no se encontró en el catálogo.")

        elif opcion == '2':
            nombre = input("Introduce el nombre de la película que deseas agregar: ")
            nueva_pelicula = Pelicula(nombre)
            catalogo.agregar_pelicula(nueva_pelicula)
            print(f"La película '{nombre}' ha sido agregada.")

        elif opcion == '3':
            catalogo.organizar_peliculas()
            print("El catálogo ha sido organizado alfabéticamente.")

        elif opcion == '4':
            confirmacion = input("¿Estás seguro de que deseas eliminar el catálogo? (s/n): ")
            if confirmacion.lower() == 's':
                catalogo.eliminar_catalogo()
                print("El catálogo ha sido eliminado.")

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_programa()
