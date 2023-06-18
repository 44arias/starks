import re
import json
from stark_1 import menu_dos
from stark_biblioteca import imprimir_dato, calcular_min, calcular_max, dividir

# ----------------------------------------------------------------------------------------------------------------------------------
# Functions 05
#1.1

def imprimir_menu_desafio_5():
    
    return imprimir_dato(menu_dos())

#1.2    
def stark_menu_principal_desafio_5():
    
    imprimir_menu_desafio_5()
    opcion = input("Ingrese la letra de una de las opciones: ")
    if re.match(r'^[A-Za-z]$', opcion):
        return opcion.upper()
    else:
        return -1

#1.3
def stark_maervel_app_5(lista_heroes: list):
    pass

#1.4
def leer_archivo(nombre_archivo: str) -> list:
    
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        datos = json.loads(contenido)
        lista_heroes = datos['heroes']
        return lista_heroes
    
nombre_archivo = "data_stark.json"
heroes = leer_archivo(nombre_archivo)

# print(heroes)

#1.5
def guardar_archivo(nombre_archivo_a_guardar: str, contenido: str) -> bool:
    
    try: 
        with open(nombre_archivo_a_guardar, "w+") as archivo:
            archivo.write(contenido)
        print(f"Se creó el archivo: {nombre_archivo_a_guardar}")
        return True
    except Exception:
        print(f"Error al crear el archivo: {nombre_archivo_a_guardar}")
        return False
    
#1.6
def capitalizar_palabras(texto: str) -> str:
    
    palabras = texto.split()
    palabras_capitalizadas = []
    for palabra in palabras:
        palabras_capitalizadas.append(palabra.capitalize())
    texto_capitalizado = " ".join(palabras_capitalizadas)
    
    return texto_capitalizado

#1.7
def obtener_nombre_capitalizado(heroe: dict, x = True) -> str:
    
    nombre_capitalizado = capitalizar_palabras(heroe['nombre'])
    
    if x:
        nombre_formateado = f"Nombre: {nombre_capitalizado}"
        return nombre_formateado
    else:
        return nombre_capitalizado

# print(obtener_nombre_capitalizado(heroes[0]))

#1.8
def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    
    keys = ["nombre", "identidad", "empresa", "altura", "peso", "genero", "color_ojos", "color_pelo", "fuerza", "inteligencia"]
    
    if key not in keys:
        return "Error, ingrese una key valida"
    else:
        key_capitalizada = capitalizar_palabras(key)
        
    nombre_capitalizado = obtener_nombre_capitalizado(heroe, False)
    
    output = f"Nombre: {nombre_capitalizado} | {key_capitalizada}: {heroe[key]}"
    
    return output

# print(obtener_nombre_y_dato(heroes[0], 'fuerza'))

# ----------------------------------------------------------------------------------------------------------------------------------
#2.1

def es_genero(heroe: dict, genero: str) -> bool:
    
    generos_validos = ['M', 'F', 'NB']
    
    if genero not in generos_validos:
        print(f"Error, el género '{genero}' no es un dato válido")
        return False
    else:
        if heroe['genero'] == genero:
            return True
        else:
            return False
    
    
#2.2
def stark_guardar_heroe_genero(lista_heroes: list, genero_a_evaluar: str) -> bool:
    generos_validos = ['M', 'F', 'NB']
    
    if genero_a_evaluar not in generos_validos:
        print(f"Error, el género '{genero_a_evaluar}' no es válido")
        return False
    
    heroes_coincidentes = [heroe for heroe in lista_heroes if es_genero(heroe, genero_a_evaluar)]
    
    if not heroes_coincidentes:
        print(f"No hay héroes o heroínas con el género '{genero_a_evaluar}'")
        return False
    
    nombre_archivo = f"heroes_{genero_a_evaluar}.csv"
    contenido_archivo = ', '.join([obtener_nombre_capitalizado(heroe) for heroe in heroes_coincidentes])
    
    if guardar_archivo(nombre_archivo, contenido_archivo):
        return True
    else:
        return False

# ----------------------------------------------------------------------------------------------------------------------------------
#3.1

def calcular_min_genero(heroes: list, key: str, genero: str) -> dict:
    
    heroes_genero = []
    for heroe in heroes:
        if heroe.get('genero') == genero:
            heroes_genero.append(heroe)
    return calcular_min(heroes_genero, key)

#3.2
def calcular_max_genero(heroes: list, key: str, genero: str) -> dict:
    
    heroes_genero = []
    for heroe in heroes:
        if heroe.get('genero') == genero:
            heroes_genero.append(heroe)
    return calcular_max(heroes_genero, key)

#3.3
def calcular_max_min_dato_genero(heroes: list, tipo_calculo: str, key: str, genero: str) -> dict:
    
    if tipo_calculo == 'max':
        heroe = calcular_max_genero(heroes, key, genero)
    elif tipo_calculo == 'min':
        heroe = calcular_min_genero(heroes, key, genero)
    else:
        print("Error: Tipo de cálculo inválido")
        return None

    nombre_heroe = heroe.get('nombre', '')
    valor_dato = heroe.get(key, '')

    return {'nombre': nombre_heroe, key: valor_dato}

#3.4
def stark_calcular_imprimir_guardar_heroe_genero(heroes: list, tipo_calculo: str, key: str, genero: str) -> bool:

    if tipo_calculo not in ['max', 'min']:
        print("Error: Tipo de cálculo inválido. Debe ser 'max' o 'min'.")
        return False

    heroes_genero = [heroe for heroe in heroes if heroe.get('genero') == genero]
    if not heroes_genero:
        print(f"No se encontraron héroes o heroínas del género '{genero}'.")
        return False

    heroe_calculado = calcular_max_min_dato_genero(heroes_genero, tipo_calculo, key, genero)
    nombre_heroe = heroe_calculado.get('nombre', '')
    valor_dato = heroe_calculado.get(key, '')

    mensaje = f"{tipo_calculo.capitalize()} {key.capitalize()}: Nombre: {nombre_heroe} | {key.capitalize()}: {valor_dato}"
    imprimir_dato(mensaje)

    nombre_archivo = f"heroes_{tipo_calculo}_{key}_{genero}.csv"
    contenido = f"{nombre_heroe},{valor_dato}"
    return guardar_archivo(nombre_archivo, contenido)

# ----------------------------------------------------------------------------------------------------------------------------------
#4.1
def sumar_dato_heroe_genero(heroes: list, dato: str, genero: str) -> float:

    if not heroes:
        print("Error: Lista de héroes vacía")
        return -1

    suma_total = 0.0

    for heroe in heroes:
        if isinstance(heroe, dict) and heroe and heroe.get('genero') == genero and dato in heroe:
            valor = heroe.get(dato)
            if isinstance(valor, (int, float)):
                suma_total += valor

    return suma_total

#4.2
def cantidad_heroes_genero(heroes: list, genero: str) -> int:

    count = 0

    for heroe in heroes:
        if isinstance(heroe, dict) and heroe.get('genero') == genero:
            count += 1

    return count

#4.3
def calcular_promedio_genero(heroes: list, key: str, genero: str) -> float:

    cantidad = cantidad_heroes_genero(heroes, genero)

    if cantidad == 0:
        return 0

    suma = sumar_dato_heroe_genero(heroes, key, genero)
    promedio = dividir(suma, cantidad)

    return promedio

#4.4
def stark_calcular_imprimir_guardar_promedio_altura_genero(heroes: list, genero: str) -> bool:

    if not heroes:
        print("Error: Lista de héroes vacía")
        return False

    promedio_altura = calcular_promedio_genero(heroes, 'altura', genero)
    mensaje = f"Altura promedio género {genero}: {promedio_altura:.2f}"
    imprimir_dato(mensaje)

    nombre_archivo = f"heroes_promedio_altura_{genero}.csv"
    contenido_archivo = mensaje
    resultado_guardado = guardar_archivo(nombre_archivo, contenido_archivo)

    return resultado_guardado

# ----------------------------------------------------------------------------------------------------------------------------------
#5.1
def calcular_cantidad_tipo(heroes: list, tipo_dato: str) -> dict:

    if not heroes:
        return {"Error": "La lista se encuentra vacía"}

    valores = {}
    for heroe in heroes:
        dato = heroe.get(tipo_dato)
        if dato:
            valor_capitalizado = capitalizar_palabras(dato)
            valores[valor_capitalizado] = valores.get(valor_capitalizado, 0) + 1

    return valores

#5.2
def guardar_cantidad_heroes_tipo(cantidad_heroes: dict, tipo_dato: str) -> bool:

    mensaje = []
    for variedad, cantidad in cantidad_heroes.items():
        mensaje.append(f"Característica: {tipo_dato} {variedad} - Cantidad de héroes: {cantidad}")

    contenido = "\n".join(mensaje)
    nombre_archivo = f"heroes_cantidad_{tipo_dato}.csv"

    return guardar_archivo(nombre_archivo, contenido)

#5.3
def stark_calcular_cantidad_por_tipo(heroes: list, tipo_dato: str) -> bool:

    cantidad_heroes = calcular_cantidad_tipo(heroes, tipo_dato)
    return guardar_cantidad_heroes_tipo(cantidad_heroes, tipo_dato)

# ----------------------------------------------------------------------------------------------------------------------------------
#6.1
def obtener_lista_de_tipos(heroes: list, tipo_dato: str) -> set:

    variedades = set()

    for heroe in heroes:
        valor = heroe.get(tipo_dato, '')
        if not valor or valor.strip() == '':
            valor = 'N/A'
        valor = capitalizar_palabras(valor)
        variedades.add(valor)

    return variedades

#6.2
def normalizar_dato(dato: str, valor_default: str) -> str:

    if not dato or dato.strip() == '':
        return valor_default

    return dato

#6.3
def normalizar_heroe(heroe: dict, key: str) -> dict:

    nombre_heroe = capitalizar_palabras(heroe.get('nombre', ''))
    valor_key = normalizar_dato(heroe.get(key, ''), 'N/A')

    heroe_normalizado = heroe.copy()
    heroe_normalizado['nombre'] = nombre_heroe
    heroe_normalizado[key] = capitalizar_palabras(valor_key)

    return heroe_normalizado

#6.4
def obtener_heroes_por_tipo(heroes: list, tipos: set, tipo_dato: str) -> dict:

    heroes_por_tipo = {}

    for tipo in tipos:
        heroes_por_tipo[tipo] = []

    for heroe in heroes:
        valor_tipo = normalizar_dato(heroe.get(tipo_dato, ''), 'N/A')
        for tipo in tipos:
            if valor_tipo == tipo:
                heroes_por_tipo[tipo].append(heroe['nombre'])

    return heroes_por_tipo

#6.5
def guardar_heroes_por_tipo(heroes_por_tipo: dict, tipo_dato: str) -> bool:

    mensaje = ""
    for tipo, heroes in heroes_por_tipo.items():
        mensaje += f"{tipo} {tipo_dato.capitalize()}: "
        mensaje += " | ".join(heroes)
        mensaje += "\n"

    nombre_archivo = f"heroes_segun_{tipo_dato}.csv"
    guardar_archivo(nombre_archivo, mensaje)

    return True

#6.6
def stark_listar_heroes_por_dato(heroes: list, tipo_dato: str) -> bool:

    tipos = obtener_lista_de_tipos(heroes, tipo_dato)
    heroes_por_tipo = obtener_heroes_por_tipo(heroes, tipos, tipo_dato)
    return guardar_heroes_por_tipo(heroes_por_tipo, tipo_dato)













