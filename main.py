# * Aqui ira toda la logica del juego * #
# * MENU * #













# * LOGICA DEL JUEGO * #
import random   # import es para adquirir funciones de distintas librerias que vienen con Python
import sys
import time

# Una funcion es un pedazo de código que puede ser reutilizado varias veces
# También puede llevar parámetros que siempre estarán dentro de los parentesis y representan
# alguna variable a pasar en cierto punto del código
# En Python, se utiliza def para inicializar una funcion y para llamarla se pone el nombre junto
# con los parámetros dentro del parentesis
# * #
def eleccion_invalida(eleccion):
    print("Tus pensamientos se nublan y sientes que eres forzado a elegir")
    # time.sleep hace que lo que el codigo pare por x segundos
    time.sleep(2)
    eleccion = random.choice(["A", "B", "C"])
    # return indica el final de una funcion se utiliza cuando una función va a devolver un valor
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

# time.sleep retrasa el programa por los segundos puestos entre parentesis
time.sleep(2)

print(
    "Cierras los ojos al sentir el impacto sobre todo tu cuerpo y tu cabeza. "
    "Lo siguiente que recuerdas es levantarte en medio de la oscuridad, con frío...")

empezar_g = input("¿Desea continuar? (N/S): ").upper()
if empezar_g != 'S':
    print("El frio te inmoviliza, hiela tus piernas y esperas el final con una ultima vista a la oscuridad")
    print()
    print()
    print()
    print("                     | ☼               ☼ |                    ")
    print("                     |  ^-----___-----^  |                    ")
    print()
    print()
    time.sleep(3)
    sys.exit()
else:
    #print("¿Qué harías?\nA - Ver alrededor\nB - Observarte\nC - Hay algo sobre mi espalda...")
    elecc = elecciones("Ver alrededor", "Observarte", "Hay algo sobre mi espalda...")
    inv = 0
    while elecc != "A" and elecc != "B" and elecc != "C":
        elecc = input("Elige una acción: ").upper()
        inv += 1
        if inv == 3:
            elecc = eleccion_invalida(elecc)
    print("Tu elección fue:", elecc)
    time.sleep(1)
    if elecc == "A":
        print("Miras a tu alrededor y solo vez oscuridad.\n"
              "El suelo en donde caíste era duro y accidentado.\n")
        print("No hay alguna luz más de la que cae de la luna a travez del hueco de donde caíste.")
        time.sleep(1)
    elif elecc == "B":
        print("Miras el estado de tu ropa y cuerpo:\n"
              "Tus piernas están algo heridas.\nTu cabeza recién se esta recuperando de la cada.")
        time.sleep(1)
    elif elecc == "C":
        print("Es pesado y parece estar sostenido por tus hombros.\nEs una mochila y parece estar medio llena.")
        time.sleep(1)

print("Tu sentidos vuelven a la realidad al escuchar un fuerte eco desde lo profundo de la oscuridad.")
print("Tu estomago se retuerce y algo te dice que no deberías estar ahi")

if elecc == "C":
    elecc = elecciones("Empezar a moverte", "Esconderte", "Buscar dentro de la mochila")
    #print("¿Qué harías?\nA - Empezar a moverte\nB - Esconderte\nC - Buscar dentro de la mochila")
    inv = 0
    while elecc != "A" and elecc != "B" and elecc != "C":
        elecc = input("Elige una acción: ").upper()
        inv += 1
        if inv == 3:
            elecc = eleccion_invalida(elecc)
    if elecc == "A":
        print("Mochila + A")
    elif elecc == "B":
        print("Mochila + B")
    elif elecc == "C":
        print("Mochila + C")
else:
    elecc = elecciones("Empezar a moverte", "Esconderte", "Crear una distracción")
    inv = 0
    while elecc != "A" and elecc != "B" and elecc != "C":
        elecc = input("Elige una acción: ").upper()
        inv += 1
        if inv == 3:
            elecc = eleccion_invalida(elecc)
    if elecc == "A":
        print("A")
    elif elecc == "B":
        print("B")
    elif elecc == "C":
        print("C")
    #print("¿Qué harías?\nA - Empezar a moverte\nB - Esconderte\nC - Crear una distracción")



