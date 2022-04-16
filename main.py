# Segundo proyecto, Pokémones

# Librerias importadas
import os
# Variables globales
import random

pokemon_inicial = ""
apodo_pokemon = ""
nivel_pokemon = 0
experiencia_pokemon = 0
tipo_pokemon = 0
movimientos_pokemon = []
ataque = 0
defensa = 0
velocidad = 0
puntos_de_vida = 0

# Generar número aleatorio para las funciones a utulizar de 1-15
def numero_aleatorio(limite_inferior, limite_superior):
    numero_aleatorio = random.randint(limite_inferior,limite_superior)
    return numero_aleatorio

# Bloque de codigo para modificar los datos iniciales
def modificar_estadísticas_iniciales():
    global pokemon_inicial,apodo_pokemon,nivel_pokemon, ataque,defensa,velocidad,puntos_de_vida
    # Dar apodo al pokémon
    apodo_pokemon = input("\x1b[1;0m" + f"Por favor ingrese el apodo que quiera darle a su pokémon {pokemon_inicial}: ")
    # Dar nivel al pokémnon
    nivel_pokemon = 5
    # Dar valores aleatorios a las características
    ataque = numero_aleatorio(1,15)
    defensa = numero_aleatorio(1,15)
    velocidad = numero_aleatorio(1,15)
    puntos_de_vida = numero_aleatorio(1,15)

# Bloque de codigo batallas salvajes
def batalla():
    return

# Bloque de codigo para chequear estadísticas
def estadísticas():
    global pokemon_inicial, apodo_pokemon, nivel_pokemon, experiencia_pokemon, \
        tipo_pokemon, movimientos_pokemon, ataque, defensa, velocidad, puntos_de_vida
    print("\x1b[1;34m" + "DATOS ")
    print("\x1b[1;0m" + f"Nombre: {pokemon_inicial}")
    print(f"Apodo: {apodo_pokemon}")
    print(f"Nivel: {nivel_pokemon}")
    print(f"Experiencia: {experiencia_pokemon}")
    print(f"Tipo: {tipo_pokemon}")
    print(f"Movimientos: {movimientos_pokemon}")
    print("\x1b[1;34m" + "DATOS DE COMBATE")
    print("\x1b[1;0m" + f"Puntos de Salud: {puntos_de_vida}")
    print("\x1b[1;0m" + f"Ataque: {ataque}")
    print("\x1b[1;0m" + f"Defensa: {defensa}")
    print("\x1b[1;0m" + f"Velocidad: {velocidad}")
    input("PRESIONE UNA TECLA PARA REGRESAR AL MENÚ...")
    menu()

# Bloque de codigo inicio del juego
def seleccion_pokemon():
    global pokemon_inicial
    opcionPokemon = ""
    os.system("cls")  # Función para limpiar la pantalla y mostrar el menú
    print("\n\x1b[1;34m" + "\t\t\t\t\tMENÚ  DE SELECCIÓN DE POKÉMON INICIAL: ")
    print("\x1b[1;0m" + "Selecciona tu Pokémon inicial: ")
    print("\ta - Bulbasaur.")
    print("\tb - Charmander")
    print("\tc - Squirtle")
    # solicituamos una opción al usuario
    opcionPokemon = input("\nInserta la variable del menú que desees ingresar: ")
    while opcionPokemon != ["a", "b", "c"]:
        if opcionPokemon == "a":
            pokemon_inicial = "Bulbasaur"
            print("\x1b[1;32m" + f"\t\t\t\t\t\tUsted ha escogido correctamente a: {pokemon_inicial}\n")
            modificar_estadísticas_iniciales()
            break
        elif opcionPokemon == "b":
            pokemon_inicial = "Charmander"
            print("\x1b[1;32m" + f"\t\t\t\t\t\tUsted ha escogido correctamente a: {pokemon_inicial}\n")
            modificar_estadísticas_iniciales()
            break
        elif opcionPokemon == "c":
            pokemon_inicial = "Squirtle"
            print("\x1b[1;32m" + f"\t\t\t\t\t\tUsted ha escogido correctamente a: {pokemon_inicial}\n")
            modificar_estadísticas_iniciales()
            break
        else:
            # Utilizo los códigos ANSI para dar estética a la salida del videojuego
            print("\x1b[1;31m" + "No has pulsado ninguna opción correcta...\n")
            opcionPokemon = input("\x1b[1;0m" + "inserta un numero valor >> ")

# Bloque de codigo del menú principal del juego
def menu():
    opcionMenu = ""
    os.system("cls")  # Función para limpiar la pantalla y mostrar el menú
    print("\n\x1b[1;34m" + "\t\t\t\t\tMENÚ PRINCIPAL: ")
    print("\n\x1b[1;0m" +"Selecciona una opción: ")
    print("\ta - Batalla contra Pokémon salvaje.")
    print("\tb - Ver estadísticas de mi Pokémon.")
    print("\tc - Salir del videojuego.")
    # solicituamos una opción al usuario
    opcionMenu = input("\nInserta la variable del menú que desees ingresar: ")
    while opcionMenu != ["a","b","c"]:
        # Utilizo los códigos ANSI para dar estética a la salida del videojuego
        if opcionMenu == "a":
            # Escogió el apartado de batalla
            print("\x1b[1;32m" + "\t\t\t\t\t\tBienvenido a la batalla contra Pokémon salvaje, Buena suerte...\n")
            batalla()
            break
        elif opcionMenu == "b":
            # Se escogió el apartado de Estadísticas
            print("\x1b[1;32m" + "\t\t\t\t\t\tBienvenido al menú de estadísticas...\n")
            estadísticas()
        elif opcionMenu == "c":
            # Se saldrá del juego
            print("\x1b[1;31m" + "\t\t\t\t\t\tMuchas gracias por probar el maravilloso juego de Pokémon. ¡Hasta la próxima!")
            exit()
        else:
            print("\x1b[1;31m" + "No has pulsado ninguna opción correcta...\n")
            opcionMenu = input("\x1b[1;0m" +"inserta un numero valor >> ")

# Bloque de codigo main
def main():
    # Mensaje de bienvenida al juego
    print("\t\t\tBienvenido a Pokémon Rojo, uno de los juegos más populares de consola para GameBoy del año 1996, ¿LISTO PARA SER EL CAMPÉON DE LA REGIÓN?")

    #Solicitar los datos para el incio del juego
    seleccion_pokemon()
    menu()


#Ejecución del programa
main()