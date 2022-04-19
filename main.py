# Segundo proyecto, Pokémones

# Librerias importadas
import os
# Variables globales
import random

# Características iniciales del pokémon
movimientos_pokemon = []
pokemon_inicial = {
    "nombre" : "",
    "apodo" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
# Pokémones enemigos
pokemon_Bulbasaur = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Charmander = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Squirtle = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Caterpie = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Weedle = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Pidgey = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Rattata = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Spearow = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Ekans = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Pikachu = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Sandshrew = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Vulpix = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Jigglypuff = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Zubat = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Oddish = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Gloom = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Diglett = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Meowth = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Psyduck = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Mewtwo = {
    "nombre" : "",
    "tipo" : "",
    "puntos_de_vida" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}

# Guardar datos de movimientos
movimiento_1 = []
movimiento_2 = []
movimiento_3 = []
movimiento_4 = []
movimientos_pokemon = []

#Función para movimientos, 30 movimientos
def movimientos(numero_aleatorio):
    # Variables a utilziar
    global movimientos_pokemon
    tipo_de_movimiento = ""
    potencia = 0
    precision = 0

    # Movimientos según el anexo del enunciado
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
    #Variables a utilizar
    global pokemon_Bulbasaur, pokemon_Charmander, pokemon_Squirtle, pokemon_Caterpie, pokemon_Weedle, pokemon_Pidgey, pokemon_Rattata, \
    pokemon_Spearow, pokemon_Ekans, pokemon_Pikachu, pokemon_Sandshrew, pokemon_Vulpix, pokemon_Jigglypuff, pokemon_Zubat, pokemon_Oddish, \
    pokemon_Gloom, pokemon_Diglett, pokemon_Meowth, pokemon_Psyduck, pokemon_Mewtwo

    # Listado de pokemones según el anexo del listado
    if numero_aleatorio == 1:
        pokemon_Bulbasaur["nombre"] = "Bulbasaur"
        pokemon_Bulbasaur["tipo"] = "Planta"
        pokemon_Bulbasaur["puntos_de_salud"] = 45
        pokemon_Bulbasaur["ataque"] = 49
        pokemon_Bulbasaur["defensa"] = 49
        pokemon_Bulbasaur["velocidad"] = 45
        pokemon_Bulbasaur["experiencia_base"] = 64
        pokemon_Bulbasaur["nivel"] = 0
    elif numero_aleatorio == 2:
        pokemon_Charmander["nombre"] = "Charmander"
        pokemon_Charmander["tipo"] = "Fuego"
        pokemon_Charmander["puntos_de_salud"] = 39
        pokemon_Charmander["ataque"] = 52
        pokemon_Charmander["defensa"] = 43
        pokemon_Charmander["velocidad"] = 65
        pokemon_Charmander["experiencia_base"] = 65
        pokemon_Charmander["nivel"] = 0
    elif numero_aleatorio == 3:
        pokemon_Squirtle["nombre"] = "Squirtle"
        pokemon_Squirtle["tipo"] = "Agua"
        pokemon_Squirtle["puntos_de_salud"] = 44
        pokemon_Squirtle["ataque"] = 48
        pokemon_Squirtle["defensa"] = 65
        pokemon_Squirtle["velocidad"] = 43
        pokemon_Squirtle["experiencia_base"] = 66
        pokemon_Squirtle["nivel"] = 0
    elif numero_aleatorio == 4:
        pokemon_Caterpie["nombre"] = "Caterpie"
        pokemon_Caterpie["tipo"] = "Bicho"
        pokemon_Caterpie["puntos_de_salud"] = 45
        pokemon_Caterpie["ataque"] = 30
        pokemon_Caterpie["defensa"] = 35
        pokemon_Caterpie["velocidad"] = 45
        pokemon_Caterpie["experiencia_base"] = 53
        pokemon_Caterpie["nivel"] = 0
    elif numero_aleatorio == 5:
        pokemon_Weedle["nombre"] = "Weedle"
        pokemon_Weedle["tipo"] = "Bicho"
        pokemon_Weedle["puntos_de_salud"] = 40
        pokemon_Weedle["ataque"] = 35
        pokemon_Weedle["defensa"] = 30
        pokemon_Weedle["velocidad"] = 50
        pokemon_Weedle["experiencia_base"] = 52
        pokemon_Weedle["nivel"] = 0
    elif numero_aleatorio == 6:
        pokemon_Pidgey["nombre"] = "Pidgey"
        pokemon_Pidgey["tipo"] = "Volador"
        pokemon_Pidgey["puntos_de_salud"] = 40
        pokemon_Pidgey["ataque"] = 45
        pokemon_Pidgey["defensa"] = 40
        pokemon_Pidgey["velocidad"] = 56
        pokemon_Pidgey["experiencia_base"] = 55
        pokemon_Pidgey["nivel"] = 0
    elif numero_aleatorio == 7:
        pokemon_Rattata["nombre"] = "Rattata"
        pokemon_Rattata["tipo"] = "Normal"
        pokemon_Rattata["puntos_de_salud"] = 30
        pokemon_Rattata["ataque"] = 56
        pokemon_Rattata["defensa"] = 35
        pokemon_Rattata["velocidad"] = 72
        pokemon_Rattata["experiencia_base"] = 57
        pokemon_Rattata["nivel"] = 0
    elif numero_aleatorio == 8:
        pokemon_Spearow["nombre"] = "Spearow"
        pokemon_Spearow["tipo"] = "Volador"
        pokemon_Spearow["puntos_de_salud"] = 40
        pokemon_Spearow["ataque"] = 60
        pokemon_Spearow["defensa"] = 30
        pokemon_Spearow["velocidad"] = 70
        pokemon_Spearow["experiencia_base"] = 58
        pokemon_Spearow["nivel"] = 0
    elif numero_aleatorio == 9:
        pokemon_Ekans["nombre"] = "Ekans"
        pokemon_Ekans["tipo"] = "Veneno"
        pokemon_Ekans["puntos_de_salud"] = 35
        pokemon_Ekans["ataque"] = 60
        pokemon_Ekans["defensa"] = 44
        pokemon_Ekans["velocidad"] = 55
        pokemon_Ekans["experiencia_base"] = 62
        pokemon_Ekans["nivel"] = 0
    elif numero_aleatorio == 10:
        pokemon_Pikachu["nombre"] = "Pikachu"
        pokemon_Pikachu["tipo"] = "Eléctrico"
        pokemon_Pikachu["puntos_de_salud"] = 35
        pokemon_Pikachu["ataque"] = 55
        pokemon_Pikachu["defensa"] = 40
        pokemon_Pikachu["velocidad"] = 90
        pokemon_Pikachu["experiencia_base"] = 82
        pokemon_Pikachu["nivel"] = 0
    elif numero_aleatorio == 11:
        pokemon_Sandshrew["nombre"] = "Sandshrew"
        pokemon_Sandshrew["tipo"] = "Tierra"
        pokemon_Sandshrew["puntos_de_salud"] = 50
        pokemon_Sandshrew["ataque"] = 75
        pokemon_Sandshrew["defensa"] = 85
        pokemon_Sandshrew["velocidad"] = 40
        pokemon_Sandshrew["experiencia_base"] = 93
        pokemon_Sandshrew["nivel"] = 0
    elif numero_aleatorio == 12:
        pokemon_Vulpix["nombre"] = "Vulpix"
        pokemon_Vulpix["tipo"] = "Fuego"
        pokemon_Vulpix["puntos_de_salud"] = 38
        pokemon_Vulpix["ataque"] = 41
        pokemon_Vulpix["defensa"] = 40
        pokemon_Vulpix["velocidad"] = 65
        pokemon_Vulpix["experiencia_base"] = 63
        pokemon_Vulpix["nivel"] = 0
    elif numero_aleatorio == 13:
        pokemon_Jigglypuff["nombre"] = "Jigglypuff"
        pokemon_Jigglypuff["tipo"] = "Normal"
        pokemon_Jigglypuff["puntos_de_salud"] = 115
        pokemon_Jigglypuff["ataque"] = 45
        pokemon_Jigglypuff["defensa"] = 20
        pokemon_Jigglypuff["velocidad"] = 20
        pokemon_Jigglypuff["experiencia_base"] = 76
        pokemon_Jigglypuff["nivel"] = 0
    elif numero_aleatorio == 14:
        pokemon_Zubat["nombre"] = "Zubat"
        pokemon_Zubat["tipo"] = "Veneno"
        pokemon_Zubat["puntos_de_salud"] = 40
        pokemon_Zubat["ataque"] = 45
        pokemon_Zubat["defensa"] = 35
        pokemon_Zubat["velocidad"] = 55
        pokemon_Zubat["experiencia_base"] = 54
        pokemon_Zubat["nivel"] = 0
    elif numero_aleatorio == 15:
        pokemon_Oddish["nombre"] = "Oddish"
        pokemon_Oddish["tipo"] = "Planta"
        pokemon_Oddish["puntos_de_salud"] = 45
        pokemon_Oddish["ataque"] = 50
        pokemon_Oddish["defensa"] = 55
        pokemon_Oddish["velocidad"] = 30
        pokemon_Oddish["experiencia_base"] = 78
        pokemon_Oddish["nivel"] = 0
    elif numero_aleatorio == 16:
        pokemon_Gloom["nombre"] = "Gloom"
        pokemon_Gloom["tipo"] = "Planta"
        pokemon_Gloom["puntos_de_salud"] = 60
        pokemon_Gloom["ataque"] = 65
        pokemon_Gloom["defensa"] = 70
        pokemon_Gloom["velocidad"] = 40
        pokemon_Gloom["experiencia_base"] = 132
        pokemon_Gloom["nivel"] = 0
    elif numero_aleatorio == 17:
        pokemon_Diglett["nombre"] = "Diglett"
        pokemon_Diglett["tipo"] = "Tierra"
        pokemon_Diglett["puntos_de_salud"] = 10
        pokemon_Diglett["ataque"] = 55
        pokemon_Diglett["defensa"] = 25
        pokemon_Diglett["velocidad"] = 95
        pokemon_Diglett["experiencia_base"] = 81
        pokemon_Diglett["nivel"] = 0
    elif numero_aleatorio == 18:
        pokemon_Meowth["nombre"] = "Meowth"
        pokemon_Meowth["tipo"] = "Normal"
        pokemon_Meowth["puntos_de_salud"] = 40
        pokemon_Meowth["ataque"] = 45
        pokemon_Meowth["defensa"] = 35
        pokemon_Meowth["velocidad"] = 90
        pokemon_Meowth["experiencia_base"] = 69
        pokemon_Meowth["nivel"] = 0
    elif numero_aleatorio == 19:
        pokemon_Psyduck["nombre"] = "Psyduck"
        pokemon_Psyduck["tipo"] = "Agua"
        pokemon_Psyduck["puntos_de_salud"] = 50
        pokemon_Psyduck["ataque"] = 52
        pokemon_Psyduck["defensa"] = 48
        pokemon_Psyduck["velocidad"] = 55
        pokemon_Psyduck["experiencia_base"] = 80
        pokemon_Psyduck["nivel"] = 0
    elif numero_aleatorio == 20:
        pokemon_Mewtwo["nombre"] = "Mewtwo"
        pokemon_Mewtwo["tipo"] = "Psíquico"
        pokemon_Mewtwo["puntos_de_salud"] = 106
        pokemon_Mewtwo["ataque"] = 110
        pokemon_Mewtwo["defensa"] = 90
        pokemon_Mewtwo["velocidad"] = 130
        pokemon_Mewtwo["experiencia_base"] = 220
        pokemon_Mewtwo["nivel"] = 0

# Función para generar números aletorios
def numero_aleatorio(limite_inferior, limite_superior):
    numero_aleatorio = random.randint(limite_inferior,limite_superior)
    return numero_aleatorio

# Bloque de codigo para modificar los datos iniciales
def modificar_estadísticas_iniciales():
    global pokemon_inicial, movimientos_pokemon
    # Dar apodo al pokémon
    pokemon_inicial["apodo"] = input("\x1b[1;0m" + f"Por favor ingrese el apodo que quiera darle a su pokémon "+pokemon_inicial["nombre"]+": ")
    # Dar nivel al pokémnon
    pokemon_inicial["nivel"] = 5
    # Dar valores aleatorios a las características
    pokemon_inicial["ataque"] = numero_aleatorio(1,15)
    pokemon_inicial["defensa"] = numero_aleatorio(1,15)
    pokemon_inicial["velocidad"] = numero_aleatorio(1,15)
    pokemon_inicial["puntos_de_vida"] = numero_aleatorio(1,15)
    movimiento_1 = movimientos(numero_aleatorio(1,30))
    movimiento_2 = movimientos(numero_aleatorio(1,30))
    movimientos_pokemon = [movimiento_1[0], movimiento_2[0]]

# Bloque de codigo batallas salvajes
def batalla():
    return

# Bloque de codigo para chequear estadísticas
def estadísticas():
    #Variables globales
    global pokemon_inicial, movimientos_pokemon

    #Características principales
    print("\x1b[1;34m" + "DATOS ")
    print("\x1b[1;0m" + "Nombre: "+pokemon_inicial["nombre"])
    print("Apodo: "+pokemon_inicial["apodo"])
    print("Nivel: "+str(pokemon_inicial["nivel"]))
    print("Experiencia: "+str(pokemon_inicial["experiencia_base"]))
    print("Tipo: "+pokemon_inicial["tipo"])
    print(f"Movimientos: {movimientos_pokemon}")

    # Características de datos de combate
    print("\x1b[1;34m" + "DATOS DE COMBATE")
    print("\x1b[1;0m" + "Puntos de Salud: "+str(pokemon_inicial["puntos_de_vida"]))
    print("\x1b[1;0m" + "Ataque: "+str(pokemon_inicial["ataque"]))
    print("\x1b[1;0m" + "Defensa: "+str(pokemon_inicial["defensa"]))
    print("\x1b[1;0m" + "Velocidad: "+str(pokemon_inicial["velocidad"]))
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
            # El usuario escogío a Bulbasaur
            pokemon_inicial["nombre"] = "Bulbasaur"
            print("\x1b[1;32m" + "\t\t\t\t\t\tUsted ha escogido correctamente a: "+ pokemon_inicial["nombre"]+"\n")
            modificar_estadísticas_iniciales()
            break
        elif opcionPokemon == "b":
            # El usuario escogío a Charmander
            pokemon_inicial["nombre"] =  "Charmander"
            print("\x1b[1;32m" + "\t\t\t\t\t\tUsted ha escogido correctamente a: "+ pokemon_inicial["nombre"]+"\n")
            modificar_estadísticas_iniciales()
            break
        elif opcionPokemon == "c":
            pokemon_inicial["nombre"] =  "Squirtle"
            # El usuario escogío a Squirtle
            print("\x1b[1;32m" + "\t\t\t\t\t\tUsted ha escogido correctamente a: "+ pokemon_inicial["nombre"]+"\n")
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