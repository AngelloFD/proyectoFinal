# * Aqui ira toda la logica del juego * #
# * MENU * #













# * LOGICA DEL JUEGO * #
import random
import sys
import time
def eleccion_invalida(eleccion):
    print("Tus pensamientos se nublan y sientes que eres forzado a elegir")
    time.sleep(2)
    eleccion = random.choice(["A", "B", "C"])
    return eleccion

def dibujarMonstro():
    print()
    print()
    print("                     /\_________________/\                     ")
    print("                     | ☼               ☼ |                    ")
    print("                     |  ^-----___-----^  |                    ")
    print()
    print()

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
mochilaOp = True
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
              "El suelo en donde caíste era duro y accidentado.\n")
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

print("Tu sentidos vuelven a la realidad al escuchar un fuerte eco, un rugido extraño en la oscuridad.")
print("Tu estomago se retuerce y algo te dice que no deberías estar ahi")

if mochilaOp:
    elecc = elecciones("Empezar a moverte", "Esconderte", "Buscar dentro de la mochila")
else:
    elecc = elecc = elecciones("Empezar a moverte", "Esconderte", "Tratar de salir del hoyo")

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
    print("Quieres moverte, pero tus piernas estan heridas y sientes un pequeño mareo")
    print("Revisas la mochila en tu espalda")
    print("Buscas dentro de la mochila y encuentras medicina, vendas, comida, agua, una pistola y dos cuchillos")

elif elecc == "B":
    print("Estas en un hoyo y no observas un lugar para esconderte")
    print("Revisas la mochila en tu espalda")
    print("Buscas dentro de la mochila y encuentras medicina, vendas, comida, agua, una pistola y dos cuchillos")


elif elecc == "C" and mochilaOp == False:
    print("Quieres salir del hoyo con tus propias manos pero resbalas y caes de nuevo")
    time.sleep(1)
    print("Tu caída hizo demasiado ruido, los rugidos se acercan a ti...")
    time.sleep(1)
    print(" Tratas de correr, pero sientes un mordisco en la pierna y otro en la espalda, gritas por ayuda..")
    time.sleep(1)
    print("Sientes cómo la vida se te escapa a mordiscos...")
    dibujarMonstro()
    sys.exit()
elif mochilaOp and elecc == "C":
    print("Buscas dentro de la mochila y encuentras medicina, vendas, comida, agua, una pistola y dos cuchillos")





elecc = elecciones("Curarte las heridas y alimentarte con la que hay en la mochila", "Usar la pistola y disparar en la dirección de los ruidos", "Guardar silencio y esperar que se vayan los ruidos")
inv = 0
while elecc != "A" and elecc != "B" and elecc != "C":
        elecc = input("Elige una acción: ").upper()
        inv += 1
        if inv == 3:
            elecc = eleccion_invalida(elecc)
print("Tu elección fue:", elecc)
time.sleep(1)
if elecc == "A":
        print("Estas cuarándote, pero hiciste mucho ruido.Entonces escuchas que los rugidos se acercan a ti")
        print(" Tratas de correr, pero sientes un mordisco en la pierna y otro en la espalda, gritas")
        print("Sientes cómo se ta va la vida a mordiscos...")
        dibujarMonstro()
        sys.exit()

elif elecc == "B":
        print("Disparas en dirección de los ruidos y escuchas un aullido de dolor")
        print("Te sientes aliviado de deshacerte de esa criatura")
        print("Pero hiciste mucho ruido con el arma, más rugidos se acercan a ti...")
        print(" Tratas de correr disparando, pero sientes un mordisco en la pierna y otro en la espalda y gritas")
        print("Sientes cómo se ta va la vida a mordiscos...")
        dibujarMonstro()
        sys.exit()
elif elecc == "C":
        print("Eres paciente y esperas a que se vayan los ruidos")
        print("Entonces después de unos minutos estas sumergido en un profundo y agradable silencio sin rugidos estremecedores")  

