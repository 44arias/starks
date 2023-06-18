# ----------------------------------------------------------------------------------------------------
# Functions

def menu():
    print("""
        1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
        2. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
        3. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
        4. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
        5. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
        6. Calcular e informar cuál es el superhéroe más y menos pesado.
        7. Acceder al menu del Desafio Stark 01.
        8. Salir.
        """)
    opcion = input("Ingrese una opción: ")
    return opcion

# ----------------------------------------------------------------------------------------------------

def obtener_valores(lista: list, key: str) -> list:
    """
    Retorna una lista con los valores correspondientes a una key específica en cada elemento de la lista.

    Args:
    - lista: Lista de diccionarios.
    - key: Key específica para obtener los valores.

    Returns:
    Una lista con los valores correspondientes a la key en cada elemento de la lista.
    """
    valores = []
    for item in lista:
        valores.append(item[key])
    return valores


# ----------------------------------------------------------------------------------------------------

def encontrar_extremo(lista: list, key: str, comparador: callable) -> dict:
    """
    Encuentra el elemento extremo en la lista según el valor de una key y un comparador especificado.

    Args:
    - lista: Lista de diccionarios.
    - key: Key específica para comparar los valores.
    - comparador: Función de comparación que toma dos argumentos y Returns True si se cumple la condición.

    Returns:
    El elemento extremo de la lista según el valor de la key y el comparador especificado.
    """
    extremo = lista[0]
    for item in lista:
        if comparador(item[key], extremo[key]):
            extremo = item
    return extremo

# ----------------------------------------------------------------------------------------------------

def calcular_promedio(lista: list, key: str) -> float:
    """
    Calcula el promedio de los valores de una key específica en la lista.

    Args:
    - lista: Lista de diccionarios.
    - key: Key específica para calcular el promedio.

    Returns:
    El promedio de los valores de la key en la lista.
    """
    total = sum(float(item[key]) for item in lista)
    promedio = total / len(lista)
    return promedio

# ----------------------------------------------------------------------------------------------------

def mostrar_nombres(lista: list):
    nombres = obtener_valores(lista, 'nombre')
    for nombre in nombres:
        print(nombre)


def mostrar_nombres_y_alturas(lista: list):
    for heroe in lista:
        print(f"Nombre: {heroe['nombre']} \nAltura: {float(heroe['altura'])}")


def mostrar_superheroe_mas_alto(lista: list):
    superheroe_alto = encontrar_extremo(
        lista, 'altura', lambda a, b: float(a) > float(b))
    print(
        f"Superhéroe más alto: {superheroe_alto['nombre']} \nAltura: {float(superheroe_alto['altura'])}")


def mostrar_superheroe_mas_bajo(lista: list):
    superheroe_bajo = encontrar_extremo(
        lista, 'altura', lambda a, b: float(a) < float(b))
    print(
        f"Superhéroe más bajo: {superheroe_bajo['nombre']} \nAltura: {float(superheroe_bajo['altura'])}")


def mostrar_altura_promedio(lista: list):
    promedio = calcular_promedio(lista, 'altura')
    print(f"Altura promedio de los superhéroes: {promedio}")


def mostrar_superheroes_pesados_livianos(lista: list):
    superheroe_mas_pesado = encontrar_extremo(
        lista, 'peso', lambda a, b: float(a) > float(b))
    superheroe_mas_liviano = encontrar_extremo(
        lista, 'peso', lambda a, b: float(a) < float(b))
    print(
        f"Superhéroe más pesado: {superheroe_mas_pesado['nombre']} \nPeso: {float(superheroe_mas_pesado['peso'])}")
    print(
        f"Superhéroe más liviano: {superheroe_mas_liviano['nombre']} \nPeso: {float(superheroe_mas_liviano['peso'])}")

# ----------------------------------------------------------------------------------------------------


