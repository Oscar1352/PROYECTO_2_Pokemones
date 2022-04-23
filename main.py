# Segundo proyecto, Pokémones

# Librerias importadas
import os
# Variables globales
import random

# Características iniciales del pokémon
movimientos_pokemon = []
movimientos_pokemon_usuario = []
movimientos_pokemon_enemigo = []
ataque_a_usar = []
pokemon_inicial = {
    "nombre" : "",
    "apodo" : "",
    "tipo" : "",
    "salud" : 0,
    "puntos_de_vida" : 0,
    "dato_de_combate" : 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_inicial_global = []

# Pokémones enemigos
pokemon_enemigos = []
pokemon_Bulbasaur = {
    "nombre" : "Bulbasaur",
    "tipo" : "Planta",
    "salud": 45,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 49,
    "defensa" : 49,
    "velocidad" : 45,
    "experiencia_base" : 64,
    "nivel" : 0
}
pokemon_Charmander = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Squirtle = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Caterpie = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Weedle = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Pidgey = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Rattata = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Spearow = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Ekans = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Pikachu = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Sandshrew = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Vulpix = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Jigglypuff = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Zubat = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Oddish = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Gloom = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Diglett = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Meowth = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Psyduck = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}
pokemon_Mewtwo = {
    "nombre" : "",
    "tipo" : "",
    "salud": 0,
    "puntos_de_salud": 0,
    "dato_de_combate": 0,
    "ataque" : 0,
    "defensa" : 0,
    "velocidad" : 0,
    "experiencia_base" : 0,
    "nivel" : 0
}

#Movimientos
movimientos_pokemon_Latigazo = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Látigo_cepa = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Rayo_solar = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Ascuas = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Lanzallamas = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Puño_fuego = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Hidrobomba = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Pistola_agua = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Rayo_burbuja = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Chupa_vidas = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Pin_misil = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Tijera_X = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Picotazo = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Pico_taladro = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Tornado = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Agarre = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Ataque_rápido = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Bomba_huevo = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Ácido = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Picotazo_venenoso = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Residuos = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Pueño_trueno = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Trueo = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Rayo = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Hueso_palo = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Huesomerang = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Terremoto = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Come_sueños = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Bola_neblina = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}
movimientos_pokemon_Resplandor = {
    "nombre" : "",
    "tipo_de_movimiento" : "",
    "potencia" : 0,
    "precision" : 0
}

# Guardar datos de movimientos usuario
movimiento_1 = []
movimiento_2 = []
movimiento_3 = []
movimiento_4 = []

# Guardar datos de movimientos enemigo
movimiento_1_enemigo = []
movimiento_2_enemigo = []
movimiento_3_enemigo = []
movimiento_4_enemigo = []

#Función para movimientos, 30 movimientos
def movimientos(numero_aleatorio):
    # Variables a utilziar
    global movimientos_pokemon_Látigo_cepa, movimientos_pokemon, movimientos_pokemon_Latigazo, movimientos_pokemon_Rayo_solar, movimientos_pokemon_Ascuas, \
    movimientos_pokemon_Lanzallamas, movimientos_pokemon_Puño_fuego, movimientos_pokemon_Hidrobomba, movimientos_pokemon_Pistola_agua,\
    movimientos_pokemon_Rayo_burbuja, movimientos_pokemon_Chupa_vidas, movimientos_pokemon_Pin_misil, movimientos_pokemon_Tijera_X, \
    movimientos_pokemon_Picotazo, movimientos_pokemon_Pico_taladro, movimientos_pokemon_Tornado, movimientos_pokemon_Agarre, movimientos_pokemon_Ataque_rápido, \
    movimientos_pokemon_Bomba_huevo, movimientos_pokemon_Ácido, movimientos_pokemon_Picotazo_venenoso, movimientos_pokemon_Residuos, movimientos_pokemon_Pueño_trueno, \
    movimientos_pokemon_Trueo, movimientos_pokemon_Rayo, movimientos_pokemon_Hueso_palo, movimientos_pokemon_Huesomerang, movimientos_pokemon_Terremoto, \
    movimientos_pokemon_Come_sueños, movimientos_pokemon_Bola_neblina, movimientos_pokemon_Resplandor

    # Movimientos según el anexo del enunciado
    if numero_aleatorio == 1:
        movimientos_pokemon_Látigo_cepa["nombre"] = "Látigo_cepa"
        movimientos_pokemon_Látigo_cepa["tipo_de_movimiento"] = "Planta"
        movimientos_pokemon_Látigo_cepa["potencia"] = 35
        movimientos_pokemon_Látigo_cepa["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Látigo_cepa
    elif numero_aleatorio == 2:
        movimientos_pokemon_Latigazo["nombre"] = "Latigazo"
        movimientos_pokemon_Latigazo["tipo_de_movimiento"] = "Planta"
        movimientos_pokemon_Latigazo["potencia"] = 120
        movimientos_pokemon_Latigazo["precision"] = 85
        movimientos_pokemon = movimientos_pokemon_Latigazo
    elif numero_aleatorio == 3:
        movimientos_pokemon_Rayo_solar["nombre"] = "Rayo solar"
        movimientos_pokemon_Rayo_solar["tipo_de_movimiento"] = "Planta"
        movimientos_pokemon_Rayo_solar["potencia"] = 120
        movimientos_pokemon_Rayo_solar["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Rayo_solar
    elif numero_aleatorio == 4:
        movimientos_pokemon_Ascuas["nombre"] = "Ascuas"
        movimientos_pokemon_Ascuas["tipo_de_movimiento"] = "Fuego"
        movimientos_pokemon_Ascuas["potencia"] = 40
        movimientos_pokemon_Ascuas["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Ascuas
    elif numero_aleatorio == 5:
        movimientos_pokemon_Lanzallamas["nombre"] = "Lanzallamas"
        movimientos_pokemon_Lanzallamas["tipo_de_movimiento"] = "Fuego"
        movimientos_pokemon_Lanzallamas["potencia"] = 90
        movimientos_pokemon_Lanzallamas["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Lanzallamas
    elif numero_aleatorio == 6:
        movimientos_pokemon_Puño_fuego["nombre"] = "Puño fuego"
        movimientos_pokemon_Puño_fuego["tipo_de_movimiento"] = "Fuego"
        movimientos_pokemon_Puño_fuego["potencia"] = 75
        movimientos_pokemon_Puño_fuego["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Puño_fuego
    elif numero_aleatorio == 7:
        movimientos_pokemon_Hidrobomba["nombre"] = "Hidrobomba"
        movimientos_pokemon_Hidrobomba["tipo_de_movimiento"] = "Agua"
        movimientos_pokemon_Hidrobomba["potencia"] = 120
        movimientos_pokemon_Hidrobomba["precision"] = 80
        movimientos_pokemon = movimientos_pokemon_Hidrobomba
    elif numero_aleatorio == 8:
        movimientos_pokemon_Pistola_agua["nombre"] = "Pistola agua"
        movimientos_pokemon_Pistola_agua["tipo_de_movimiento"] = "Agua"
        movimientos_pokemon_Pistola_agua["potencia"] = 40
        movimientos_pokemon_Pistola_agua["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Pistola_agua
    elif numero_aleatorio == 9:
        movimientos_pokemon_Rayo_burbuja["nombre"] = "Rayo burbuja"
        movimientos_pokemon_Rayo_burbuja["tipo_de_movimiento"] = "Agua"
        movimientos_pokemon_Rayo_burbuja["potencia"] = 65
        movimientos_pokemon_Rayo_burbuja["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Rayo_burbuja
    elif numero_aleatorio == 10:
        movimientos_pokemon_Chupa_vidas["nombre"] = "Chupa vidas"
        movimientos_pokemon_Chupa_vidas["tipo_de_movimiento"] = "Bicho"
        movimientos_pokemon_Chupa_vidas["potencia"] = 20
        movimientos_pokemon_Chupa_vidas["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Chupa_vidas
    elif numero_aleatorio == 11:
        movimientos_pokemon_Pin_misil["nombre"] = "Pin misil"
        movimientos_pokemon_Pin_misil["tipo_de_movimiento"] = "Bicho"
        movimientos_pokemon_Pin_misil["potencia"] = 14
        movimientos_pokemon_Pin_misil["precision"] = 85
        movimientos_pokemon = movimientos_pokemon_Pin_misil
    elif numero_aleatorio == 12:
        movimientos_pokemon_Tijera_X["nombre"] = "Tijera X"
        movimientos_pokemon_Tijera_X["tipo_de_movimiento"] = "Bicho"
        movimientos_pokemon_Tijera_X["potencia"] = 80
        movimientos_pokemon_Tijera_X["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Tijera_X
    elif numero_aleatorio == 13:
        movimientos_pokemon_Picotazo["nombre"] = "Picotazo"
        movimientos_pokemon_Picotazo["tipo_de_movimiento"] = "Volador"
        movimientos_pokemon_Picotazo["potencia"] = 35
        movimientos_pokemon_Picotazo["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Picotazo
    elif numero_aleatorio == 14:
        movimientos_pokemon_Pico_taladro["nombre"] = "Pico taladro"
        movimientos_pokemon_Pico_taladro["tipo_de_movimiento"] = "Volador"
        movimientos_pokemon_Pico_taladro["potencia"] = 80
        movimientos_pokemon_Pico_taladro["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Pico_taladro
    elif numero_aleatorio == 15:
        movimientos_pokemon_Tornado["nombre"] = "Tornado"
        movimientos_pokemon_Tornado["tipo_de_movimiento"] = "Volador"
        movimientos_pokemon_Tornado["potencia"] = 40
        movimientos_pokemon_Tornado["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Tornado
    elif numero_aleatorio == 16:
        movimientos_pokemon_Agarre["nombre"] = "Agarre"
        movimientos_pokemon_Agarre["tipo_de_movimiento"] = "Normal"
        movimientos_pokemon_Agarre["potencia"] = 55
        movimientos_pokemon_Agarre["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Agarre
    elif numero_aleatorio == 17:
        movimientos_pokemon_Ataque_rápido["nombre"] = "Ataque rápido"
        movimientos_pokemon_Ataque_rápido["tipo_de_movimiento"] = "Normal"
        movimientos_pokemon_Ataque_rápido["potencia"] = 40
        movimientos_pokemon_Ataque_rápido["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Ataque_rápido
    elif numero_aleatorio == 18:
        movimientos_pokemon_Bomba_huevo["nombre"] = "Bomba huevo"
        movimientos_pokemon_Bomba_huevo["tipo_de_movimiento"] = "Normal"
        movimientos_pokemon_Bomba_huevo["potencia"] = 100
        movimientos_pokemon_Bomba_huevo["precision"] = 75
        movimientos_pokemon = movimientos_pokemon_Ataque_rápido
    elif numero_aleatorio == 19:
        movimientos_pokemon_Ácido["nombre"] = "Ácido"
        movimientos_pokemon_Ácido["tipo_de_movimiento"] = "Veneno"
        movimientos_pokemon_Ácido["potencia"] = 40
        movimientos_pokemon_Ácido["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Ácido
    elif numero_aleatorio == 20:
        movimientos_pokemon_Picotazo_venenoso["nombre"] = "Picotazo venenoso"
        movimientos_pokemon_Picotazo_venenoso["tipo_de_movimiento"] = "Veneno"
        movimientos_pokemon_Picotazo_venenoso["potencia"] = 55
        movimientos_pokemon_Picotazo_venenoso["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Ácido
    elif numero_aleatorio == 21:
        movimientos_pokemon_Residuos["nombre"] = "Residuos"
        movimientos_pokemon_Residuos["tipo_de_movimiento"] = "Veneno"
        movimientos_pokemon_Residuos["potencia"] = 65
        movimientos_pokemon_Residuos["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Residuos
    elif numero_aleatorio == 22:
        movimientos_pokemon_Pueño_trueno["nombre"] = "Pueño trueno"
        movimientos_pokemon_Pueño_trueno["tipo_de_movimiento"] = "Eléctrico"
        movimientos_pokemon_Pueño_trueno["potencia"] = 75
        movimientos_pokemon_Pueño_trueno["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Pueño_trueno
    elif numero_aleatorio == 23:
        movimientos_pokemon_Trueo["nombre"] = "Trueo"
        movimientos_pokemon_Trueo["tipo_de_movimiento"] = "Eléctrico"
        movimientos_pokemon_Trueo["potencia"] = 120
        movimientos_pokemon_Trueo["precision"] = 70
        movimientos_pokemon = movimientos_pokemon_Trueo
    elif numero_aleatorio == 24:
        movimientos_pokemon_Rayo["nombre"] = "Rayo"
        movimientos_pokemon_Rayo["tipo_de_movimiento"] = "Eléctrico"
        movimientos_pokemon_Rayo["potencia"] = 95
        movimientos_pokemon_Rayo["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Rayo
    elif numero_aleatorio == 25:
        movimientos_pokemon_Hueso_palo["nombre"] = "Hueso palo"
        movimientos_pokemon_Hueso_palo["tipo_de_movimiento"] = "Tierra"
        movimientos_pokemon_Hueso_palo["potencia"] = 65
        movimientos_pokemon_Hueso_palo["precision"] = 85
        movimientos_pokemon = movimientos_pokemon_Hueso_palo
    elif numero_aleatorio == 26:
        movimientos_pokemon_Huesomerang["nombre"] = "Huesomerang"
        movimientos_pokemon_Huesomerang["tipo_de_movimiento"] = "Tierra"
        movimientos_pokemon_Huesomerang["potencia"] = 50
        movimientos_pokemon_Huesomerang["precision"] = 90
        movimientos_pokemon = movimientos_pokemon_Huesomerang
    elif numero_aleatorio == 27:
        movimientos_pokemon_Terremoto["nombre"] = "Terremoto"
        movimientos_pokemon_Terremoto["tipo_de_movimiento"] = "Tierra"
        movimientos_pokemon_Terremoto["potencia"] = 100
        movimientos_pokemon_Terremoto["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Terremoto
    elif numero_aleatorio == 28:
        movimientos_pokemon_Come_sueños["nombre"] = "Come sueños"
        movimientos_pokemon_Come_sueños["tipo_de_movimiento"] = "Psíquico"
        movimientos_pokemon_Come_sueños["potencia"] = 100
        movimientos_pokemon_Come_sueños["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Come_sueños
    elif numero_aleatorio == 29:
        movimientos_pokemon_Bola_neblina["nombre"] = "Bola neblina"
        movimientos_pokemon_Bola_neblina["tipo_de_movimiento"] = "Psíquico"
        movimientos_pokemon_Bola_neblina["potencia"] = 70
        movimientos_pokemon_Bola_neblina["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Bola_neblina
    elif numero_aleatorio == 30:
        movimientos_pokemon_Resplandor["nombre"] = "Resplandor"
        movimientos_pokemon_Resplandor["tipo_de_movimiento"] = "Psíquico"
        movimientos_pokemon_Resplandor["potencia"] = 70
        movimientos_pokemon_Resplandor["precision"] = 100
        movimientos_pokemon = movimientos_pokemon_Resplandor
        # Se mantiene un arreglo con los datos de características de cada movimiento
    return movimientos_pokemon

    # Generar número aleatorio para las funciones a utulizar de 1-15

# Listado de pokemon con sus caractersiticas, 20 personajes
def listado_de_pokemon(numero_aleatorio):
    #Variables a utilizar
    global pokemon_Bulbasaur, pokemon_Charmander, pokemon_Squirtle, pokemon_Caterpie, pokemon_Weedle, pokemon_Pidgey, pokemon_Rattata, \
    pokemon_Spearow, pokemon_Ekans, pokemon_Pikachu, pokemon_Sandshrew, pokemon_Vulpix, pokemon_Jigglypuff, pokemon_Zubat, pokemon_Oddish, \
    pokemon_Gloom, pokemon_Diglett, pokemon_Meowth, pokemon_Psyduck, pokemon_Mewtwo, pokemon_enemigos

    # Listado de pokemones según el anexo del listado
    if numero_aleatorio == 1:
        pokemon_Bulbasaur["nombre"] = "Bulbasaur"
        pokemon_Bulbasaur["tipo"] = "Planta"
        pokemon_Bulbasaur["salud"] = 45
        pokemon_Bulbasaur["ataque"] = 49
        pokemon_Bulbasaur["defensa"] = 49
        pokemon_Bulbasaur["velocidad"] = 45
        pokemon_Bulbasaur["experiencia_base"] = 64
        pokemon_Bulbasaur["nivel"] = 0
        pokemon_enemigos = pokemon_Bulbasaur
    elif numero_aleatorio == 2:
        pokemon_Charmander["nombre"] = "Charmander"
        pokemon_Charmander["tipo"] = "Fuego"
        pokemon_Charmander["salud"] = 39
        pokemon_Charmander["ataque"] = 52
        pokemon_Charmander["defensa"] = 43
        pokemon_Charmander["velocidad"] = 65
        pokemon_Charmander["experiencia_base"] = 65
        pokemon_Charmander["nivel"] = 0
        pokemon_enemigos = pokemon_Charmander
    elif numero_aleatorio == 3:
        pokemon_Squirtle["nombre"] = "Squirtle"
        pokemon_Squirtle["tipo"] = "Agua"
        pokemon_Squirtle["salud"] = 44
        pokemon_Squirtle["ataque"] = 48
        pokemon_Squirtle["defensa"] = 65
        pokemon_Squirtle["velocidad"] = 43
        pokemon_Squirtle["experiencia_base"] = 66
        pokemon_Squirtle["nivel"] = 0
        pokemon_enemigos = pokemon_Squirtle
    elif numero_aleatorio == 4:
        pokemon_Caterpie["nombre"] = "Caterpie"
        pokemon_Caterpie["tipo"] = "Bicho"
        pokemon_Caterpie["salud"] = 45
        pokemon_Caterpie["ataque"] = 30
        pokemon_Caterpie["defensa"] = 35
        pokemon_Caterpie["velocidad"] = 45
        pokemon_Caterpie["experiencia_base"] = 53
        pokemon_Caterpie["nivel"] = 0
        pokemon_enemigos = pokemon_Caterpie
    elif numero_aleatorio == 5:
        pokemon_Weedle["nombre"] = "Weedle"
        pokemon_Weedle["tipo"] = "Bicho"
        pokemon_Weedle["salud"] = 40
        pokemon_Weedle["ataque"] = 35
        pokemon_Weedle["defensa"] = 30
        pokemon_Weedle["velocidad"] = 50
        pokemon_Weedle["experiencia_base"] = 52
        pokemon_Weedle["nivel"] = 0
        pokemon_enemigos = pokemon_Weedle
    elif numero_aleatorio == 6:
        pokemon_Pidgey["nombre"] = "Pidgey"
        pokemon_Pidgey["tipo"] = "Volador"
        pokemon_Pidgey["salud"] = 40
        pokemon_Pidgey["ataque"] = 45
        pokemon_Pidgey["defensa"] = 40
        pokemon_Pidgey["velocidad"] = 56
        pokemon_Pidgey["experiencia_base"] = 55
        pokemon_Pidgey["nivel"] = 0
        pokemon_enemigos = pokemon_Pidgey
    elif numero_aleatorio == 7:
        pokemon_Rattata["nombre"] = "Rattata"
        pokemon_Rattata["tipo"] = "Normal"
        pokemon_Rattata["salud"] = 30
        pokemon_Rattata["ataque"] = 56
        pokemon_Rattata["defensa"] = 35
        pokemon_Rattata["velocidad"] = 72
        pokemon_Rattata["experiencia_base"] = 57
        pokemon_Rattata["nivel"] = 0
        pokemon_enemigos = pokemon_Rattata
    elif numero_aleatorio == 8:
        pokemon_Spearow["nombre"] = "Spearow"
        pokemon_Spearow["tipo"] = "Volador"
        pokemon_Spearow["salud"] = 40
        pokemon_Spearow["ataque"] = 60
        pokemon_Spearow["defensa"] = 30
        pokemon_Spearow["velocidad"] = 70
        pokemon_Spearow["experiencia_base"] = 58
        pokemon_Spearow["nivel"] = 0
        pokemon_enemigos = pokemon_Spearow
    elif numero_aleatorio == 9:
        pokemon_Ekans["nombre"] = "Ekans"
        pokemon_Ekans["tipo"] = "Veneno"
        pokemon_Ekans["salud"] = 35
        pokemon_Ekans["ataque"] = 60
        pokemon_Ekans["defensa"] = 44
        pokemon_Ekans["velocidad"] = 55
        pokemon_Ekans["experiencia_base"] = 62
        pokemon_Ekans["nivel"] = 0
        pokemon_enemigos = pokemon_Ekans
    elif numero_aleatorio == 10:
        pokemon_Pikachu["nombre"] = "Pikachu"
        pokemon_Pikachu["tipo"] = "Eléctrico"
        pokemon_Pikachu["salud"] = 35
        pokemon_Pikachu["ataque"] = 55
        pokemon_Pikachu["defensa"] = 40
        pokemon_Pikachu["velocidad"] = 90
        pokemon_Pikachu["experiencia_base"] = 82
        pokemon_Pikachu["nivel"] = 0
        pokemon_enemigos = pokemon_Pikachu
    elif numero_aleatorio == 11:
        pokemon_Sandshrew["nombre"] = "Sandshrew"
        pokemon_Sandshrew["tipo"] = "Tierra"
        pokemon_Sandshrew["salud"] = 50
        pokemon_Sandshrew["ataque"] = 75
        pokemon_Sandshrew["defensa"] = 85
        pokemon_Sandshrew["velocidad"] = 40
        pokemon_Sandshrew["experiencia_base"] = 93
        pokemon_Sandshrew["nivel"] = 0
        pokemon_enemigos = pokemon_Sandshrew
    elif numero_aleatorio == 12:
        pokemon_Vulpix["nombre"] = "Vulpix"
        pokemon_Vulpix["tipo"] = "Fuego"
        pokemon_Vulpix["puntos_de_salud"] = 38
        pokemon_Vulpix["ataque"] = 41
        pokemon_Vulpix["defensa"] = 40
        pokemon_Vulpix["velocidad"] = 65
        pokemon_Vulpix["experiencia_base"] = 63
        pokemon_Vulpix["nivel"] = 0
        pokemon_enemigos = pokemon_Vulpix
    elif numero_aleatorio == 13:
        pokemon_Jigglypuff["nombre"] = "Jigglypuff"
        pokemon_Jigglypuff["tipo"] = "Normal"
        pokemon_Jigglypuff["salud"] = 115
        pokemon_Jigglypuff["ataque"] = 45
        pokemon_Jigglypuff["defensa"] = 20
        pokemon_Jigglypuff["velocidad"] = 20
        pokemon_Jigglypuff["experiencia_base"] = 76
        pokemon_Jigglypuff["nivel"] = 0
        pokemon_enemigos = pokemon_Jigglypuff
    elif numero_aleatorio == 14:
        pokemon_Zubat["nombre"] = "Zubat"
        pokemon_Zubat["tipo"] = "Veneno"
        pokemon_Zubat["salud"] = 40
        pokemon_Zubat["ataque"] = 45
        pokemon_Zubat["defensa"] = 35
        pokemon_Zubat["velocidad"] = 55
        pokemon_Zubat["experiencia_base"] = 54
        pokemon_Zubat["nivel"] = 0
        pokemon_enemigos = pokemon_Zubat
    elif numero_aleatorio == 15:
        pokemon_Oddish["nombre"] = "Oddish"
        pokemon_Oddish["tipo"] = "Planta"
        pokemon_Oddish["salud"] = 45
        pokemon_Oddish["ataque"] = 50
        pokemon_Oddish["defensa"] = 55
        pokemon_Oddish["velocidad"] = 30
        pokemon_Oddish["experiencia_base"] = 78
        pokemon_Oddish["nivel"] = 0
        pokemon_enemigos = pokemon_Oddish
    elif numero_aleatorio == 16:
        pokemon_Gloom["nombre"] = "Gloom"
        pokemon_Gloom["tipo"] = "Planta"
        pokemon_Gloom["salud"] = 60
        pokemon_Gloom["ataque"] = 65
        pokemon_Gloom["defensa"] = 70
        pokemon_Gloom["velocidad"] = 40
        pokemon_Gloom["experiencia_base"] = 132
        pokemon_Gloom["nivel"] = 0
        pokemon_enemigos = pokemon_Gloom
    elif numero_aleatorio == 17:
        pokemon_Diglett["nombre"] = "Diglett"
        pokemon_Diglett["tipo"] = "Tierra"
        pokemon_Diglett["salud"] = 10
        pokemon_Diglett["ataque"] = 55
        pokemon_Diglett["defensa"] = 25
        pokemon_Diglett["velocidad"] = 95
        pokemon_Diglett["experiencia_base"] = 81
        pokemon_Diglett["nivel"] = 0
        pokemon_enemigos = pokemon_Diglett
    elif numero_aleatorio == 18:
        pokemon_Meowth["nombre"] = "Meowth"
        pokemon_Meowth["tipo"] = "Normal"
        pokemon_Meowth["salud"] = 40
        pokemon_Meowth["ataque"] = 45
        pokemon_Meowth["defensa"] = 35
        pokemon_Meowth["velocidad"] = 90
        pokemon_Meowth["experiencia_base"] = 69
        pokemon_Meowth["nivel"] = 0
        pokemon_enemigos = pokemon_Meowth
    elif numero_aleatorio == 19:
        pokemon_Psyduck["nombre"] = "Psyduck"
        pokemon_Psyduck["tipo"] = "Agua"
        pokemon_Psyduck["salud"] = 50
        pokemon_Psyduck["ataque"] = 52
        pokemon_Psyduck["defensa"] = 48
        pokemon_Psyduck["velocidad"] = 55
        pokemon_Psyduck["experiencia_base"] = 80
        pokemon_Psyduck["nivel"] = 0
        pokemon_enemigos = pokemon_Psyduck
    elif numero_aleatorio == 20:
        pokemon_Mewtwo["nombre"] = "Mewtwo"
        pokemon_Mewtwo["tipo"] = "Psíquico"
        pokemon_Mewtwo["salud"] = 106
        pokemon_Mewtwo["ataque"] = 110
        pokemon_Mewtwo["defensa"] = 90
        pokemon_Mewtwo["velocidad"] = 130
        pokemon_Mewtwo["experiencia_base"] = 220
        pokemon_Mewtwo["nivel"] = 0
        pokemon_enemigos = pokemon_Mewtwo
        # Le otorgo los datos de puntos de salud al pokemon
    return pokemon_enemigos

# Función para generar números aletorios
def numero_aleatorio(limite_inferior, limite_superior):
    numero_aleatorio = random.randint(limite_inferior,limite_superior)
    return numero_aleatorio

#mostrar los datos en pantalla
def mostrar_datos_en_pantallla():
    print("\x1b[1;34m", pokemon_inicial["nombre"],pokemon_inicial["nivel"], pokemon_inicial["puntos_de_vida"])
    print("\x1b[1;31m", pokemon_enemigos["nombre"],pokemon_enemigos["nivel"], pokemon_enemigos["puntos_de_vida"])

# Bloque de codigo para modificar los datos iniciales
def modificar_estadísticas_iniciales():
    global pokemon_inicial, movimientos_pokemon_usuario,  movimiento_1, movimiento_2
    # Dar apodo al pokémon
    pokemon_inicial["apodo"] = input("\x1b[1;0m" + f"Por favor ingrese el apodo que quiera darle a su pokémon "+pokemon_inicial["nombre"]+": ")
    # Dar nivel al pokémnon
    pokemon_inicial["nivel"] = 5
    # Dar valores aleatorios a las características
    pokemon_inicial["ataque"] = numero_aleatorio(1,15)
    pokemon_inicial["defensa"] = numero_aleatorio(1,15)
    pokemon_inicial["velocidad"] = numero_aleatorio(1,15)
    pokemon_inicial["salud"] = numero_aleatorio(1,15)
    # Se extrae los movimientos de manera aleatoria
    movimiento_1 = movimientos(numero_aleatorio(1,30))
    movimiento_2 = movimientos(numero_aleatorio(1,30))
    movimientos_pokemon_usuario.append(movimiento_1["nombre"])
    movimientos_pokemon_usuario.append(movimiento_2["nombre"])

# Calcular los datos de combate del usuario
def datos_de_combate_usuario():
    global pokemon_inicial, pokemon_inicial_global
    pokemon_inicial["puntos_de_vida"] = ((pokemon_inicial["salud"] + 2 * pokemon_inicial_global["salud"]) * (pokemon_inicial["nivel"] / 100) + 10 + pokemon_inicial["nivel"])
    pokemon_inicial["dato_de_combate"] = (((pokemon_inicial["ataque"] + 2 * pokemon_inicial_global["ataque"]) * (pokemon_inicial["nivel"] / 100)) + 5 )

# Calcular los datos de combate del usuario
def datos_de_combate_enemigo():
    global pokemon_inicial, pokemon_enemigos
    pokemon_enemigos = listado_de_pokemon(numero_aleatorio(1,20))
    pokemon_enemigos["puntos_de_vida"] = ((pokemon_enemigos["salud"] + 2 * pokemon_enemigos["puntos_de_salud"]) * (pokemon_enemigos["nivel"] / 100) + 10 + pokemon_enemigos["nivel"])
    pokemon_enemigos["dato_de_combate"] = (((pokemon_enemigos["ataque"] + 2 * pokemon_enemigos["ataque"]) * (pokemon_enemigos["nivel"] / 100)) + 5 )
    pokemon_enemigos["puntos_de_salud"] = numero_aleatorio(1,15)
    if numero_aleatorio(1,2) == 1:
        pokemon_enemigos["nivel"] = pokemon_inicial["nivel"] + 4
    else:
        pokemon_enemigos["nivel"] = pokemon_inicial["nivel"] - 4

# Calcular los movimientos aleatorios del enemigo
def movimientos_enemigo():
    global movimientos_pokemon_enemigo, movimiento_1_enemigo, movimiento_2_enemigo, movimiento_3_enemigo, movimiento_4_enemigo
    movimiento_1_enemigo = movimientos(numero_aleatorio(1,30))
    movimiento_2_enemigo = movimientos(numero_aleatorio(1,30))
    movimiento_3_enemigo = movimientos(numero_aleatorio(1,30))
    movimiento_4_enemigo = movimientos(numero_aleatorio(1,30))
    movimientos_pokemon_enemigo = movimiento_1_enemigo["nombre"], movimiento_2_enemigo["nombre"], movimiento_3_enemigo["nombre"], movimiento_4_enemigo["nombre"]

# Bloque de codigo batallas salvajes
def batalla():
    global movimientos_pokemon_usuario, ataque_a_usar, movimientos_pokemon_enemigo, movimiento_1, movimiento_2, movimiento_3, movimiento_4
    movimiento_valido = False
    opcion_menu = False
    datos_de_combate_usuario()
    datos_de_combate_enemigo()
    movimientos_enemigo()
    # Menú de batalla
    os.system("cls")  # Función para limpiar la pantalla y mostrar el menú
    print("\n\x1b[1;34m" + "\t\t\t\t\tMENÚ DE BATALLA: ")
    print("\n\x1b[1;0m" +"Selecciona una opción: ")
    print("\ta - Atacar.")
    print("\tb - Regresar.")
    while not opcion_menu:
        opcionMenu = input("\nInserta la variable del menú que desees ingresar: ")
        if opcionMenu == "a":
            # Imprimo los movimientos que tiene posibilidad el usuario
            for i in range(0, len(movimientos_pokemon_usuario)):
                print("\x1b[1;0m", i, "-- ", movimientos_pokemon_usuario[i])

            # Escoger el ataque a utilizar durante el programa
            while not movimiento_valido:
                eleccion = int(
                    input(f"Por favor de escoger el ataque que usará 0-{len(movimientos_pokemon_usuario) - 1}: "))

                if eleccion == 0:
                    ataque_a_usar.append(movimiento_1)
                    movimiento_valido = True
                elif eleccion == 1:
                    ataque_a_usar.append(movimiento_2)
                    movimiento_valido = True
                elif eleccion == 2:
                    ataque_a_usar.append(movimiento_3)
                    movimiento_valido = True
                elif eleccion == 3:
                    ataque_a_usar.append(movimiento_4)
                    movimiento_valido = True
                else:
                    print("Opción inválida ")
            opcion_menu = True
        elif opcionMenu == "b":
            print("Usted regresará al menú principal\n")
            opcion_menu = True
            menu()
        else:
            print("Opción inválida. ")

# Bloque de codigo para chequear estadísticas
def estadísticas():
    #Variables globales
    global pokemon_inicial, movimientos_pokemon_usuario, pokemon_inicial_global

    datos_de_combate_usuario()
    #Características principales
    print("\x1b[1;34m" + "DATOS ")
    print("\x1b[1;0m" + "Nombre: "+pokemon_inicial["nombre"])
    print("Apodo: "+pokemon_inicial["apodo"])
    print("Nivel: "+str(pokemon_inicial["nivel"]))
    print("Experiencia: "+str(pokemon_inicial["experiencia_base"]))
    print("Tipo: "+pokemon_inicial["tipo"])
    print(f"Movimientos: {movimientos_pokemon_usuario}")

    # Características de datos de combate
    print("\x1b[1;34m" + "DATOS DE COMBATE")
    print("\x1b[1;0m" + "Salud: "+str(pokemon_inicial["salud"]))
    print("\x1b[1;0m" + "Ataque: "+str(pokemon_inicial["ataque"]))
    print("\x1b[1;0m" + "Defensa: "+str(pokemon_inicial["defensa"]))
    print("\x1b[1;0m" + "Velocidad: "+str(pokemon_inicial["velocidad"]))
    print("Datos de Combate: ", pokemon_inicial["dato_de_combate"])
    print("Datos de Combate: ", pokemon_inicial["puntos_de_vida"])
    input("PRESIONE UNA TECLA PARA REGRESAR AL MENÚ...")
    menu()

# Bloque de codigo inicio del juego
def seleccion_pokemon():
    global pokemon_inicial, pokemon_inicial_global
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
            pokemon_inicial["tipo"] = "Planta"
            pokemon_inicial_global = pokemon_Bulbasaur
            print("\x1b[1;32m" + "\t\t\t\t\t\tUsted ha escogido correctamente a: "+ pokemon_inicial["nombre"]+"\n")
            modificar_estadísticas_iniciales()
            break
        elif opcionPokemon == "b":
            # El usuario escogío a Charmander
            pokemon_inicial["nombre"] =  "Charmander"
            pokemon_inicial["tipo"] = "Fuego"
            pokemon_inicial_global = pokemon_Charmander
            print("\x1b[1;32m" + "\t\t\t\t\t\tUsted ha escogido correctamente a: "+ pokemon_inicial["nombre"]+"\n")
            modificar_estadísticas_iniciales()
            break
        elif opcionPokemon == "c":
            # El usuario escogío a Squirtle
            pokemon_inicial["nombre"] =  "Squirtle"
            pokemon_inicial["tipo"] = "Agua"
            pokemon_inicial_global = pokemon_Squirtle
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
    print("\n\t\t\tBienvenido a Pokémon Rojo, uno de los juegos más populares de consola para GameBoy del año 1996, ¿LISTO PARA SER EL CAMPÉON DE LA REGIÓN?")
    #Solicitar los datos para el incio del juego
    seleccion_pokemon()
    menu()

#Ejecución del programa
main()