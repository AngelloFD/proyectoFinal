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
              "Tus piernas están algo heridas.\nTu cabeza recién se esta recuperando de la caída.")
        print("Te das cuenta que tienes una mochila en la espalda")
        time.sleep(1)
    elif elecc == "C":
        print("Es pesado y parece estar sostenido por tus hombros.\nEs una mochila y parece estar medio llena.")
        time.sleep(1)

print("Tu sentidos vuelven a la realidad al escuchar un fuerte eco, un rugido extraño en la oscuridad.")
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
    time.sleep(1)
    print("Tu elección fue:", elecc)
    time.sleep()
    if elecc == "A":
        print("Quieres moverte, pero tus piernas estan heridas y sientes un pequeño mareo")
    elif elecc == "B":
        print("Estas en un hoyo y no observas un lugar para esconderte")
    elif elecc == "C":
        print("Buscas dentro de la mochila y encuentras medicina, vendas, comida, agua, una pistola y dos cuchillos")


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
        print("Quieres moverte, pero tus piernas estan heridas y sientes un pequeño mareo")
    elif elecc == "B":
       print("Esta todo oscuro y no observas un lugar para esconderte")
    elif elecc == "C":
        print("Quieres salir del hoyo con tus propias manos pero resbalas y caes de nuevo")
        print("Hiciste mucho ruido, los rugidos se acercan a ti...")
        print(" Tratas de correr, pero sientes un mordisco en la pierna y otro en la espalda, gritas")
        print("Sientes cómo la vida se te escapa a mordiscos...")
        import sys
        sys.exit()
    if elecc=="A" or elecc=="B":
      print("Sientes que tienes algo en la espalda, es una mochila")
      print("Buscas dentro de la mochila y encuentras botiquín de primeros auxilios, comida, agua, una pistola y dos cuchillos")

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
        import sys
        sys.exit()

elif elecc == "B":
        print("Disparas en dirección de los ruidos y escuchas un aullido de dolor")
        print("Te sientes aliviado de deshacerte de esa criatura")
        print("Pero hiciste mucho ruido con el arma, más rugidos se acercan a ti...")
        print(" Tratas de correr disparando, pero sientes un mordisco en la pierna y otro en la espalda y gritas")
        print("Sientes cómo se ta va la vida a mordiscos...")
        import sys
        sys.exit()
elif elecc == "C":
        print("Eres paciente y esperas a que se vayan los ruidos")
        print("Entonces después de unos minutos estas sumergido en un profundo y agradable silencio sin rugidos estremecedores")  



