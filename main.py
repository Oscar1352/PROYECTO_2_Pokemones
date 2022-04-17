# Segundo proyecto, Pokémones

# Librerias importadas
import os
# Variables globales
import random

# Características iniciales del pokémon
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

# Guardar datos de movimientos
movimiento_1 = []
movimiento_2 = []
movimiento_3 = []
movimiento_4 = []

#Función para movimientos, 30 movimientos
def movimientos(numero_aleatorio):
    global movimientos_pokemon
    tipo_de_movimiento = ""
    potencia = 0
    precision = 0
    if numero_aleatorio == 1:
        movimientos_pokemon = "Látigo_cepa"
        tipo_de_movimiento = "Planta"
        potencia = 35
        precision = 100
    elif numero_aleatorio == 2:
        movimientos_pokemon = "Latigazo"
        tipo_de_movimiento = "Planta"
        potencia = 120
        precision = 85
    elif numero_aleatorio == 3:
        movimientos_pokemon = "Rayo solar"
        tipo_de_movimiento = "Planta"
        potencia = 120
        precision = 100
    elif numero_aleatorio == 4:
        movimientos_pokemon = "Ascuas"
        tipo_de_movimiento = "Fuego"
        potencia = 40
        precision = 100
    elif numero_aleatorio == 5:
        movimientos_pokemon = "Lanzallamas"
        tipo_de_movimiento = "Fuego"
        potencia = 90
        precision = 100
    elif numero_aleatorio == 6:
        movimientos_pokemon = "Puño fuego"
        tipo_de_movimiento = "Fuego"
        potencia = 75
        precision = 100
    elif numero_aleatorio == 7:
        movimientos_pokemon = "Hidrobomba"
        tipo_de_movimiento = "Agua"
        potencia = 120
        precision = 80
    elif numero_aleatorio == 8:
        movimientos_pokemon = "Pistola agua"
        tipo_de_movimiento = "Agua"
        potencia = 40
        precision = 100
    elif numero_aleatorio == 9:
        movimientos_pokemon = "Rayo burbuja"
        tipo_de_movimiento = "Agua"
        potencia = 65
        precision = 100
    elif numero_aleatorio == 10:
        movimientos_pokemon = "Chupa vidas"
        tipo_de_movimiento = "Bicho"
        potencia = 20
        precision = 100
    elif numero_aleatorio == 11:
        movimientos_pokemon = "Pin misil"
        tipo_de_movimiento = "Bicho"
        potencia = 14
        precision = 85
    elif numero_aleatorio == 12:
        movimientos_pokemon = "Tijera X"
        tipo_de_movimiento = "Bicho"
        potencia = 80
        precision = 100
    elif numero_aleatorio == 13:
        movimientos_pokemon = "Picotazo"
        tipo_de_movimiento = "Volador"
        potencia = 35
        precision = 100
    elif numero_aleatorio == 14:
        movimientos_pokemon = "Pico taladro"
        tipo_de_movimiento = "Volador"
        potencia = 80
        precision = 100
    elif numero_aleatorio == 15:
        movimientos_pokemon = "Tornado"
        tipo_de_movimiento = "Volador"
        potencia = 40
        precision = 100
    elif numero_aleatorio == 16:
        movimientos_pokemon = "Agarre"
        tipo_de_movimiento = "Normal"
        potencia = 55
        precision = 100
    elif numero_aleatorio == 17:
        movimientos_pokemon = "Ataque rápido"
        tipo_de_movimiento = "Normal"
        potencia = 40
        precision = 100
    elif numero_aleatorio == 18:
        movimientos_pokemon = "Bomba huevo"
        tipo_de_movimiento = "Normal"
        potencia = 100
        precision = 75
    elif numero_aleatorio == 19:
        movimientos_pokemon = "Ácido"
        tipo_de_movimiento = "Veneno"
        potencia = 40
        precision = 100
    elif numero_aleatorio == 20:
        movimientos_pokemon = "Picotazo venenoso"
        tipo_de_movimiento = "Veneno"
        potencia = 55
        precision = 100
    elif numero_aleatorio == 21:
        movimientos_pokemon = "Residuos"
        tipo_de_movimiento = "Veneno"
        potencia = 65
        precision = 100
    elif numero_aleatorio == 22:
        movimientos_pokemon = "Pueño trueno"
        tipo_de_movimiento = "Eléctrico"
        potencia = 75
        precision = 100
    elif numero_aleatorio == 23:
        movimientos_pokemon = "Trueo"
        tipo_de_movimiento = "Eléctrico"
        potencia = 120
        precision = 70
    elif numero_aleatorio == 24:
        movimientos_pokemon = "Rayo"
        tipo_de_movimiento = "Veneno"
        potencia = 95
        precision = 100
    elif numero_aleatorio == 25:
        movimientos_pokemon = "Hueso palo"
        tipo_de_movimiento = "Tierra"
        potencia = 65
        precision = 85
    elif numero_aleatorio == 26:
        movimientos_pokemon = "Huesomerang"
        tipo_de_movimiento = "Tierra"
        potencia = 50
        precision = 90
    elif numero_aleatorio == 27:
        movimientos_pokemon = "Terremoto"
        tipo_de_movimiento = "Tierra"
        potencia = 100
        precision = 100
    elif numero_aleatorio == 28:
        movimientos_pokemon = "Come sueños"
        tipo_de_movimiento = "Psíquico"
        potencia = 100
        precision = 100
    elif numero_aleatorio == 29:
        movimientos_pokemon = "Bola neblina"
        tipo_de_movimiento = "Psíquico"
        potencia = 70
        precision = 100
    elif numero_aleatorio == 30:
        movimientos_pokemon = "Resplandor"
        tipo_de_movimiento = "Psíquico"
        potencia = 70
        precision = 100
        # Se mantiene un arreglo con los datos de características de cada movimiento
    return movimientos_pokemon, tipo_de_movimiento, potencia, precision


    # Generar número aleatorio para las funciones a utulizar de 1-15

# Listado de pokemon con sus caractersiticas, 20 personajes
def listado_de_pokemon(numero_aleatorio):
    nombre = ""
    tipo = ""
    puntos_de_salud = 0
    ataque = 0
    defensa = 0
    velocidad = 0
    experiencia_base = 0

    if numero_aleatorio == 1:
        nombre = "Bulbasaur"
        tipo = "Planta"
        puntos_de_salud = 45
        ataque = 49
        defensa = 49
        velocidad = 45
        experiencia_base = 64
    elif numero_aleatorio == 2:
        nombre = "Charmander"
        tipo = "Fuego"
        puntos_de_salud = 39
        ataque = 52
        defensa = 43
        velocidad = 65
        experiencia_base = 65
    elif numero_aleatorio == 3:
        nombre = "Squirtle"
        tipo = "Agua"
        puntos_de_salud = 44
        ataque = 48
        defensa = 65
        velocidad = 43
        experiencia_base = 66
    elif numero_aleatorio == 4:
        nombre = "Caterpie"
        tipo = "Bicho"
        puntos_de_salud = 45
        ataque = 30
        defensa = 35
        velocidad = 45
        experiencia_base = 53
    elif numero_aleatorio == 5:
        nombre = "Weedle"
        tipo = "Bicho"
        puntos_de_salud = 40
        ataque = 35
        defensa = 30
        velocidad = 50
        experiencia_base = 52
    elif numero_aleatorio == 6:
        nombre = "Pidgey"
        tipo = "Volador"
        puntos_de_salud = 40
        ataque = 45
        defensa = 40
        velocidad = 56
        experiencia_base = 55
    elif numero_aleatorio == 7:
        nombre = "Rattata"
        tipo = "Normal"
        puntos_de_salud = 30
        ataque = 56
        defensa = 35
        velocidad = 72
        experiencia_base = 57
    elif numero_aleatorio == 8:
        nombre = "Spearow"
        tipo = "Volador"
        puntos_de_salud = 40
        ataque = 60
        defensa = 30
        velocidad = 70
        experiencia_base = 58
    elif numero_aleatorio == 9:
        nombre = "Ekans"
        tipo = "Veneno"
        puntos_de_salud = 35
        ataque = 60
        defensa = 44
        velocidad = 55
        experiencia_base = 62
    elif numero_aleatorio == 10:
        nombre = "Pikachu"
        tipo = "Eléctrico"
        puntos_de_salud = 35
        ataque = 55
        defensa = 40
        velocidad = 90
        experiencia_base = 82
    elif numero_aleatorio == 11:
        nombre = "Sandshrew"
        tipo = "Tierra"
        puntos_de_salud = 50
        ataque = 75
        defensa = 85
        velocidad = 40
        experiencia_base = 93
    elif numero_aleatorio == 12:
        nombre = "Vulpix"
        tipo = "Fuego"
        puntos_de_salud = 38
        ataque = 41
        defensa = 40
        velocidad = 65
        experiencia_base = 63
    elif numero_aleatorio == 13:
        nombre = "Jigglypuff"
        tipo = "Normal"
        puntos_de_salud = 115
        ataque = 45
        defensa = 20
        velocidad = 20
        experiencia_base = 76
    elif numero_aleatorio == 14:
        nombre = "Zubat"
        tipo = "Veneno"
        puntos_de_salud = 40
        ataque = 45
        defensa = 35
        velocidad = 55
        experiencia_base = 54
    elif numero_aleatorio == 15:
        nombre = "Oddish"
        tipo = "Planta"
        puntos_de_salud = 45
        ataque = 50
        defensa = 55
        velocidad = 30
        experiencia_base = 78
    elif numero_aleatorio == 16:
        nombre = "Gloom"
        tipo = "Planta"
        puntos_de_salud = 60
        ataque = 65
        defensa = 70
        velocidad = 40
        experiencia_base = 132
    elif numero_aleatorio == 17:
        nombre = "Diglett"
        tipo = "Tierra"
        puntos_de_salud = 10
        ataque = 55
        defensa = 25
        velocidad = 95
        experiencia_base = 81
    elif numero_aleatorio == 18:
        nombre = "Meowth"
        tipo = "Normal"
        puntos_de_salud = 40
        ataque = 45
        defensa = 35
        velocidad = 90
        experiencia_base = 69
    elif numero_aleatorio == 19:
        nombre = "Psyduck"
        tipo = "Agua"
        puntos_de_salud = 50
        ataque = 52
        defensa = 48
        velocidad = 55
        experiencia_base = 80
    elif numero_aleatorio == 20:
        nombre = "Mewtwo"
        tipo = "Psíquico"
        puntos_de_salud = 106
        ataque = 110
        defensa = 90
        velocidad = 130
        experiencia_base = 220
    return nombre, tipo, puntos_de_salud, ataque ,defensa, velocidad,experiencia_base

# Función para generar números aletorios
def numero_aleatorio(limite_inferior, limite_superior):
    numero_aleatorio = random.randint(limite_inferior,limite_superior)
    return numero_aleatorio

# Bloque de codigo para modificar los datos iniciales
def modificar_estadísticas_iniciales():
    global pokemon_inicial,apodo_pokemon,nivel_pokemon, ataque,defensa,velocidad,puntos_de_vida, movimientos_pokemon, \
        movimiento_1, movimiento_2
    # Dar apodo al pokémon
    apodo_pokemon = input("\x1b[1;0m" + f"Por favor ingrese el apodo que quiera darle a su pokémon {pokemon_inicial}: ")
    # Dar nivel al pokémnon
    nivel_pokemon = 5
    # Dar valores aleatorios a las características
    ataque = numero_aleatorio(1,15)
    defensa = numero_aleatorio(1,15)
    velocidad = numero_aleatorio(1,15)
    puntos_de_vida = numero_aleatorio(1,15)
    movimiento_1 = movimientos(numero_aleatorio(1,30))
    movimiento_2 = movimientos(numero_aleatorio(1,30))
    movimientos_pokemon = [movimiento_1[0], movimiento_2[0]]

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