# ----------------------------------------------------------------------------------------------------------------------------------
# Menu

from data_stark import *
from stark_0 import *
from stark_1 import *
import os

lista = lista_personajes

flag_1 = False

while True:
    opcion = menu()
    os.system('cls')
    if opcion == '1':
        flag_1 = True
        mostrar_nombres(lista)
    elif flag_1:
        if opcion == '2':
            mostrar_nombres_y_alturas(lista)
        elif opcion == '3':
            mostrar_superheroe_mas_alto(lista)
        elif opcion == '4':
            mostrar_superheroe_mas_bajo(lista)
        elif opcion == '5':
            mostrar_altura_promedio(lista)
        elif opcion == '6':
            mostrar_superheroes_pesados_livianos(lista)
        elif opcion == '7':
            os.system('cls')
            while True:
                os.system('cls')
                opcion = menu_dos()
                if opcion == 'A':
                    recorrer_superheroes_genero(lista, 'M')
                elif opcion == 'B':
                    recorrer_superheroes_genero(lista, 'F')
                elif opcion == 'C':
                    superheroe_mas_alto_genero(lista, 'M')
                elif opcion == 'D':
                    superheroe_mas_alto_genero(lista, 'F')
                elif opcion == 'E':
                    superheroe_mas_bajo_genero_m = encontrar_superheroe_mas_bajo_genero(lista, 'M')
                    print(f"Superhéroe más bajo de género M: {obtener_nombre_superheroe(superheroe_mas_bajo_genero_m)}")
                elif opcion == 'F':
                    superheroe_mas_bajo_genero_f = encontrar_superheroe_mas_bajo_genero(lista, 'F')
                    print(f"Superhéroe más bajo de género F: {obtener_nombre_superheroe(superheroe_mas_bajo_genero_f)}")
                elif opcion == 'G':
                    altura_promedio_genero_m = calcular_altura_promedio_genero(lista, 'M')
                    print(f"Altura promedio de los superhéroes de género M: {altura_promedio_genero_m}")
                elif opcion == 'H':
                    altura_promedio_genero_f = calcular_altura_promedio_genero(lista, 'F')
                    print(f"Altura promedio de los superhéroes de género F: {altura_promedio_genero_f}")
                elif opcion == 'I':
                    superheroe_mas_alto_genero_m = encontrar_superheroe_mas_alto_genero(lista, 'M')
                    superheroe_mas_alto_genero_f = encontrar_superheroe_mas_alto_genero(lista, 'F')
                    superheroe_mas_bajo_genero_m = encontrar_superheroe_mas_bajo_genero(lista, 'M')
                    superheroe_mas_bajo_genero_f = encontrar_superheroe_mas_bajo_genero(lista, 'F')
                    print(f"Nombre del superhéroe más alto de género M: {obtener_nombre_superheroe(superheroe_mas_alto_genero_m)}")
                    print(f"Nombre del superhéroe más alto de género F: {obtener_nombre_superheroe(superheroe_mas_alto_genero_f)}")
                    print(f"Nombre del superhéroe más bajo de género M: {obtener_nombre_superheroe(superheroe_mas_bajo_genero_m)}")
                    print(f"Nombre del superhéroe más bajo de género F: {obtener_nombre_superheroe(superheroe_mas_bajo_genero_f)}")
                elif opcion == 'J':
                    conteo_color_ojos = contar_superheroes_por_atributo(lista, 'color_ojos')
                    print("Cantidad de superhéroes por color de ojos:")
                    for color, cantidad in conteo_color_ojos.items():
                        print(f"{color}: {cantidad}")
                elif opcion == 'K':
                    conteo_color_pelo = contar_superheroes_por_atributo(lista, 'color_pelo')
                    print("Cantidad de superhéroes por color de pelo:")
                    for color, cantidad in conteo_color_pelo.items():
                        print(f"{color}: {cantidad}")
                elif opcion == 'L':
                    conteo_inteligencia = contar_superheroes_por_atributo(lista, 'inteligencia')
                    print("Cantidad de superhéroes por tipo de inteligencia:")
                    for tipo, cantidad in conteo_inteligencia.items():
                        print(f"{tipo}: {cantidad}")
                elif opcion == 'M':
                    superheroes_agrupados_color_ojos = agrupar_superheroes_por_atributo(lista, 'color_ojos')
                    print("Superhéroes agrupados por color de ojos:")
                    for color, superheroes in superheroes_agrupados_color_ojos.items():
                        print(f"{color}:")
                        for heroe in superheroes:
                            print(f" - {obtener_nombre_superheroe(heroe)}")
                elif opcion == 'N':
                    superheroes_agrupados_color_pelo = agrupar_superheroes_por_atributo(lista, 'color_pelo')
                    print("Superhéroes agrupados por color de pelo:")
                    for color, superheroes in superheroes_agrupados_color_pelo.items():
                        print(f"{color}:")
                        for heroe in superheroes:
                            print(f" - {obtener_nombre_superheroe(heroe)}")
                elif opcion == 'O':
                    superheroes_agrupados_inteligencia = agrupar_superheroes_por_atributo(lista, 'inteligencia')
                    print("Superhéroes agrupados por tipo de inteligencia:")
                    for inteligencia, superheroes in superheroes_agrupados_inteligencia.items():
                        print(f"{inteligencia}:")
                        for heroe in superheroes:
                            print(f" - {obtener_nombre_superheroe(heroe)}")
                elif opcion == 'P':
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
                os.system('pause')
        elif opcion == '8':
            salir = input("Confirma salida? (s/n): ").capitalize()
            if salir == 'S':
                os.system('cls')
                print("Vuelva pronto!")
                break
            elif salir == 'N':
                continue
            else:
                print("Opción inválida. Por favor, ingrese una opción válida. (s/n): ")
                continue
        else:
            print("Opción inválida. Intente nuevamente.")
    elif opcion == '8':
            print("Vuelva pronto!")
            break
    else:
        os.system('cls')
        print("Primero debe cargar los datos...")
    os.system('pause')
