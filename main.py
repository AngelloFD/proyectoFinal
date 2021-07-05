# * import se utiliza para habilitar el uso de funciones de ciertas librerias que vienen con Python 
#  * #
import random
import sys
import time
import os

# * CODIGO DEL MENU * #
def creditos():
    print("Juego hecho gracias a todo el equipo 5 y cada uno de sus integrantes")
    time.sleep(1)
    print("Gómez Cornejo, Berly Matheo")
    time.sleep(1)
    print("Moscol Rojas, Jose Alonso")
    time.sleep(1)
    print("Carranza Paredes, Aldo")
    time.sleep(1)
    print("Falla Dapello, Angello Andre")
    time.sleep(1)
    print("Jaime Segundo, Vivían Ayne")
    time.sleep(1)
    print("Portugal Hilasaca, Jafeth Jose")
    time.sleep(1)
    print("Tovar Oxa, Milene")
    time.sleep(1)
    print("Rodrigo Altamirano, Alfredo Jesús")
    time.sleep(1)
    print("Ceballos Manrique, Dennis Andre")
    time.sleep(1)
    print("Huaccha Chuquitucto, Miguel Angel")
    time.sleep(5)
    print("Volviendo al menú..")
    time.sleep(5)

def printMenu(): 
    print("______________________________________")
    print("|                                    |")
    print("|                                    |")
    print("|              Trapped               |")
    print("|         Un juego de texto          |")
    print("|                                    |")
    print("|                                    |")
    print("|                                    |")
    print("|       [J] - Jugar                  |")
    print("|       [C] - Créditos               |")
    print("|       [X] - Salir                  |")
    print("|                                    |")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    op = input("Esperando a su input: ").upper()
    while op != "J" and op != "C" and op != "X":    # * Mientras que op no sea J y C y X se seguirá requiriendo el input del usuario * #
        op = input("Esperando a su input: ").upper()
    if op == "J":
        print("\nPreparando la aventura...")
        time.sleep(5)
        os.system("cls")
    elif op == "C":
        creditos()
        os.system("cls")
        printMenu()
    elif op == "X":
        print("Saliendo..")
        time.sleep(5)
        sys.exit()
printMenu()

# * LOGICA DEL JUEGO * #
def eleccion_invalida(eleccion):
    print("Tus pensamientos se nublan y sientes que eres forzado a elegir")
    time.sleep(2)
    eleccion = random.choice(["A", "B", "C"])
    return eleccion

def dibujarMonstro():
    print()
    print()
    print("                     /\_________________/\                    ")
    print("                     | ☼               ☼ |                    ")
    print("                     |  ^-----___-----^  |                    ")
    print()
    print()

def elecciones(elA, elB, elC):
    print("¿Qué harías?")
    print("A - ", elA)
    print("B - ", elB)
    if elC != 0:
        print("C - ", elC)
    respuesta = input("Tu elección: ").upper()
    return respuesta

print("Algo te seguía. No dejabas de ver sobre tus hombros, no era humano ni algún animal que hallas visto.\n"
      "De pronto, sientes un vacío debajo de tu pie derecho para luego enterarte que caías dentro de una hoyo.")
time.sleep(2)
print("Cierras los ojos al sentir el impacto sobre todo tu cuerpo y tu cabeza. "
    "Lo siguiente que recuerdas es levantarte en medio de la oscuridad, con frío...")

empezar_g = input("¿Desea continuar? (N/S): ").upper()
mochilaOp = False   #* Declarando mochilaOp falso para más adelante alterar el diálogo de acuerdo a una opción elegida *#
if empezar_g != 'S':
    print("El frio te inmoviliza, hiela tus piernas y esperas el final con una última vista a la oscuridad")
    dibujarMonstro()
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
    time.sleep(1)
    if elecc == "A":
        print("Miras a tu alrededor y solo vez oscuridad.\n"
              "El suelo en donde caíste era duro y accidentado.")
        print("No hay alguna luz más de la que cae de la luna a través del hueco de donde caíste.")
        time.sleep(1)
    elif elecc == "B":
        print("Miras el estado de tu ropa y cuerpo:\n"
              "Tus piernas están algo heridas.\nTu cabeza recién se esta recuperando de la caída.\nToda tu espalda te duele y pesa por la carga que llevas detrás de ti, es una mochila")
        mochilaOp = True
        time.sleep(1)
    elif elecc == "C":
        print("Es pesado y parece estar sostenido por tus hombros.\nEs una mochila y parece estar medio llena.")
        mochilaOp = True
        time.sleep(1)

print("\nTu sentidos vuelven a la realidad al escuchar un fuerte eco, un rugido extraño en la oscuridad.")
print("Tu estomago se retuerce y algo te dice que no deberías estar ahi")

if mochilaOp:
    elecc = elecciones("Empezar a moverte", "Esconderte", "Buscar dentro de la mochila")
else:
    elecc = elecciones("Empezar a moverte", "Esconderte", "Tratar de salir del hoyo")

inv = 0
while elecc != "A" and elecc != "B" and elecc != "C":
    elecc = input("Elige una acción: ").upper()
    inv += 1
    if inv == 3:
        elecc = eleccion_invalida(elecc)
time.sleep(1)
print("Tu elección fue:", elecc)
time.sleep(1)

if elecc == "A":
    print("Quieres moverte, pero tus piernas estan heridas y todavía tienes mareos de la caída")
    print("Decides seguir luchando y logras ponerte de pie, caminando lentamente lejos de los sonidos de lo que sea que esté viniendo")
    time.sleep(3)
    print("¿Fuiste lo suficientemente rápido para salir del camino de la bestia?")
    time.sleep(1)
    print("El respiro detrás de tu cuello te dice que no.. Solo te queda cerrar los ojos y aceptar lo que viene después..")
    time.sleep(1)
    dibujarMonstro()
    sys.exit()

elif elecc == "B":
    print("Aprovechas la altura de algunas rocas sobresalientes del suelo y la oscuridad para ocultarte. Los rugidos se vuelven se acercan a ti..")
    print("Pasan unos momentos de silencio, cierras los ojos y te acoges a lo que venga..")
    time.sleep(5)
    chance = random.randint(0,1)
    if chance == 0:
        print("Sientes un mordisco jalarte fuera de tu escondite por la pierna y otro en la espalda, gritas por ayuda..")
        time.sleep(2)
        print("Sientes cómo la vida se te escapa a mordiscos...")
        dibujarMonstro()
        sys.exit()
    else:
        print("El silencio continua hasta que es roto por un rugido distante.\nLo que sea que te halla escuchado, se ha ido.")

elif elecc == "C" and mochilaOp == False:
    print("Quieres salir del hoyo con tus propias manos pero resbalas por la superficie lisa y caes de nuevo")
    time.sleep(1)
    print("Tu caída hizo demasiado ruido, los rugidos se acercan a ti...")
    print("Tratas de correr, pero sientes un mordisco en la pierna y otro en la espalda, gritas por ayuda..")
    time.sleep(1)
    print("Sientes cómo la vida se te escapa a mordiscos...")
    dibujarMonstro()
    sys.exit()
elif mochilaOp and elecc == "C":
    print("Buscas dentro de la mochila y encuentras vendas, una botella de agua, una pistola")

elecc = elecciones("Curarte las heridas", "Usar la pistola y disparar en la dirección de los ruidos", "Guardar silencio y esperar que se vayan los ruidos")
inv = 0
while elecc != "A" and elecc != "B" and elecc != "C":
        elecc = input("Elige una acción: ").upper()
        inv += 1
        if inv == 3:
            elecc = eleccion_invalida(elecc)
print("Tu elección fue:", elecc)
time.sleep(1)
if elecc == "A":
        print("Las vendas cubren tus heridas pero no creo que halla sido un buen momento para esto.. Escuchas que los rugidos se acercan a ti")
        print("Tratas de correr, pero sientes un mordisco en la pierna y otro en la espalda, gritas por ayuda..")
        print("Sientes cómo se ta va la vida a mordiscos...")
        dibujarMonstro()
        time.sleep(1)
        sys.exit()

elif elecc == "B":
        print("Disparas en dirección de los ruidos pero por la oscuridad, no sabes donde disparar..")
        chance = random.randint(0,1)
        if chance == 0:
            print("Oyes distantes alaridos de dolor..")
            print("Te sientes aliviado de haberte desecho de esa criatura")
            time.sleep(2)
            print("Pero hiciste mucho ruido con el arma, más rugidos se acercan a ti...")
            print("Tratas de correr disparando, pero sientes un mordisco en la pierna y otro en la espalda, gritas por ayuda..")
            time.sleep(1)
            print("Sientes cómo se ta va la vida a mordiscos...")
            dibujarMonstro()
            time.sleep(1)
            sys.exit()
        else:
            print("Oyes distantes alaridos de dolor..")
            print("Te sientes aliviado de haberte desecho de esa criatura")
        
elif elecc == "C":
        print("Eres paciente y esperas a que se vayan los ruidos")
        print("Entonces después de unos minutos estas sumergido en un profundo y agradable silencio sin rugidos estremecedores")  

print("\nAhora sería un buen momento para encontrar una salida.\nPero ¿A dónde ir? Solo hay dos caminos disponibles y por uno de ellos se fue la criatura..")
elecc = elecciones("Ir a la derecha", "Ir a la izquierda",0)
inv = 0
while elecc != "A" and elecc != "B":
    elecc = input("Elige una acción: ").upper()
    inv += 1
    if inv == 3:
        elecc = eleccion_invalida(elecc)
print("Tu elección fue:", elecc)
time.sleep(1)
chance = random.randint(0,1)
if chance == 0:
    print("Empiezas a caminar por esa dirección pero te ves interrumpido al tropezar sobre algo")
    time.sleep(1)
    print("Eso empieza a chillar, un chillido que resuena en las paredes de la cueva")
    time.sleep(1)
    print("Grandes pasos se escuchan por tu detrás, corriendo a gran velocidad..")
    time.sleep(1)
    print("Tratas de correr, pero sientes un mordisco en la pierna y otro en la espalda, gritas por ayuda..")
    time.sleep(1)
    print("Sientes cómo la vida se te escapa a mordiscos...")
    dibujarMonstro()
    sys.exit()
else:
    print("Empiezas a caminar por esa dirección, es un largo camino pero logras ver una luz al final del camino")
    time.sleep(2)

elecc = elecciones("Correr", "Caminar",0)
while elecc != "A" and elecc != "B":
    elecc = input("Elige una acción: ").upper()
    inv += 1
    if inv == 3:
        elecc = eleccion_invalida(elecc)
print("Tu elección fue:", elecc)
time.sleep(1)
if elecc == "A":
    print("Tomas tus ultimas fuerzas y corres lo más rápido posible hacia la salida..")
    time.sleep(3)
    print("Logras salir de la cueva pero miras detrás de tu hombro y vez que esas cosas te siguen ahora..")
    time.sleep(1)
    print("La persecución continua..")
    print("\n                   BAD ENDING\n                   Gracias por jugar!")
    time.sleep(2)
    sys.exit()
elif elecc == "B":
    print("Te tomas tu tiempo, tratas de calmarte y sigues caminando..")
    time.sleep(3)
    print("Logras salir de la cueva sin más problemas, ni nada siguiendote.. Al fin, consigues la paz que necesitas")
    time.sleep(1)
    print("\n                   GOOD ENDING\n                   Gracias por jugar!")
    time.sleep(2)
    sys.exit()
