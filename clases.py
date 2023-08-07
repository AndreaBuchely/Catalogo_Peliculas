import os

class Pelicula:
    def __init__(self,nombre, año, calificacion):
        self.__nombre = nombre
        self.año = año
        self.calificacion = calificacion
    
    def __str__(self):
        return f"Nombre: {self.nombre} Año: {self.año} Calificación: {self.calificacion}"
    
    
    #def __repr__(self):

    # crear metodos de acceso: mostrar el atributo nombre y modificar
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

class CatalogoPelicula:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f'{self.nombre}.txt'

    def agregar_pelicula(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        # abrir el archivo con with 
        # imprimir lo que hay en el archivo ( arhivo.read() )
        #con un print debo mostrar en pantalla todo el listado
        pass

    def eliminar_peliculas(self): #deberia ser eliminar catalogo
        os.remove(self.ruta_archivo) #con esto se elimina el catalogo
        print(f'Archivo eliminado: {self.ruta_archivo}')