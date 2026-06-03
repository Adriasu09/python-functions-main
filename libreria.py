"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""

# Escribe tu código aquí
# Prueba la función con algunos valores
def agregar_libro(titulo, autor):
    libro = {'titulo': titulo, 'autor': autor}
    return libro

"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""

libros = [
    {
        'titulo': 'Autor',
        'autor': 'maria'
    },
    {
        "titulo": "prueba",
        "autor": "nana"
    },
    {
        "titulo": "otro mas",
        "autor": "Luna"
    }
]

# Escribe tu código aquí
# Prueba la función con algunos valores
def listar_libros(libros):
    lista_titulos = []
    for libro in libros:
        lista_titulos.append(libro['titulo'])

    #print(lista_titulos)
    return lista_titulos

listar_libros(libros)

"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""

# Escribe tu código aquí
def buscar_libro(libros, titulo):
    libro_encontrado = None
    for libro in libros:
        if libro['titulo'] == titulo:
            libro_encontrado = libro
            break
    print(f"Este es el resultado {libro_encontrado}")
    return libro_encontrado

# Prueba la función con algunos valores
buscar_libro(libros, "prueba")

"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""

# Escribe tu código aquí
def quitar_libro(libros, titulo):
    libro_encontrado = False
    try:
        for index, libro in enumerate(libros):
            if libro['titulo'] == titulo:
                libros.pop(index)
                libro_encontrado = True
                print(f"El libro {titulo}, ha sido eliminado con exito")
                break
        if not libro_encontrado:
            raise ValueError("El libro no ha sido encontrado")
    except ValueError as e:
        print(e)
    return libros

# Prueba la función con algunos valores
quitar_libro(libros, "prueba")


"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""

# Escribe tu código aquí

def crear_inventario(libros):
    inventario = {}
    for libro in libros:
        autor = libro['autor']
        if autor in inventario:
            inventario[autor] += 1
        else:
            inventario[autor] = 1
    return inventario

# Prueba la función con algunos valores

libros_inventario = [
    {"titulo": "Libro 1", "autor": "maria"},
    {"titulo": "Libro 2", "autor": "nana"},
    {"titulo": "Libro 3", "autor": "maria"},
    {"titulo": "Libro 4", "autor": "Luna"},
    {"titulo": "Libro 5", "autor": "maria"},
    {"titulo": "Libro 6", "autor": "nana"},
]

print(crear_inventario(libros_inventario))

"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""

# Escribe tu código aquí
def libros_por_autor(libros, autor):
    libros_por_autor = []
    for libro in libros:
        if libro['autor'] == autor:
            libros_por_autor.append(libro['titulo'])
    return libros_por_autor

# forma simplificada como un filter + .map en js
def libros_por_autor_2(libros, autor):
    return [libro['titulo'] for libro in libros if libro['autor'] == autor]


# Prueba la función con algunos valores

print(libros_por_autor(libros_inventario, "maria"))
print(libros_por_autor_2(libros_inventario, "maria"))

"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""

# Escribe tu código aquí

# Prueba la función con algunos valores

