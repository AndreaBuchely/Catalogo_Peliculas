from clases import *  # podia poner Pelicula, CatalogoPelicula, pero el * importa todo

opcion = None

nombre_catalogo = input("Ingrese nombre del catalogo:")
catalogo = CatalogoPelicula(nombre_catalogo)

while opcion != 4:
    try:
        print("Opciones: ")
        print("1. Agregar Pelicula")
        print("2. Listar Pelicula")
        print("3. Eliminar catálogo películas")
        print("4. Salir")

        opcion = int(input("Escribe tu opción ( del 1 al 4):"))

        if opcion == 1:
            nombre_pelicula = input(" Indique el nombre de la pelicula:")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        elif opcion == 2:
            #esta opc no va a funcionar hasta que se desarrolle el metodo listar peliculas de la clase CatalogoPelicula
            catalogo.listar_peliculas()
        elif opcion == 3:
            catalogo.eliminar_peliculas()
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        opcion = 4
else:
    print("Programa finalizado")