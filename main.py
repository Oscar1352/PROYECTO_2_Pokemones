# Segundo proyecto, Pokémones

# Librerias importadas
import os, random, time
from numpy import random
# Variables globales


# Características iniciales del pokémon
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
pokemon_enemigo = []
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

def borrarPantalla():
    borrarPantalla = lambda: os.system ("cls") #Limpia la pantalla

#Función para movimientos, 30 movimientos
def movimientos(numero_aleatorio):
    # Variables a utilziar
    global movimientos_pokemon_Látigo_cepa, movimientos_pokemon_Latigazo, movimientos_pokemon_Rayo_solar, movimientos_pokemon_Ascuas, \
    movimientos_pokemon_Lanzallamas, movimientos_pokemon_Puño_fuego, movimientos_pokemon_Hidrobomba, movimientos_pokemon_Pistola_agua,\
    movimientos_pokemon_Rayo_burbuja, movimientos_pokemon_Chupa_vidas, movimientos_pokemon_Pin_misil, movimientos_pokemon_Tijera_X, \
    movimientos_pokemon_Picotazo, movimientos_pokemon_Pico_taladro, movimientos_pokemon_Tornado, movimientos_pokemon_Agarre, movimientos_pokemon_Ataque_rápido, \
    movimientos_pokemon_Bomba_huevo, movimientos_pokemon_Ácido, movimientos_pokemon_Picotazo_venenoso, movimientos_pokemon_Residuos, movimientos_pokemon_Pueño_trueno, \
    movimientos_pokemon_Trueo, movimientos_pokemon_Rayo, movimientos_pokemon_Hueso_palo, movimientos_pokemon_Huesomerang, movimientos_pokemon_Terremoto, \
    movimientos_pokemon_Come_sueños, movimientos_pokemon_Bola_neblina, movimientos_pokemon_Resplandor

    movimientos_pokemon = []

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
    pokemon_Gloom, pokemon_Diglett, pokemon_Meowth, pokemon_Psyduck, pokemon_Mewtwo, pokemon_enemigo

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
        pokemon_enemigo = pokemon_Bulbasaur
    elif numero_aleatorio == 2:
        pokemon_Charmander["nombre"] = "Charmander"
        pokemon_Charmander["tipo"] = "Fuego"
        pokemon_Charmander["salud"] = 39
        pokemon_Charmander["ataque"] = 52
        pokemon_Charmander["defensa"] = 43
        pokemon_Charmander["velocidad"] = 65
        pokemon_Charmander["experiencia_base"] = 65
        pokemon_Charmander["nivel"] = 0
        pokemon_enemigo = pokemon_Charmander
    elif numero_aleatorio == 3:
        pokemon_Squirtle["nombre"] = "Squirtle"
        pokemon_Squirtle["tipo"] = "Agua"
        pokemon_Squirtle["salud"] = 44
        pokemon_Squirtle["ataque"] = 48
        pokemon_Squirtle["defensa"] = 65
        pokemon_Squirtle["velocidad"] = 43
        pokemon_Squirtle["experiencia_base"] = 66
        pokemon_Squirtle["nivel"] = 0
        pokemon_enemigo = pokemon_Squirtle
    elif numero_aleatorio == 4:
        pokemon_Caterpie["nombre"] = "Caterpie"
        pokemon_Caterpie["tipo"] = "Bicho"
        pokemon_Caterpie["salud"] = 45
        pokemon_Caterpie["ataque"] = 30
        pokemon_Caterpie["defensa"] = 35
        pokemon_Caterpie["velocidad"] = 45
        pokemon_Caterpie["experiencia_base"] = 53
        pokemon_Caterpie["nivel"] = 0
        pokemon_enemigo = pokemon_Caterpie
    elif numero_aleatorio == 5:
        pokemon_Weedle["nombre"] = "Weedle"
        pokemon_Weedle["tipo"] = "Bicho"
        pokemon_Weedle["salud"] = 40
        pokemon_Weedle["ataque"] = 35
        pokemon_Weedle["defensa"] = 30
        pokemon_Weedle["velocidad"] = 50
        pokemon_Weedle["experiencia_base"] = 52
        pokemon_Weedle["nivel"] = 0
        pokemon_enemigo = pokemon_Weedle
    elif numero_aleatorio == 6:
        pokemon_Pidgey["nombre"] = "Pidgey"
        pokemon_Pidgey["tipo"] = "Volador"
        pokemon_Pidgey["salud"] = 40
        pokemon_Pidgey["ataque"] = 45
        pokemon_Pidgey["defensa"] = 40
        pokemon_Pidgey["velocidad"] = 56
        pokemon_Pidgey["experiencia_base"] = 55
        pokemon_Pidgey["nivel"] = 0
        pokemon_enemigo = pokemon_Pidgey
    elif numero_aleatorio == 7:
        pokemon_Rattata["nombre"] = "Rattata"
        pokemon_Rattata["tipo"] = "Normal"
        pokemon_Rattata["salud"] = 30
        pokemon_Rattata["ataque"] = 56
        pokemon_Rattata["defensa"] = 35
        pokemon_Rattata["velocidad"] = 72
        pokemon_Rattata["experiencia_base"] = 57
        pokemon_Rattata["nivel"] = 0
        pokemon_enemigo = pokemon_Rattata
    elif numero_aleatorio == 8:
        pokemon_Spearow["nombre"] = "Spearow"
        pokemon_Spearow["tipo"] = "Volador"
        pokemon_Spearow["salud"] = 40
        pokemon_Spearow["ataque"] = 60
        pokemon_Spearow["defensa"] = 30
        pokemon_Spearow["velocidad"] = 70
        pokemon_Spearow["experiencia_base"] = 58
        pokemon_Spearow["nivel"] = 0
        pokemon_enemigo = pokemon_Spearow
    elif numero_aleatorio == 9:
        pokemon_Ekans["nombre"] = "Ekans"
        pokemon_Ekans["tipo"] = "Veneno"
        pokemon_Ekans["salud"] = 35
        pokemon_Ekans["ataque"] = 60
        pokemon_Ekans["defensa"] = 44
        pokemon_Ekans["velocidad"] = 55
        pokemon_Ekans["experiencia_base"] = 62
        pokemon_Ekans["nivel"] = 0
        pokemon_enemigo = pokemon_Ekans
    elif numero_aleatorio == 10:
        pokemon_Pikachu["nombre"] = "Pikachu"
        pokemon_Pikachu["tipo"] = "Eléctrico"
        pokemon_Pikachu["salud"] = 35
        pokemon_Pikachu["ataque"] = 55
        pokemon_Pikachu["defensa"] = 40
        pokemon_Pikachu["velocidad"] = 90
        pokemon_Pikachu["experiencia_base"] = 82
        pokemon_Pikachu["nivel"] = 0
        pokemon_enemigo = pokemon_Pikachu
    elif numero_aleatorio == 11:
        pokemon_Sandshrew["nombre"] = "Sandshrew"
        pokemon_Sandshrew["tipo"] = "Tierra"
        pokemon_Sandshrew["salud"] = 50
        pokemon_Sandshrew["ataque"] = 75
        pokemon_Sandshrew["defensa"] = 85
        pokemon_Sandshrew["velocidad"] = 40
        pokemon_Sandshrew["experiencia_base"] = 93
        pokemon_Sandshrew["nivel"] = 0
        pokemon_enemigo = pokemon_Sandshrew
    elif numero_aleatorio == 12:
        pokemon_Vulpix["nombre"] = "Vulpix"
        pokemon_Vulpix["tipo"] = "Fuego"
        pokemon_Vulpix["puntos_de_salud"] = 38
        pokemon_Vulpix["ataque"] = 41
        pokemon_Vulpix["defensa"] = 40
        pokemon_Vulpix["velocidad"] = 65
        pokemon_Vulpix["experiencia_base"] = 63
        pokemon_Vulpix["nivel"] = 0
        pokemon_enemigo = pokemon_Vulpix
    elif numero_aleatorio == 13:
        pokemon_Jigglypuff["nombre"] = "Jigglypuff"
        pokemon_Jigglypuff["tipo"] = "Normal"
        pokemon_Jigglypuff["salud"] = 115
        pokemon_Jigglypuff["ataque"] = 45
        pokemon_Jigglypuff["defensa"] = 20
        pokemon_Jigglypuff["velocidad"] = 20
        pokemon_Jigglypuff["experiencia_base"] = 76
        pokemon_Jigglypuff["nivel"] = 0
        pokemon_enemigo = pokemon_Jigglypuff
    elif numero_aleatorio == 14:
        pokemon_Zubat["nombre"] = "Zubat"
        pokemon_Zubat["tipo"] = "Veneno"
        pokemon_Zubat["salud"] = 40
        pokemon_Zubat["ataque"] = 45
        pokemon_Zubat["defensa"] = 35
        pokemon_Zubat["velocidad"] = 55
        pokemon_Zubat["experiencia_base"] = 54
        pokemon_Zubat["nivel"] = 0
        pokemon_enemigo = pokemon_Zubat
    elif numero_aleatorio == 15:
        pokemon_Oddish["nombre"] = "Oddish"
        pokemon_Oddish["tipo"] = "Planta"
        pokemon_Oddish["salud"] = 45
        pokemon_Oddish["ataque"] = 50
        pokemon_Oddish["defensa"] = 55
        pokemon_Oddish["velocidad"] = 30
        pokemon_Oddish["experiencia_base"] = 78
        pokemon_Oddish["nivel"] = 0
        pokemon_enemigo = pokemon_Oddish
    elif numero_aleatorio == 16:
        pokemon_Gloom["nombre"] = "Gloom"
        pokemon_Gloom["tipo"] = "Planta"
        pokemon_Gloom["salud"] = 60
        pokemon_Gloom["ataque"] = 65
        pokemon_Gloom["defensa"] = 70
        pokemon_Gloom["velocidad"] = 40
        pokemon_Gloom["experiencia_base"] = 132
        pokemon_Gloom["nivel"] = 0
        pokemon_enemigo = pokemon_Gloom
    elif numero_aleatorio == 17:
        pokemon_Diglett["nombre"] = "Diglett"
        pokemon_Diglett["tipo"] = "Tierra"
        pokemon_Diglett["salud"] = 10
        pokemon_Diglett["ataque"] = 55
        pokemon_Diglett["defensa"] = 25
        pokemon_Diglett["velocidad"] = 95
        pokemon_Diglett["experiencia_base"] = 81
        pokemon_Diglett["nivel"] = 0
        pokemon_enemigo = pokemon_Diglett
    elif numero_aleatorio == 18:
        pokemon_Meowth["nombre"] = "Meowth"
        pokemon_Meowth["tipo"] = "Normal"
        pokemon_Meowth["salud"] = 40
        pokemon_Meowth["ataque"] = 45
        pokemon_Meowth["defensa"] = 35
        pokemon_Meowth["velocidad"] = 90
        pokemon_Meowth["experiencia_base"] = 69
        pokemon_Meowth["nivel"] = 0
        pokemon_enemigo = pokemon_Meowth
    elif numero_aleatorio == 19:
        pokemon_Psyduck["nombre"] = "Psyduck"
        pokemon_Psyduck["tipo"] = "Agua"
        pokemon_Psyduck["salud"] = 50
        pokemon_Psyduck["ataque"] = 52
        pokemon_Psyduck["defensa"] = 48
        pokemon_Psyduck["velocidad"] = 55
        pokemon_Psyduck["experiencia_base"] = 80
        pokemon_Psyduck["nivel"] = 0
        pokemon_enemigo = pokemon_Psyduck
    elif numero_aleatorio == 20:
        pokemon_Mewtwo["nombre"] = "Mewtwo"
        pokemon_Mewtwo["tipo"] = "Psíquico"
        pokemon_Mewtwo["salud"] = 106
        pokemon_Mewtwo["ataque"] = 110
        pokemon_Mewtwo["defensa"] = 90
        pokemon_Mewtwo["velocidad"] = 130
        pokemon_Mewtwo["experiencia_base"] = 220
        pokemon_Mewtwo["nivel"] = 0
        pokemon_enemigo = pokemon_Mewtwo
        # Le otorgo los datos de puntos de salud al pokemon
    return pokemon_enemigo

# Función para generar números aletorios
def numero_aleatorio(limite_inferior, limite_superior):
    numero_aleatorio = random.randint(limite_inferior,limite_superior)
    return numero_aleatorio

#mostrar los datos en pantalla
def mostrar_datos_en_pantalla():
    global pokemon_inicial, pokemon_enemigo
    print("\x1b[1;34m","Pokémon del usuario Nombre:", pokemon_inicial["nombre"],"Nivel:  ",int(pokemon_inicial["nivel"]),"Puntos de vida:  ",int(pokemon_inicial["puntos_de_vida"]), "\x1b[1;0m")
    print("\x1b[1;31m","Pokémon Salvaje Nombre: ", pokemon_enemigo["nombre"],"Nivel:  ",int(pokemon_enemigo["nivel"]),"Puntos de vida:  ",int(pokemon_enemigo["puntos_de_vida"]), "\x1b[1;0m")

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

    # Se le dan los datos a utilizar al pokemon del usuario durante el combate
    pokemon_inicial["puntos_de_vida"] = ((pokemon_inicial["salud"] + 2 * pokemon_inicial_global["salud"]) * (pokemon_inicial["nivel"] / 100) + 10 + pokemon_inicial["nivel"])
    pokemon_inicial["dato_de_combate"] = (((pokemon_inicial["ataque"] + 2 * pokemon_inicial_global["ataque"]) * (pokemon_inicial["nivel"] / 100)) + 5 )

# Calcular los datos de combate del usuario
def datos_de_combate_enemigo():
    global pokemon_inicial, pokemon_enemigo

    # Se escoge un pokemon de manera aleatoria
    pokemon_enemigo = listado_de_pokemon(numero_aleatorio(1, 20))

    # Se le da el nivel a utilizar
    if random.binomial(n=1, p=.5, size=1) == 1:
        pokemon_enemigo["nivel"] = pokemon_inicial["nivel"] + 4
    else:
        pokemon_enemigo["nivel"] = pokemon_inicial["nivel"] - 4

    # Se le dan los datos a utilizar durante el ataque
    pokemon_enemigo["puntos_de_salud"] = numero_aleatorio(1, 15)
    pokemon_enemigo["puntos_de_vida"] = ((pokemon_enemigo["salud"] + 2 * pokemon_enemigo["puntos_de_salud"]) * (pokemon_enemigo["nivel"] / 100) + 10 + pokemon_enemigo["nivel"])
    pokemon_enemigo["dato_de_combate"] = (((pokemon_enemigo["ataque"] + 2 * pokemon_enemigo["ataque"]) * (pokemon_enemigo["nivel"] / 100)) + 5)

# Calcular los movimientos aleatorios del enemigo
def movimientos_enemigo():
    global movimientos_pokemon_enemigo, movimiento_1_enemigo, movimiento_2_enemigo, movimiento_3_enemigo, movimiento_4_enemigo

    # Se dan los movimientos de manera aleatoria al pokemon enemigo
    movimiento_1_enemigo = movimientos(numero_aleatorio(1,30))
    movimiento_2_enemigo = movimientos(numero_aleatorio(1,30))
    movimiento_3_enemigo = movimientos(numero_aleatorio(1,30))
    movimiento_4_enemigo = movimientos(numero_aleatorio(1,30))
    #movimientos_pokemon_enemigo = movimiento_1_enemigo["nombre"], movimiento_2_enemigo["nombre"], movimiento_3_enemigo["nombre"], movimiento_4_enemigo["nombre"]
    movimientos_pokemon_enemigo.append(movimiento_1_enemigo)
    movimientos_pokemon_enemigo.append(movimiento_2_enemigo)
    movimientos_pokemon_enemigo.append(movimiento_3_enemigo)
    movimientos_pokemon_enemigo.append(movimiento_4_enemigo)

# Probabilidad de acertar el golpe
def probabilidad_de_acertar_el_golpe(tipo_de_ataque, pokemon):
    probabilidad = 0

    # Genera un manejo de ataque según la probabilidad establecida
    # Se utiliza una escala en donde el 2 de más eficaz es 1, o 100%

    # Tipo de ataque - Planta
    if tipo_de_ataque == "Planta" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Planta" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.5, size=1)

    # Tipo de ataque - Fuego
    if tipo_de_ataque == "Fuego" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Fuego" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.5, size=1)

    # Tipo de ataque - Agua
    if tipo_de_ataque == "Agua" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Agua" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.5, size=1)

    # Tipo de ataque - Bicho
    if tipo_de_ataque == "Bicho" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Bicho" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=1, size=1)

    # Tipo de ataque - Volador
    if tipo_de_ataque == "Volador" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Volador" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.5, size=1)

    # Tipo de ataque - Normal
    if tipo_de_ataque == "Normal" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Normal" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.5, size=1)

    # Tipo de ataque - Veneno
    if tipo_de_ataque == "Veneno" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Veneno" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.5, size=1)

    # Tipo de ataque - Eléctrico
    if tipo_de_ataque == "Eléctrico" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=0, size=1)
    elif tipo_de_ataque == "Eléctrico" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.25, size=1)

    # Tipo de ataque - Tierra
    if tipo_de_ataque == "Tierra" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=0, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.25, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Tierra" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.5, size=1)

    # Tipo de ataque - Psíquico
    if tipo_de_ataque == "Psíquico" and pokemon == "Planta":
        probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Fuego":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Agua":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Bicho":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Volador":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Normal":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Veneno":
        probabilidad = random.binomial(n=1, p=1, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Eléctrico":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Tierra":
       probabilidad = random.binomial(n=1, p=.5, size=1)
    elif tipo_de_ataque == "Psíquico" and pokemon == "Psíquico":
        probabilidad = random.binomial(n=1, p=.25, size=1)
    return probabilidad

# Probabilidades de hacer un golpe crítico
def golpe_critico():
    critico = random.binomial(n=1, p= .0625, size=1)
    return critico

#Combate de pokemones
def combate_usuario(pokemon_atacante, pokemon_defensor):
    global pokemon_enemigo, pokemon_inicial,ataque_a_usar,pokemon_inicial_global
    opcion_menu_ataque = False
    mostrar_datos_en_pantalla()
    print("\n\x1b[1;34m" + "\t\t\t\t\tMENÚ DE ATAQUE: ")
    print("\n\x1b[1;0m" + "Selecciona una opción: ")
    print("\ta - Atacar.")
    print("\tb - Huir.")
    while not opcion_menu_ataque:
        opcion_menu_ataque = input("\nInserta la variable del menú que desees ingresar: ")
        if opcion_menu_ataque == "a":
            seleccion_movimientos_usuario_batalla()
            # Ataque de parte del usuario
            efectividad_usuario = probabilidad_de_acertar_el_golpe(ataque_a_usar["tipo_de_movimiento"], pokemon_defensor["tipo"])
            if efectividad_usuario == 1:
                # Variable de bonificación de ataque
                if pokemon_atacante["tipo"] == ataque_a_usar["tipo_de_movimiento"]:
                    b = 1.5
                else:
                    b= 1

                # Golpe crítico
                if golpe_critico() == 1:
                    daño_usuario = (0.01 * b * efectividad_usuario * numero_aleatorio(85, 100)) * ((((0.2) * pokemon_atacante["nivel"] + 1) * pokemon_atacante["ataque"] * int(pokemon_inicial_global["ataque"])) / (25 * pokemon_defensor["defensa"]) + 2)
                    # Dar la ventaja del golpe crítico
                    daño_usuario = daño_usuario * 1.5
                    print("Usted ha recibido la ventaja de un golpe crítico")
                else:
                    daño_usuario = (0.01 * b * efectividad_usuario * numero_aleatorio(85, 100)) * ((((0.2) * pokemon_atacante["nivel"] + 1) * pokemon_atacante["ataque"] * int(pokemon_inicial_global["ataque"])) / (25 * pokemon_defensor["defensa"]) + 2)

                # Tiempo para simular realidad en el ataque
                print("\n\x1b[1;32m" + "Turno del Usuario: " + "\x1b[1;0m")
                time.sleep(3)
                print(f"\nEl usuario hizo un total de: {daño_usuario} de daño\n")
                pokemon_enemigo["puntos_de_vida"] = pokemon_enemigo["puntos_de_vida"] - daño_usuario
                if pokemon_enemigo["puntos_de_vida"] <= 0:
                    print("\n\x1b[1;32m" + "FELICIDADES, USTED HA GANADO" + "\n\x1b[1;0m")
                else:
                    print("\n\x1b[1;32m" + "Turno del Pokémon enemigo: " + "\x1b[1;0m")
                    combate_enemigo(pokemon_enemigo, pokemon_inicial)

            #El pokemon ha fallado el ataque
            else:
                print("\n\x1b[1;32m" + "Turno del Usuario: " + "\x1b[1;0m")
                # Tiempo para simular realidad en el ataque
                time.sleep(3)
                print("\x1b[1;31m" + "Ataque fallido"+ "\x1b[1;0m")
                print("\n\x1b[1;32m" + "Turno del Pokémon enemigo: " + "\x1b[1;0m")
                combate_enemigo(pokemon_enemigo, pokemon_inicial)
            opcion_menu_ataque = True

        elif opcion_menu_ataque == "b":
            # Calcular los datos para huir
            f = ((pokemon_inicial["velocidad"] * 128) / pokemon_enemigo["velocidad"] + 30) % 256
            numero = numero_aleatorio(0, 255)
            opcion_menu_ataque = True

            if numero < f:
                print("Usted logró huir")
                time.sleep(1.5)
                menu()
            else:
                print("\x1b[1;31m" +"No es posible la huida" +"\x1b[1;0m")
                time.sleep(1.5)
                combate_de_pokemones()
            opcion_menu_ataque = True

# combate de parte del enemigo
def combate_enemigo(pokemon_atacante, pokemon_defensor):
    global pokemon_enemigo, pokemon_inicial,ataque_a_usar,pokemon_inicial_global

    mostrar_datos_en_pantalla()
    probabilidad_enemigo = probabilidad_de_acertar_el_golpe(ataque_a_usar["tipo_de_movimiento"], pokemon_defensor["tipo"])
    if probabilidad_enemigo == 1:
        # Variable de bonificación de ataque
        if pokemon_atacante["tipo"] == ataque_a_usar["tipo_de_movimiento"]:
            b = 1.5
        else:
            b= 1
        # Golpe crítico
        if golpe_critico() == 1:
            daño_enemigo = (0.01 * b * probabilidad_enemigo * numero_aleatorio(85, 100)) * ((((0.2) * pokemon_atacante["nivel"] + 1) * pokemon_atacante["ataque"] * int(pokemon_inicial_global["ataque"])) / (25 * pokemon_defensor["defensa"]) + 2)
            # Dar la ventaja del golpe crítico
            daño_enemigo = daño_enemigo * 1.5
            print("Usted ha recibido la ventaja de un golpe crítico")
        else:
            daño_enemigo = (0.01 * b * probabilidad_enemigo * numero_aleatorio(85, 100)) * ((((0.2) * pokemon_atacante["nivel"] + 1) * pokemon_atacante["ataque"] * int(pokemon_inicial_global["ataque"])) / (25 * pokemon_defensor["defensa"]) + 2)

        # Tiempo para simular realidad en el ataque
        time.sleep(3)
        print(f"El enemigo hizo un total de: {daño_enemigo} de daño\n")
        pokemon_inicial["puntos_de_vida"] = pokemon_inicial["puntos_de_vida"] - daño_enemigo
        if pokemon_inicial["puntos_de_vida"] <= 0:
            print("\n\x1b[1;31m"+"LO SENTIMOS MUCHO, EL POKEMON SALVAJE HA GANADO"+"\n\x1b[1;0m")
            print("Usted será llevado de regreso al menú principal")
            time.sleep(1.5)
            menu()
        else:
            combate_usuario(pokemon_inicial, pokemon_enemigo)
    else:
        # Tiempo para simular realidad en el ataque
        time.sleep(3)
        print("\n\x1b[1;31m" + "Ataque fallido" + "\x1b[1;0m")
        combate_usuario(pokemon_inicial, pokemon_enemigo)

# Selección de ataque de usuario
def seleccion_movimientos_usuario_batalla():
    global movimientos_pokemon_usuario, ataque_a_usar, movimientos_pokemon_enemigo, movimiento_1, movimiento_2, movimiento_3, movimiento_4, pokemon_enemigo

    movimiento_valido = False
    # Imprimo los movimientos que tiene posibilidad el usuario
    print("\n\x1b[1;34m" + "\nAtaques disponibles a usar: "+ "\x1b[1;0m")
    if len(movimientos_pokemon_usuario) == 1:
        print(0,"--",movimiento_1)
    elif len(movimientos_pokemon_usuario) == 2:
        print(0,"--",movimiento_1)
        print(1,"--",movimiento_2)
    elif len(movimientos_pokemon_usuario) == 3:
        print(0,"--",movimiento_1)
        print(1,"--",movimiento_2)
        print(2,"--",movimiento_3)
    elif len(movimientos_pokemon_usuario) == 4:
        print(0,"--",movimiento_1)
        print(1,"--",movimiento_2)
        print(2,"--",movimiento_3)
        print(3,"--",movimiento_4)
    # Escoger el ataque a utilizar durante el programa
    while not movimiento_valido:
        eleccion = int(input(f"Por favor de escoger el ataque que usará 0 - {len(movimientos_pokemon_usuario) - 1}: "))

        # Se guarda el ataque a utilizar
        if eleccion == 0:
            # Se establece el moviiento a al usuario
            ataque_a_usar = movimiento_1
            movimiento_valido = True

        elif eleccion == 1:
            # Se establece el moviiento 2 al usuario
            ataque_a_usar = movimiento_2
            movimiento_valido = True

        elif eleccion == 2:
            # Se establece el moviiento 3 al usuario
            ataque_a_usar = movimiento_3
            movimiento_valido = True

        elif eleccion == 3:
            # Se establece el moviiento 3 al usuario
            ataque_a_usar = movimiento_4
            movimiento_valido = True

        else:
            print("Opción inválida ")
            movimiento_valido = False

# Bloque de codigo batallas salvajes
def batalla():
    global pokemon_inicial, pokemon_enemigo
    # Variables a utilizar
    opcion_menu = False
    datos_de_combate_usuario()
    datos_de_combate_enemigo()
    movimientos_enemigo()
    mostrar_datos_en_pantalla()

    # Menú de batalla  #Limpia la pantalla
    borrarPantalla()  # Función para limpiar la pantalla y mostrar el menú
    print("\n\x1b[1;34m" + "\t\t\t\t\tMENÚ DE BATALLA: ")
    print("\n\x1b[1;0m" +"Selecciona una opción: ")
    print("\ta - Menú de ataque.")
    print("\tb - Regresar.")
    while not opcion_menu:
        opcionMenu = input("\nInserta la variable del menú que desees ingresar: ")

        # Se establecen las opciones para el ataque
        if opcionMenu == "a":
            combate_usuario(pokemon_inicial, pokemon_enemigo)
            opcion_menu = True

        # Se regresa al menú principal
        elif opcionMenu == "b":
            print("Usted regresará al menú principal\n")
            time.sleep(1.5)
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
    print("Movimientos:", movimientos_pokemon_usuario)

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
    borrarPantalla()  # Función para limpiar la pantalla y mostrar el menú
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