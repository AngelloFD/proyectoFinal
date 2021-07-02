# * LOGICA DEL JUEGO * #
import random
import sys
import time

def eleccion_invalida(eleccion):
    print("Tus pensamientos se nublan y sientes que eres forzado a elegir")
    time.sleep(2)
    eleccion = random.choice(["A", "B", "C"])
    return eleccion


def elecciones(elA, elB, elC):
    print("¿Qué harías?")
    print("A - ", elA)
    print("B - ", elB)
    print("C - ", elC)
    respuesta = input("Tu elección: ").upper()
    return respuesta


print("Algo te seguía. No dejabas de ver sobre tus hombros, no era humano ni algún animal que hallas visto.\n"
      "De pronto, sientes un vacío debajo de tu pie derecho para luego enterarte que caías dentro de una hoyo.")

time.sleep(2)

print(
    "Cierras los ojos al sentir el impacto sobre todo tu cuerpo y tu cabeza. "
    "Lo siguiente que recuerdas es levantarte en medio de la oscuridad, con frío...")

empezar_g = input("¿Desea continuar? (N/S): ").upper()
if empezar_g != 'S':
    print("El frio te inmoviliza, hiela tus piernas y esperas el final con una ultima vista a la oscuridad")
    print()
    print()
    print("                     | ☼               ☼ |                    ")
    print("                     |  ^-----___-----^  |                    ")
    print()
    print()
    time.sleep(3)
    sys.exit()
else:
    elecc = elecciones("Ver alrededor", "Observarte", "Hay algo sobre mi espalda...")
    inv = 0
    while elecc != "A" and elecc != "B" and elecc != "C":
        elecc = input("Elige una acción: ").upper()
        inv += 1
        if inv == 3:
            elecc = eleccion_invalida(elecc)
    print("Tu elección fue:", elecc)
    print()
    time.sleep(1)
    if elecc == "A":
        print("Miras a tu alrededor y solo vez oscuridad.\n"
              "El suelo en donde caíste era duro y accidentado.\n")
        print("No hay alguna luz más de la que cae de la luna a travez del hueco de donde caíste.")
        print()
        time.sleep(1)
    elif elecc == "B":
        print("Miras el estado de tu ropa y cuerpo:\n"
              "Tus piernas están algo heridas.\nTu cabeza recién se esta recuperando de la cada.")
        print()
        time.sleep(1)
    elif elecc == "C":
        print("Es pesado y parece estar sostenido por tus hombros.\nEs una mochila y parece estar medio llena.")
        mochilaVia = True
        print()
        time.sleep(1)

print("Tu sentidos vuelven a la realidad al escuchar un fuerte eco desde lo profundo de la oscuridad.")
print("Tu estomago se retuerce, algo te dice que no deberías estar ahi")
print()

if mochilaVia:
    elecc = elecciones("Empezar a moverte", "Esconderte", "Buscar dentro de la mochila")
    mochilaOp = "Buscar desesperadamente dentro de tu mochila"
else:
    elecc = elecciones("Empezar a moverte", "Esconderte", "Crear una distracción")
    mochilaOp = ""

inv = 0
while elecc != "A" and elecc != "B" and elecc != "C":
    elecc = input("Elige una acción: ").upper()
    inv += 1
    if inv == 3:
        elecc = eleccion_invalida(elecc)
print("Tu elección fue: ", elecc, "\n")
time.sleep(1)
if elecc == "A":
    print("Decides no esperar más y te pones de pie, trotando en la dirección opuesta a los sonidos y tropezando con las rocas que sobresalían del suelo")