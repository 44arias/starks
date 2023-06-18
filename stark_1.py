# ----------------------------------------------------------------------------------------------------------------------------------
# Functions 01

from data_stark import *
from stark_0 import *

def menu_dos():
    print("""
        A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
        B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
        C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
        D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
        E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
        F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
        G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
        H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
        I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
        J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
        K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
        L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
        M. Listar todos los superhéroes agrupados por color de ojos.
        N. Listar todos los superhéroes agrupados por color de pelo.
        O. Listar todos los superhéroes agrupados por tipo de inteligencia
        P. Salir.
        """)
    opcion = input("Ingrese una opción: ").capitalize()
    return opcion

# ----------------------------------------------------------------------------------------------------------------------------------

def recorrer_superheroes_genero(lista: list, genero: str) -> None:
    """
    Recorre una lista de superhéroes y muestra por pantalla los nombres de aquellos que coincidan con el género proporcionado.

    Args:
        lista (list): Una lista de diccionarios que representan superhéroes, donde cada diccionario contiene información sobre el nombre y género del superhéroe.
        genero (str): El género de superhéroes que se desea filtrar.

    Returns:
        None
    """
    for heroe in lista:
        if heroe['genero'] == genero:
            print(heroe['nombre'])

# ----------------------------------------------------------------------------------------------------------------------------------

def encontrar_superheroe_mas_alto_genero(lista: list, genero: str) -> dict:
    """
    Encuentra el superhéroe más alto en una lista de superhéroes filtrada por género.

    Args:
        lista (list): Una lista de diccionarios que representan superhéroes, donde cada diccionario contiene información sobre el nombre, género y altura del superhéroe.
        genero (str): El género de superhéroes que se desea filtrar.

    Returns:
        dict: Un diccionario que representa el superhéroe más alto del género especificado.
    """
    superheroes_genero = [heroe for heroe in lista if heroe['genero'] == genero]
    superheroe_alto = encontrar_extremo(
        superheroes_genero, 'altura', lambda a, b: float(a) > float(b))
    return superheroe_alto

# ----------------------------------------------------------------------------------------------------------------------------------

def encontrar_superheroe_mas_bajo_genero(lista: list, genero: str) -> dict:
    """
    Encuentra el superhéroe más bajo en una lista de superhéroes filtrada por género.

    Args:
        lista (list): Una lista de diccionarios que representan superhéroes, donde cada diccionario contiene información sobre el nombre, género y altura del superhéroe.
        genero (str): El género de superhéroes que se desea filtrar.

    Returns:
        dict: Un diccionario que representa el superhéroe más bajo del género especificado.
    """
    superheroes_genero = [heroe for heroe in lista if heroe['genero'] == genero]
    superheroe_bajo = encontrar_extremo(
        superheroes_genero, 'altura', lambda a, b: float(a) < float(b))
    return superheroe_bajo

# ----------------------------------------------------------------------------------------------------------------------------------

def calcular_altura_promedio_genero(lista: list, genero: str) -> float:
    """
    Calcula la altura promedio de los superhéroes en una lista filtrada por género.

    Args:
        lista (list): Una lista de diccionarios que representan superhéroes, donde cada diccionario contiene información sobre el nombre, género y altura del superhéroe.
        genero (str): El género de superhéroes que se desea filtrar.

    Returns:
        float: La altura promedio de los superhéroes del género especificado.
    """
    superheroes_genero = [heroe for heroe in lista if heroe['genero'] == genero]
    promedio = calcular_promedio(superheroes_genero, 'altura')
    return promedio

# ----------------------------------------------------------------------------------------------------------------------------------

def obtener_nombre_superheroe(superheroe: dict) -> str:
    """
    Obtiene el nombre de un superhéroe a partir de un diccionario que lo representa.

    Args:
        superheroe (dict): Un diccionario que contiene información sobre el nombre de un superhéroe.

    Returns:
        str: El nombre del superhéroe.
    """
    return superheroe['nombre']

# ----------------------------------------------------------------------------------------------------------------------------------

def contar_superheroes_por_atributo(lista: list, atributo: str) -> dict:
    """
    Cuenta la cantidad de superhéroes que tienen un valor específico para un atributo dado.

    Args:
        lista (list): Una lista de diccionarios que representan superhéroes, donde cada diccionario contiene información sobre diferentes atributos del superhéroe.
        atributo (str): El nombre del atributo que se desea contar.

    Returns:
        dict: Un diccionario donde las claves son los valores del atributo y los valores son la cantidad de superhéroes que tienen ese valor para el atributo dado.
    """
    contador = {}
    for heroe in lista:
        valor = heroe[atributo]
        if valor not in contador:
            contador[valor] = 0
        contador[valor] += 1
    return contador

# ----------------------------------------------------------------------------------------------------------------------------------

def agrupar_superheroes_por_atributo(lista: list, atributo: str) -> dict:
    """
    Agrupa los superhéroes en una lista según un atributo dado.

    Args:
        lista (list): Una lista de diccionarios que representan superhéroes, donde cada diccionario contiene información sobre diferentes atributos del superhéroe.
        atributo (str): El nombre del atributo por el cual se desea agrupar los superhéroes.

    Returns:
        dict: Un diccionario donde las claves son los valores del atributo y los valores son listas de superhéroes que tienen ese valor para el atributo dado.
    """
    agrupados = {}
    for heroe in lista:
        valor = heroe[atributo]
        if valor not in agrupados:
            agrupados[valor] = []
        agrupados[valor].append(heroe)
    return agrupados

# ----------------------------------------------------------------------------------------------------------------------------------

def superheroe_mas_alto_genero(lista: list, genero: str) -> None:
    """
    Encuentra y muestra por pantalla el superhéroe más alto de un género específico.

    Args:
        lista (list): Una lista de diccionarios que representan superhéroes, donde cada diccionario contiene información sobre el nombre, género y altura del superhéroe.
        genero (str): El género de superhéroes que se desea filtrar.

    Returns:
        None
    """
    superheroe_mas_alto_genero = encontrar_superheroe_mas_alto_genero(lista, genero)
    print(f"Superhéroe más alto de género {genero}: {obtener_nombre_superheroe(superheroe_mas_alto_genero)}")