import os


class Pelicula:
    def __init__(self,nombre):
        self.__nombre = nombre
                    
    def __str__(self):
        return f"Nombre: {self.nombre}"
           
   
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
        with open(self.ruta_archivo) as f :
            print(f.read())
           

    def eliminar_peliculas(self): 
        os.remove(self.ruta_archivo) 
        print(f'Archivo eliminado: {self.ruta_archivo}')