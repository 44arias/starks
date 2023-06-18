from data_stark import *
import os

# ----------------------------------------------------------------------------------------------------------------------------------
# Functions 02
#0

def stark_normalizar_datos(lista: list, x = True) -> None:
    """
    Normaliza los datos numéricos en la lista de héroes.

    Args:
        lista (list): Lista de diccionarios que representan a los héroes.

    Returns:
        None

    """
    if not lista:
        print("Error: Lista de héroes vacía")
        return

    datos_modificados = False

    for heroe in lista:
        for key, value in heroe.items():
            if key in ["altura", "peso", "fuerza", "inteligencia"]:
                try:
                    if key == "altura":
                        heroe[key] = float(value)
                    elif key == "peso":
                        heroe[key] = float(value)
                    elif key == "fuerza":
                        heroe[key] = int(value)
                    elif key == "inteligencia":
                        heroe[key] = int(value)
                    datos_modificados = True
                except (ValueError, TypeError):
                    pass
                
    if x:
        if datos_modificados:
            print("Datos normalizados")
        return lista
        
lista_personajes_normalizada = stark_normalizar_datos(lista_personajes, False)

# ----------------------------------------------------------------------------------------------------------------------------------
#1.1

def obtener_nombre(heroe: dict) -> str:
    """
    Obtiene el nombre formateado de un héroe.

    Recibe un diccionario que representa a un héroe y devuelve un string con el nombre
    formateado en el siguiente formato: 'Nombre: {nombre_del_heroe}'.

    Parameters:
        heroe (dict): Un diccionario que representa a un héroe.

    Returns:
        str: El nombre formateado del héroe.

    """
    nombre = heroe.get('nombre', '')
    return f'Nombre: {nombre}'

#1.2
def imprimir_dato(dato: str) -> None:
    """
    Imprime un dato en la consola.

    Parameters:
        dato (str): El dato a imprimir.

    Returns:
        None: Esta función no retorna ningún valor.
    """
    print(dato)
    
#1.3
def stark_imprimir_nombres_heroes(heroes: list) -> int:
    """
    Imprime por consola el nombre de cada superhéroe en la lista de héroes.

    Parameters:
        heroes (list): Una lista de diccionarios que representan a los héroes con sus respectivos atributos.

    Returns:
        int: Retorna -1 si la lista de héroes está vacía, de lo contrario retorna 0.
    """
    if not heroes:
        print("Error: Lista de héroes vacía")
        return -1

    for heroe in heroes:
        nombre = obtener_nombre(heroe)
        imprimir_dato(nombre)

    return 0

# ----------------------------------------------------------------------------------------------------------------------------------
#2

def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    """
    Obtiene el nombre y el dato de un héroe según la clave especificada.

    Args:
        heroe (dict): Diccionario que representa a un héroe.
        key (str): Clave que representa el dato que se desea obtener.

    Returns:
        str: Cadena formateada con el nombre y el dato del héroe.
    """
    nombre = heroe.get("nombre", "")
    dato = heroe.get(key, "")
    return f"{key.capitalize()}: {dato}"

# ----------------------------------------------------------------------------------------------------------------------------------
#3

def stark_imprimir_nombres_alturas(heroes: list) -> None:
    """
    Imprime el nombre y la altura de cada superhéroe en la lista de héroes.

    Recibe una lista de diccionarios que representan a los superhéroes con sus respectivos atributos.
    Imprime por consola el nombre y la altura de cada superhéroe en el siguiente formato:
    'Nombre: {nombre_del_heroe} | Altura: {altura_del_heroe}'.

    Si la lista de héroes está vacía, no se imprime nada.

    Args:
        heroes (list): Una lista de diccionarios que representan a los superhéroes.

    Returns:
        None: Esta función no retorna ningún valor.
    """
    if not heroes:
        return -1

    for heroe in heroes:
        mensaje = obtener_nombre_y_dato(heroe, "altura")
        print(mensaje)

# ----------------------------------------------------------------------------------------------------------------------------------
#4.1

def calcular_max(heroes: list, key: str) -> dict:
    """
    Calcula el héroe con el valor máximo para una clave específica.

    Recibe una lista de héroes representados como diccionarios y una clave para
    determinar qué dato se utilizará para encontrar el valor máximo. Retorna el héroe
    que tiene el valor más alto para la clave especificada.

    Args:
        heroes (list): Una lista de diccionarios que representan a los héroes con sus respectivos atributos.
        key (str): La clave que se utilizará para encontrar el valor máximo.

    Returns:
        dict: El héroe con el valor máximo para la clave especificada.

    """
    return max(heroes, key=lambda heroe: heroe.get(key, float('-inf')))

#4.2
def calcular_min(heroes: list, key: str) -> dict:
    """
    Encuentra el héroe con el valor mínimo en la lista de héroes, utilizando una clave específica.

    Args:
        heroes (list): Lista de diccionarios que representan a los héroes.
        key (str): Clave que representa el dato utilizado para determinar el valor mínimo.

    Returns:
        dict: Diccionario que representa al héroe con el valor mínimo en la clave especificada.

    """
    return min(heroes, key=lambda heroe: heroe.get(key, float('inf')))

#4.3
def calcular_max_min_dato(heroes: list, tipo_calculo: str, key: str) -> dict:
    """
    Calcula el héroe con el valor máximo o mínimo para el dato especificado.

    Args:
        heroes (list): Lista de héroes.
        tipo_calculo (str): Tipo de cálculo a realizar. Puede ser 'max' o 'min'.
        key (str): Clave del dato a calcular.

    Returns:
        dict: Diccionario con el nombre del héroe y el valor del dato calculado.

    """
    if tipo_calculo == 'max':
        heroe = max(heroes, key=lambda h: h.get(key, float('-inf')))
    elif tipo_calculo == 'min':
        heroe = min(heroes, key=lambda h: h.get(key, float('inf')))
    else:
        print("Error: Tipo de cálculo inválido")
        return None

    nombre_heroe = heroe.get('nombre', '')
    valor_dato = heroe.get(key, '')
    
    return {'nombre': nombre_heroe, key: valor_dato}

# heroe_max_altura = calcular_max_min_dato(lista_personajes_normalizada, 'max', 'altura')
# print(f"Héroe con la altura máxima: {heroe_max_altura['nombre']} | Altura: {heroe_max_altura['altura']}")

#4.4
def stark_calcular_imprimir_heroe(heroes: list, tipo_calculo: str, dato: str) -> int:
    """
    Obtiene el héroe que cumple con la condición especificada, imprime su nombre y el valor calculado.

    Requiere de las funciones obtener_nombre_y_dato() y calcular_max_min_dato() previamente definidas.

    Args:
        heroes (list): Lista de diccionarios que representan a los héroes.
        tipo_calculo (str): Tipo de cálculo a realizar, puede ser 'max' o 'min'.
        dato (str): Nombre del dato a calcular (altura, peso o fuerza).

    Returns:
        int: Retorna -1 si la lista de héroes está vacía o si el dato no es válido, de lo contrario retorna 0.
    """
    if not heroes:
        print("Error: Lista de héroes vacía")
        return -1

    if tipo_calculo not in ['max', 'min']:
        print("Error: Tipo de cálculo no válido. Debe ser 'max' o 'min'.")
        return -1

    if dato not in ['altura', 'peso', 'fuerza']:
        print("Error: Dato no válido. Debe ser 'altura', 'peso' o 'fuerza'.")
        return -1

    heroe_calculado = calcular_max_min_dato(heroes, tipo_calculo, dato)
    nombre = obtener_nombre(heroe_calculado)
    mensaje = obtener_nombre_y_dato(heroe_calculado, dato)
    imprimir_dato(f"{tipo_calculo.capitalize()} {dato}: {nombre} | {mensaje}")

    return 0

# stark_calcular_imprimir_heroe(lista_personajes_normalizada, 'max', 'altura')

# ----------------------------------------------------------------------------------------------------------------------------------
#5.1

def sumar_dato_heroe(heroes: list, dato: str) -> float:
    """
    Suma el valor de un dato específico en todos los héroes de la lista.

    Args:
        heroes (list): Lista de diccionarios que representan a los héroes.
        dato (str): Nombre del dato a sumar.

    Returns:
        float: La suma total del dato en todos los héroes. 
        Si la lista de héroes está vacía o si algún héroe no tiene el dato especificado, retorna 0.
    """
    if not heroes:
        print("Error: Lista de héroes vacía")
        return 0

    suma_total = 0.0

    for heroe in heroes:
        if type(heroe) == dict and heroe and dato in heroe:
            valor = heroe.get(dato)
            if type(valor) in (int, float):
                suma_total += valor

    return suma_total

# resultado = sumar_dato_heroe(lista_personajes_normalizada, 'altura')
# print("Suma de alturas:", resultado)

#5.2
def dividir(dividendo: float, divisor: float) -> float:
    """
    Realiza la división entre el dividendo y el divisor.

    Args:
        dividendo (float): El número que será dividido.
        divisor (float): El número por el cual se dividirá el dividendo.

    Returns:
        float: El resultado de la división si el divisor no es cero, de lo contrario retorna 0.
    """
    if divisor == 0:
        return 0
    
    return dividendo / divisor

#5.3
def calcular_promedio(heroes: list, key: str) -> float:
    """
    Calcula el promedio del dato especificado de los héroes en la lista.

    Args:
        heroes (list): Lista de héroes.
        key (str): Clave que representa el dato a promediar.

    Returns:
        float: El promedio del dato de los héroes, o 0 si la lista está vacía.
    """
    if not heroes:
        return 0

    suma = sumar_dato_heroe(heroes, key)
    cantidad = len(heroes)

    if cantidad == 0:
        return 0

    promedio = dividir(suma, cantidad)
    return promedio

#5.4
def stark_calcular_imprimir_promedio_altura(heroes: list) -> int:
    """
    Calcula y muestra el promedio de altura de los héroes en la lista.

    Args:
        heroes (list): Lista de héroes.

    Returns:
        int: Retorna -1 si la lista de héroes está vacía, de lo contrario retorna 0.
    """
    if not heroes:
        print("Error: Lista de héroes vacía")
        return -1

    promedio_altura = calcular_promedio(heroes, 'altura')
    mensaje = f"Promedio de altura: {promedio_altura:.2f}"
    imprimir_dato(mensaje)

    return 0

# stark_calcular_imprimir_promedio_altura(lista_personajes_normalizada)

# ----------------------------------------------------------------------------------------------------------------------------------
#6.1

def imprimir_menu(opciones: list) -> None:
    """
    Imprime el menú de opciones por pantalla.

    Args:
        opciones (list): Lista de opciones a imprimir. Cada opción debe ser un string.

    Returns:
        None
    """
    imprimir_dato("----- MENÚ -----")
    for opcion in opciones:
        imprimir_dato(opcion)

#6.2
def validar_entero(numero_str: str) -> bool:
    """
    Verifica si un string está conformado únicamente por dígitos.

    Args:
        numero_str (str): El string de número a verificar.

    Returns:
        bool: True si el string está conformado únicamente por dígitos, False en caso contrario.
    """
    return numero_str.isdigit()

#6.3
def stark_menu_principal() -> int:
    """
    Muestra el menú principal y obtiene la opción seleccionada por el usuario.

    Returns:
        int: La opción seleccionada por el usuario.
    """
    opciones = [
        "1. Imprimir nombres de héroes",
        "2. Imprimir altura max",
        "3. Imprimir fuerza min",
        "4. Imprimir peso max",
        "5. Imprimir promedio de altura",
        "6. Salir"
    ]

    imprimir_menu(opciones)
    opcion = input("Seleccione una opción: ")
    return opcion



# ----------------------------------------------------------------------------------------------------------------------------------
#7

def stark_marvel_app(heroes: list) -> None:
    """
    Función principal que ejecuta la aplicación de Marvel.

    Args:
        heroes (list): Lista de héroes.

    Returns:
        None
    """
    while True:
        opcion = stark_menu_principal()
        os.system('cls')

        if opcion == '1':
            stark_imprimir_nombres_heroes(heroes)
        elif opcion == '2':
            stark_calcular_imprimir_heroe(heroes, 'max', 'altura')
        elif opcion == '3':
            stark_calcular_imprimir_heroe(heroes, 'min', 'fuerza')
        elif opcion == '4':
            stark_calcular_imprimir_heroe(heroes, 'max', 'peso')
        elif opcion == '5':
            stark_calcular_imprimir_promedio_altura(heroes)
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción incorrecta. Por favor, ingrese un número válido.")
        os.system('pause')

# stark_marvel_app(lista_personajes_normalizada)


