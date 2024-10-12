"""
Aqui estamos creando la logica del segundo archivo
"""

# catalogo.py
from pelicula import Pelicula 
import os

class CatalogoPeliculas:
    def __init__(self, ruta):
        self.ruta = ruta

    def agregar_pelicula(self, pelicula):
        with open(self.ruta, 'a') as archivo:
            archivo.write(pelicula.obtener_nombre() + '\n')

    def buscar_pelicula(self, nombre):
        if os.path.exists(self.ruta):
            with open(self.ruta, 'r') as archivo:
                peliculas = archivo.readlines()
                for pelicula in peliculas:
                    if pelicula.strip().lower() == nombre.lower():
                        return True
        return False

    def listar_peliculas(self):
        if os.path.exists(self.ruta):
            with open(self.ruta, 'r') as archivo:
                peliculas = archivo.readlines()
                return [p.strip() for p in peliculas]
        return []

    def organizar_peliculas(self):
        peliculas = self.listar_peliculas()
        peliculas.sort()
        with open(self.ruta, 'w') as archivo:
            for pelicula in peliculas:
                archivo.write(pelicula + '\n')

    def eliminar_catalogo(self):
        if os.path.exists(self.ruta):
            os.remove(self.ruta)

# Lógica del menú
def mostrar_menu():
    print("Menú del catálogo de películas:")
    print("1. Buscar una película")
    print("2. Agregar una película")
    print("3. Organizar todas las películas")
    print("4. Eliminar el catálogo actual para crear uno nuevo")
    print("5. Salir")

def ejecutar_programa():
    catalogo = CatalogoPeliculas("C:/Users/Alejandra Sanchez/Desktop/ADA_Proyecto2/Catalogo.txt")

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
