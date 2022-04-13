# Segundo proyecto, Pokémones

# Librerias importadas
import os
# Variables globales
pokemon_inicial = ""


def batalla():
    return


def estadísticas():
    return


def menu():
    opcionMenu = ""
    os.system("cls")  # Función para limpiar la pantalla y mostrar el menú
    print("Selecciona una opción: ")
    print("\ta - Batalla contra Pokémon salvaje.")
    print("\tb - Ver estadísticas de mi Pokémon.")
    print("\tc - Salir del videojuego.")
    # solicituamos una opción al usuario
    opcionMenu = input("\nInserta la variable del menú que desees ingresar: ")
    while opcionMenu != ["a","b","c"]:
        if opcionMenu == "a":
            print("\x1b[1;0m" + "\t\t\t\t\t\tBienvenido a la batalla contra Pokémon salvaje, Buena suerte...\n")
            batalla()
            break
        elif opcionMenu == "b":
            print("\x1b[1;0m" + "\t\t\t\t\t\tBienvenido al menú de estadísticas...\n")
            estadísticas()
            break
        elif opcionMenu == "c":
            print("\x1b[1;31m" + "\t\t\t\t\t\tMuchas gracias por probar el maravilloso juego de Pokémon. ¡Hasta la próxima!")
            exit()
        else:
            # Utilizo los códigos ANSI para dar estética a la salida del videojuego
            print("No has pulsado ninguna opción correcta...\n")
            opcionMenu = input("inserta un numero valor >> ")


def main():
    #Solicitar los datos para el incio del juego
    menu()




#Ejecución del programa
main()