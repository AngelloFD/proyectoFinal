import tkinter
import os
import turtle
from tkinter import StringVar
from tkinter import messagebox


# menu.destroy()

ventana=tkinter.Tk()
ventana.geometry("400x200")
ventana.title("Juego PONG")

Nombre1=StringVar()
Nombre2=StringVar()
Color1=StringVar()
Color2=StringVar()



listaJugadores=list()
jugador={}



def iniciarJuego():
    print("Inciando juego.... ")
    ventana.destroy()




etiquetaUsuario1= tkinter.Label(ventana, text="Ingrese nombre jugador 1")
textUsuario1= tkinter.Entry(ventana,textvariable=Nombre1,font="Verdana 12")
etiquetaColor1=tkinter.Label(ventana,text="Color")
textColor1=tkinter.Entry(ventana,textvariable=Color1,font="Verdana 12")




etiquetaUsuario2= tkinter.Label(ventana, text="Ingrese nombre jugador 2")
textUsuario2= tkinter.Entry(ventana,textvariable=Nombre2,font="Verdana 12")
etiquetaColor2=tkinter.Label(ventana,text="Color")
textColor2=tkinter.Entry(ventana,textvariable=Color2,font="Verdana 12")

BotonJugar=tkinter.Button(ventana,text="Jugar",command=iniciarJuego)

etiquetaUsuario1.grid(row=0,column=0,padx=10,pady=10)
textUsuario1.grid(row=0,column=1)
etiquetaColor1.grid(row=1,column=0)
textColor1.grid(row=1,column=1)




etiquetaUsuario2.grid(row=2,column=0,padx=10,pady=10)
textUsuario2.grid(row=2,column=1)
etiquetaColor2.grid(row=3,column=0)
textColor2.grid(row=3,column=1)

BotonJugar.grid(row=5,column=1,padx=10,pady=10)

ventana.mainloop()




#-------------------------------------------------------------------------

#Ventana
wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)                     # para que el juego se ejecute fluidamente



#Marcador
marcadorA = 0
marcadorB = 0

#JugadorA
jugadorA= turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color(Color1.get())
jugadorA.penup()    #borra linea de huella al mover objetos
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1) #dar fomma multiplicar largo y ancho

#JugadorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color(Color2.get())
jugadorB.penup()
jugadorB.goto(350, 0)    #obtener la posicion
jugadorB.shapesize(stretch_wid=5, stretch_len=1)


#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

#Modificar estas variables para cambiar la velocidad de la pelota
pelota.dx = 1
pelota.dy = 1


#Pen para dibujar el marcador.
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()     #ocultar objeto flecha
pen.goto(0, 260)
pen.write("Jugador A: 0               jugadorB: 0", align="center", font=("Courier", 25, "normal"))


is_paused=False

#Funciones
def jugadorA_up():
        y = jugadorA.ycor()
        y += 20
        if y<270:
                jugadorA.sety(y)

def jugadorA_down():
        y = jugadorA.ycor()
        y -= 20
        if y>-250:
                jugadorA.sety(y)

def jugadorB_up():
        y = jugadorB.ycor()
        y += 20
        if y<270:
                jugadorB.sety(y)

def jugadorB_down():
        y = jugadorB.ycor()
        y -= 20
        if y>-250:
                jugadorB.sety(y)



def guardarPartida():
    global marcadorA
    global marcadorB
    valor=messagebox.askquestion("Guardar","¿Guardar Partida?")
    if valor == "yes":
        MarcadorA=str(marcadorA)
        MarcadorB=str(marcadorB)
        jugador={}
        jugador["Nombre1"]=Nombre1.get()
        jugador["P1"]=MarcadorA
        jugador["P2"]=MarcadorB
        jugador["Nombre2"]=Nombre2.get()
        listaJugadores.append(jugador)
        guardarArchivo()
        messagebox.showinfo("Guardar","Registro correcto")
   

def listarPartidas():
    for item in listaJugadores:
        print(item["Nombre1"],"-",item["P1"],"-",item["P2"],"-",item["Nombre2"])
    
        


def guardarArchivo():
    archivoju=open("jugadores.txt","w")
    for item in listaJugadores:
        linea=(item["Nombre1"] + ";" + item["P1"] + ";" + item["P2"] + ";" + item["Nombre2"])
        linea=linea.strip()
        archivoju.write(linea + "\n")
    archivoju.close()


def cargarDatosArchivo():
    archivoju=open("jugadores.txt","r")
    for item in archivoju:
        lista=item.split(";")
        jugador={}
        jugador["Nombre1"]=lista[0]
        jugador["P1"]=lista[1]
        jugador["P2"]=lista[2]
        jugador["Nombre2"]=lista[3]

        listaJugadores.append(jugador)
    archivoju.close()


def reanudar_Juego():
    global is_paused
    if is_paused==True:
        is_paused=False
        ventana2.destroy()

def terminar_Juego():
    ventana2.destroy()
    wn.update()
    turtle.bye()




def opciones_Juego():
    global is_paused
    global ventana2
    if is_paused==True:
        is_paused=False
    else:
        is_paused=True
        ventana2=tkinter.Tk()
        ventana2.geometry("250x200")
        ventana2.title("Opciones Juego")
        buttonReanudar=tkinter.Button(ventana2,text="Reanudar",command=reanudar_Juego)
        buttonguardarpar=tkinter.Button(ventana2,text="Guardar Partida",command=guardarPartida)
        buttonlistarpar=tkinter.Button(ventana2,text="Listar Partidas",command=listarPartidas)
        buttonTerminar=tkinter.Button(ventana2,text="Terminar",command=terminar_Juego)


        buttonReanudar.grid(row=0,column=0,padx=80,pady=10)
        buttonguardarpar.grid(row=1,column=0,padx=80,pady=10)
        buttonlistarpar.grid(row=2,column=0,padx=80,pady=10)
        buttonTerminar.grid(row=3,column=0,padx=80,pady=10)

        

        
cargarDatosArchivo()

#Teclado
wn.listen()          #para que reciba ordenes
wn.onkeypress(jugadorA_up, "w")      # cuando presiones la tecla w llama funcion subir
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")
wn.onkeypress(opciones_Juego, "p")


while True:
    if not is_paused:
            wn.update()               #actualizar ventana
            pelota.setx(pelota.xcor() + pelota.dx)
            pelota.sety(pelota.ycor() + pelota.dy)

            #Revisa colisiones con los bordes de la ventana
            if pelota.ycor() > 290:
                    pelota.dy *= -1
            if pelota.ycor() < -290:
                    pelota.dy *= -1            #para cambiar direccion

            # Si la pelota sale por la izq o derecha, esta regresa al centro.
            if pelota.xcor() > 390:
                    pelota.goto(0,0)
                    pelota.dx *= -1
                    marcadorA += 1
                    pen.clear()     #limpiar texto escrito y no se sobreescriban los puntos

               
                    pen.write(f"{Nombre1.get()}: {marcadorA}		{Nombre2.get()}: {marcadorB}", align="center", font=("Courier", 25, "normal"))

            if pelota.xcor() < -390:
                    pelota.goto(0,0)
                    pelota.dx *= -1
                    marcadorB += 1
                    pen.clear()
                    #Esta línea de codigo vuelve a pintar el marcador, utilizo "format" de la versión 3.6 en adelante de python.
                    #Si tienes python menor a la versión 3.6 esta parte no te funcionará.
                    pen.write(f"{Nombre1.get()}: {marcadorA}		{Nombre2.get()}: {marcadorB}", align="center", font=("Courier", 25, "normal"))


            #Revisa las colisiones
            if ((pelota.xcor() > 340 and pelota.xcor() < 350)
                            and (pelota.ycor() < jugadorB.ycor() + 50
                            and pelota.ycor() > jugadorB.ycor() - 50)):
                    pelota.dx *= -1

            if ((pelota.xcor() < -340 and pelota.xcor() > -350)
                            and (pelota.ycor() < jugadorA.ycor() + 50
                            and pelota.ycor() > jugadorA.ycor() - 50)):
                    pelota.dx *= -1

    else:
        wn.update()
