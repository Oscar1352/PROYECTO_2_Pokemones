from numpy import random


def probabilidad_de_acertar_el_golpe(tipo_de_ataque_usuario, tipo_de_ataque_enemigo):
    probabilidad = 0

    # Genera un manejo de ataque según la probabilidad establecida
    if tipo_de_ataque_usuario == "Planta" and tipo_de_ataque_enemigo == "Planta":
        probabilidad = random.binomial(n=1, p=.5, size=1)
    else:
        print(tipo_de_ataque_usuario + tipo_de_ataque_enemigo)

    if probabilidad == 1:
        print(f"Ataque acertado: {probabilidad}")
    else:
        print(f"Ataque fallado{probabilidad}")
    return probabilidad

def main():
    tipo_de_ataque_usuario ={
        "nombre": "prueba1",
        "tipo" : "Planta"
    }
    tipo_de_ataque_enemigo ={
        "nombre": "prueba2",
        "tipo" : "Planta"
    }
    probabilidad_de_acertar_el_golpe(tipo_de_ataque_usuario["tipo"], tipo_de_ataque_enemigo["tipo"])


main()