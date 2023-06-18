import re
import json
import os

# ----------------------------------------------------------------------------------------------------------------------------------
# Functions 02

path = r"C:\Users\4\Desktop\starks\data_stark.json"

def cargar_datos(path, lista):
    with open(path, "r+", encoding="utf-8") as file:
        lista = json.load(file)
        lista = lista['heroes']
        
        for i in lista:
            i['altura'] = round(float(i['altura']), 2)
            i['peso'] = round(float(i['peso']), 2)
            i['fuerza'] = round(float(i['fuerza']), 2)
        return lista
    
lista = cargar_datos(path, lista=list)

#1.1

def extraer_iniciales(nombre_heroe: str) -> str:
    """
    Extrae las iniciales del nombre de un personaje y las devuelve como un nuevo string.

    Args:
        nombre_heroe (str): El nombre del personaje.

    Returns:
        str: Las iniciales del nombre del personaje seguidas por un punto (.).
             En caso de que el nombre del personaje contenga el artículo 'the', se omite de las iniciales.
             Si el nombre contiene un guión '-', se reemplaza por un espacio en blanco en las iniciales.

    Raises:
        None
    """
    if not nombre_heroe:
        return 'N/A'
    
    nombre_heroe = nombre_heroe.replace('-', ' ')
    palabras = nombre_heroe.split()
    iniciales = ''
    for palabra in palabras:
        if palabra.lower() != 'the':
            iniciales += palabra[0].upper() + '.'
            
    return iniciales

#1.2
def definir_iniciales_nombre(heroe: dict) -> bool:
    """
    Agrega la clave 'iniciales' al diccionario 'heroe', con el valor obtenido de llamar a la función 'extraer_iniciales'.

    Args:
        heroe (dict): Un diccionario con los datos del personaje.

    Returns:
        bool: True si se agrega la clave 'iniciales' correctamente, False en caso contrario.
    """
    if not isinstance(heroe, dict):
    
        return False
    
    if 'nombre' not in heroe:
        return False
    
    iniciales = extraer_iniciales(heroe['nombre'])
    heroe['iniciales'] = iniciales
    
    return True

#1.3
def agregar_iniciales_nombre(lista_heroes: list) -> bool:
    """
    Agrega las iniciales al nombre de cada héroe en una lista de personajes.

    Args:
        lista_heroes (list): Una lista de diccionarios con los datos de los personajes.

    Returns:
        bool: True si se agregaron las iniciales correctamente a todos los héroes, False en caso contrario.
    """
    if not isinstance(lista_heroes, list):
        print("El origen de datos no contiene el formato correcto")
        return False

    if len(lista_heroes) == 0:
        print("La lista no contiene elementos")
        return False
    
    for heroe in lista_heroes:
        if not definir_iniciales_nombre(heroe):
            print("El origen de datos no contiene el formato correcto")
            return False
        else:
            definir_iniciales_nombre(heroe)
            
    return True


#1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes: list) -> None:
    """
    Agrega las iniciales a los nombres de los personajes en una lista y los imprime.

    Args:
        lista_heroes (list): Una lista de diccionarios con los datos de los personajes.

    Returns:
        None
    """
    if not isinstance(lista_heroes, list):
        print("El origen de datos no contiene el formato correcto")
        return False
    
    if len(lista_heroes) == 0:
        print("La lista no contiene elementos")
        return False
    
    if not agregar_iniciales_nombre(lista_heroes):
        return False
    
    for heroe in lista_heroes:
        nombre = heroe.get('nombre', '')
        iniciales = heroe.get('iniciales', '')
        print(f"* {nombre} ({iniciales})")
        
# stark_imprimir_nombres_con_iniciales(lista)

# ----------------------------------------------------------------------------------------------------------------------------------
#2.1

def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    """
    Genera un código para un héroe a partir de su identificador y género.

    Args:
        id_heroe (int): El identificador del héroe.
        genero_heroe (str): El género del héroe ('M', 'F' o 'NB').

    Returns:
        str: El código generado en el formato "GENERO-000...000ID", o 'N/A' si no se pasan las validaciones.
    """
    if not isinstance(id_heroe, int) or not isinstance (genero_heroe, str):
        return 'N/A'
    
    if genero_heroe not in ['M', 'F', 'NB']:
        return 'N/A'
    
    codigo = f"{genero_heroe}-" + str(id_heroe).zfill(8) 
    if len(codigo) > 10:
        return 'N/A'
    
    return codigo

#2.2    
def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    """
    Agrega un código de héroe al diccionario del personaje.

    Args:
        heroe (dict): Un diccionario con los datos del personaje.
        id_heroe (int): El identificador del héroe.

    Returns:
        bool: True si se agregó el código correctamente, False si se encontró un error.
    """
    if not heroe or not isinstance(heroe, dict):
        return False
    
    codigo_heroe = generar_codigo_heroe(id_heroe, heroe.get('genero', ''))
    if codigo_heroe == 'N/A' or len(codigo_heroe) != 10:
        return False
    
    heroe['codigo_heroe'] = codigo_heroe
    return True

#2.3
def stark_generar_codigos_heroes(lista_heroes, x = True) -> None:
    """
    Asigna códigos a los héroes de una lista de personajes y muestra información relacionada.

    Args:
        lista_heroes (list): Lista de diccionarios que representan a los personajes.

    Returns:
        None
    """
    if len(lista_heroes) == 0:
        print('El origen de datos no contiene el formato correcto')
        return
    
    for hero in lista_heroes:
        if not isinstance(hero, dict) or 'genero' not in hero:
            print('El origen de datos no contiene el formato correcto')
            return
    
    for i, heroe in enumerate(lista_heroes, 1):
        agregar_codigo_heroe(heroe, i)  
            
    cantidad_codigos = len(lista_heroes)
    
    if x:
        print(f"Se asignaron {cantidad_codigos} códigos")
    
# stark_generar_codigos_heroes(lista)

# ----------------------------------------------------------------------------------------------------------------------------------
#3.1
def sanitizar_entero(numero_str: str) -> int:
    """
    Sanitiza una cadena de texto representando un número entero.

    Args:
        numero_str (str): Cadena de texto a sanitizar.

    Returns:
        int: Número entero sanitizado, o un código de error.

    Error Codes:
        -1: Error desconocido al sanitizar el número.
        -2: Número negativo no válido.
        -3: Cadena de texto vacía o no válida.

    """
    if isinstance(numero_str, str):
        numero_str = numero_str.replace(" ", "")
        numero_str = numero_str.replace(",", ".")
    
    try:
        numero = int(numero_str)
        
        if numero < 0:
            return -2
        
        return numero
    
    except Exception:
        if numero_str == "" or not isinstance(numero_str, str):
            return -3
        else:
            return -1

#3.2

def sanitizar_flotante(numero_str: str) -> float:
    """
    Sanitiza una cadena de texto representando un número de punto flotante.

    Args:
        numero_str (str): Cadena de texto a sanitizar.

    Returns:
        float: Número de punto flotante sanitizado, o un código de error.

    Error Codes:
        -1: Error desconocido al sanitizar el número.
        -2: Número negativo no válido.
        -3: Cadena de texto vacía o no válida.

    """
    if isinstance(numero_str, str):
        numero_str = numero_str.replace(" ", "")
        numero_str = numero_str.replace(",", ".")
    
    try:
        numero = float(numero_str)
        
        if numero < 0:
            return -2
        
        return numero
    
    except Exception:
        if numero_str == "" or not isinstance(numero_str, str):
            return -3
        else:
            return -1

    
#3.3
def sanitizar_string(valor_str = None, valor_por_defecto = "-", reemplazar_barrita = True):
    """
    Sanitiza una cadena de texto según las opciones especificadas.

    Args:
        valor_str (str, optional): Cadena de texto a sanitizar. Por defecto es None.
        valor_por_defecto (str, optional): Valor a retornar si la cadena de texto es vacía o contiene solo espacios en blanco. Por defecto es "-".
        reemplazar_barrita (bool, optional): Indica si se debe reemplazar la barra ("/") por un espacio en blanco. Por defecto es True.

    Returns:
        str: Cadena de texto sanitizada.

    """
    if not valor_str or re.match(r'^\s*$', valor_str):
        return valor_por_defecto  
    
    valor_str = valor_str.lower().strip()  
    
    if reemplazar_barrita:
        valor_str = valor_str.replace("/", " ") 
    
    return valor_str  


#3.4
def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str):
    """
    Sanitiza un dato específico de un diccionario de héroes, según el tipo de dato especificado.

    Args:
        heroe (dict): Diccionario que contiene información del héroe.
        clave (str): Clave del dato a sanitizar.
        tipo_dato (str): Tipo de dato al que se debe sanitizar el valor.

    Returns:
        str: Mensaje indicando que el dato fue sanitizado.

    Raises:
        ValueError: Si el tipo de dato no es reconocido.
        KeyError: Si la clave especificada no existe en el diccionario.

    """
    clave = sanitizar_string(clave)
    tipo_dato = sanitizar_string(tipo_dato)
    
    tipos_validos = ["flotante", "entero", "string"] 
    claves_validas = ["nombre", "identidad", "empresa", "genero", "color_pelo", "color_ojos", "inteligencia", "altura", "peso", "fuerza"]  
    
    if tipo_dato not in tipos_validos:
        raise ValueError("Tipo de dato no reconocido")  
    
    if clave not in claves_validas:
        raise KeyError("La clave especificada no existe") 
    
    valor = heroe[clave]
    
    if tipo_dato == "string":
        sanitizar_string(valor)  
    elif tipo_dato == "flotante":
        sanitizar_flotante(valor)  
    elif tipo_dato == "entero":
        sanitizar_entero(valor)  
    
    return f"{clave} fue sanitizada/o" 


#3.5
def stark_normalizar_datos(lista: list):
    """
    Normaliza los datos de una lista de héroes Stark, aplicando la sanitización correspondiente a cada atributo.

    Args:
        lista (list): Lista de diccionarios que contienen los datos de los héroes Stark.

    Returns:
        None

    """
    if not lista:
        print("Error, lista vacía")
        return None

    for i in lista:
        sanitizar_dato(i, "fuerza", "entero")
        sanitizar_dato(i, "peso", "flotante")
        sanitizar_dato(i, "altura", "flotante")
        sanitizar_dato(i, "color_ojos", "string")
        sanitizar_dato(i, "color_pelo", "string")
        sanitizar_dato(i, "inteligencia", "string")

    print("Datos sanitizados")

# ----------------------------------------------------------------------------------------------------------------------------------
#4.1

def generar_indice_nombres(lista_heroes: list) -> list:
    """
    Genera una lista con las palabras que componen los nombres de los personajes.

    Parámetros:
        lista_heroes (list): La lista de personajes.

    Retorna:
        list: La lista de palabras que componen los nombres.

    """
    if not lista_heroes:
        print("El origen de datos no contiene el formato correcto")
        return []
    
    for heroe in lista_heroes:
        if not isinstance(heroe, dict) or 'nombre' not in heroe:
            print("El origen de datos no contiene el formato correcto")
            return 
        
    indice_nombres = []
    
    for heroe in lista_heroes:
        nombre = heroe['nombre']
        palabras = nombre.split()
        indice_nombres.extend(palabras)
        
    return indice_nombres

#4.2
def stark_imprimir_indice_nombre(lista_heroes: list):
    """
    Imprime por pantalla el índice de nombres generado a partir de la lista de personajes.

    Parámetros:
        lista_heroes (list): La lista de personajes.

    """
    indice_nombres = generar_indice_nombres(lista_heroes)
    if indice_nombres:
        indice_formateado = '-'.join(indice_nombres)
        print(indice_formateado)
        
# ----------------------------------------------------------------------------------------------------------------------------------
#5.1
        
def convertir_cm_a_mtrs(valor_cm: float) -> float:
    """
    Convierte una medida en centímetros a metros.

    Parámetros:
        valor_cm (float): El valor en centímetros a convertir.

    Retorna:
        float: El valor convertido a metros, o -1 si el número no es un flotante positivo.

    """
    if isinstance(valor_cm, float) and valor_cm > 0:
        return valor_cm / 100
    else:
        return -1
    
#5.2
def generar_separador(patron: str, largo: int, imprimir = True):
    """
    Genera un separador utilizando un patrón y un largo específico.

    Parámetros:
        patron (str): Un carácter utilizado como patrón para el separador.
        largo (int): La cantidad de caracteres que ocupará el separador.
        imprimir (bool, opcional): Indica si se imprimirá el separador por pantalla. Por defecto es True.

    Retorna:
        str: El separador generado, o 'N/A' si las validaciones no se cumplen.

    """
    if len(patron) >= 1 and len(patron) <= 2 and isinstance(largo, int) and largo >= 1 and largo <= 235:
        separador = patron * largo
        if imprimir:
            print(separador)
        return separador
    else:
        return 'N/A'
    
#5.3
def generar_encabezado(titulo: str) -> str:
    """
    Genera un encabezado con el título de una sección de la ficha.

    Parámetros:
        titulo (str): El título de la sección.

    Retorna:
        str: El encabezado generado.

    """
    separador = generar_separador('*', 80, False)
    titulo_mayusculas = titulo.upper()
    encabezado = f"{separador}\n{titulo_mayusculas}\n{separador}"
    
    return encabezado

#5.4
def imprimir_ficha_heroe(heroe: dict) -> None:
    
    separador_1 = generar_encabezado('Principal')
    separador_2 = generar_encabezado('Fisico')
    separador_3 = generar_encabezado('Señas Particulares')
    
    stark_generar_codigos_heroes(lista, False)
    agregar_iniciales_nombre(lista)

    string = f"""
    {separador_1}
    NOMBRE HEROE:           {heroe["nombre"]}({heroe["iniciales"]})
    IDENTIDAD SECRETA:      {heroe["identidad"]}
    CONSULTORA:             {heroe["empresa"]}
    CODIGO DE HEORE:        {heroe["codigo_heroe"]}
    {separador_2}
    ALTURA:                 {(heroe['altura'])}cms
    PESO:                   {heroe["peso"]} Kg.
    FUERZA                  {heroe["fuerza"]} N
    {separador_3}
    COLOR DE OJOS:          {heroe["color_ojos"]}
    COLOR DE PELO:          {heroe["color_pelo"]}
    {generar_separador("-", 50, True)}"""
    print(string)
    
#5.5
def stark_navegar_fichas(lista:list):
    contador = 0
    eleccion = "s"
    while True:
        os.system('cls')
        imprimir_ficha_heroe(lista[contador])
        eleccion = input("Escriba 1, para avanzar la lista hacia la izquierda, 2 a la derecha o S para salir: ").lower()
        while eleccion != "1" and eleccion != "2" and eleccion != "s":
            eleccion = input("Error, ingrese una opcion valida: ")
        if eleccion == "1":
            contador -= 1
        elif eleccion == "2":
            contador += 1
        else:
            break
        if contador == 23 or contador == -23:
            contador = 0

# ----------------------------------------------------------------------------------------------------------------------------------            
#6.1
def imprimir_menu():
    print("""
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir

    ____________________________________________________________
    """)
    
#6.2
def stark_menu_principal():
    imprimir_menu()
    opcion = input("Ingrese una opcion... ").upper()
    return opcion

#6.3
def stark_marvel_app_3(lista_heroes: list):
    while True:
        opcion = stark_menu_principal()
        os.system('cls')
        
        if opcion == "1":
            for personaje in lista:
                nombre = personaje["nombre"]
                iniciales = extraer_iniciales(nombre)
                print(f"Iniciales de '{nombre}': {iniciales}")
        elif opcion == "2":
            stark_generar_codigos_heroes(lista_heroes)
        elif opcion == "3":
            stark_normalizar_datos(lista_heroes)
        elif opcion == "4":
            stark_imprimir_indice_nombre(lista_heroes)
        elif opcion == "5":
            stark_navegar_fichas(lista_heroes)
        elif opcion == "S":
            print("Saliendo del programa...")
            break
        else:
            print("Opción incorrecta. Por favor, ingrese una opción válida.")
        os.system('pause')
            
stark_marvel_app_3(lista)
        
    