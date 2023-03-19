# cSpell: disable
import turtle
import random
import time
import os

# ruta para imagenes
directorio_script = os.path.dirname(__file__)


#ventana
wn = turtle.Screen()
wn.title("REPROBADOS")
wn.setup(width=800,height=600)
wn.tracer(0)
nombre=turtle.textinput("NOM","Cuál es tu nombre:")
if nombre=="":
    nombre="desconosido"

#tortuga de texto de la primera parte
pen=turtle.Turtle()
#tortuga del titulo
tilte=turtle.Turtle()
#tortuga de texto para pasar
pasar=turtle.Turtle()

#tortugas de texto
inventari=turtle.Turtle()
inventari2=turtle.Turtle()
dialogo=turtle.Turtle()


#tortugas visibles
personaje=turtle.Turtle()
poli1=turtle.Turtle()
poli2=turtle.Turtle()
poli3=turtle.Turtle()
poli4=turtle.Turtle()
poli5=turtle.Turtle()
personaje_mini=turtle.Turtle()
persona1=turtle.Turtle()
persona2=turtle.Turtle()
persona3=turtle.Turtle()
persona4=turtle.Turtle()
persona5=turtle.Turtle()
contador1=turtle.Turtle()
contador2=turtle.Turtle()
contador3=turtle.Turtle()
pizarra=turtle.Turtle()
profesor1=turtle.Turtle()
profesor2=turtle.Turtle()
profesor3=turtle.Turtle()
profesor4=turtle.Turtle()
profesor5=turtle.Turtle()

#tortugas cuadro de texto
cuadro_inventario=turtle.Turtle()
cuadro_dialogo=turtle.Turtle()
cuadro_inventario2=turtle.Turtle()

#tortugas para canbiar de parte(tortugas de cambio)
espacio=turtle.Turtle()
tecla1=turtle.Turtle()
tecla2=turtle.Turtle()
tecla3=turtle.Turtle()
tecla4=turtle.Turtle()
tecla5=turtle.Turtle()
tecla6=turtle.Turtle()
tecla7=turtle.Turtle()
tecla8=turtle.Turtle()
tecla9=turtle.Turtle()
tecla0=turtle.Turtle()
teclaa=turtle.Turtle()
teclab=turtle.Turtle()
teclamas=turtle.Turtle()
teclamenos=turtle.Turtle()

#levantar pluma
personaje.penup()
contador1.penup()
contador2.penup()
contador3.penup()
pizarra.penup()
profesor1.penup()
profesor2.penup()
profesor3.penup()
profesor4.penup()
profesor5.penup()

#ubicacion de tortugas
tespa=espacio.xcor()
t1=tecla1.xcor()
t2=tecla2.xcor()
t3=tecla3.xcor()
t4=tecla4.xcor()
t5=tecla5.xcor()
t6=tecla6.xcor()
t7=tecla7.xcor()
t8=tecla8.xcor()
t9=tecla9.xcor()
t0=tecla0.xcor()
ta=teclaa.xcor()
tb=teclab.xcor()
tmenos=teclamenos.xcor()
tmas=teclamas.xcor()
personaje.goto(-360,-260)
contador1.goto(-300,120)
contador2.goto(-280,120)
contador3.goto(-260,120)
pizarra.goto(0,180)

#esconder tortugas
pen.hideturtle()
tilte.hideturtle()
pasar.hideturtle()
inventari.hideturtle()
dialogo.hideturtle()
inventari2.hideturtle()
personaje.hideturtle()
poli1.hideturtle()
poli2.hideturtle()
poli3.hideturtle()
poli4.hideturtle()
poli5.hideturtle()
personaje_mini.hideturtle()
persona1.hideturtle()
persona2.hideturtle()
persona3.hideturtle()
persona4.hideturtle()
persona5.hideturtle()
cuadro_inventario.hideturtle()
cuadro_dialogo.hideturtle()
cuadro_inventario2.hideturtle()
espacio.hideturtle()
tecla1.hideturtle()
tecla2.hideturtle()
tecla3.hideturtle()
tecla4.hideturtle()
tecla5.hideturtle()
tecla6.hideturtle()
tecla7.hideturtle()
tecla8.hideturtle()
tecla9.hideturtle()
tecla0.hideturtle()
teclaa.hideturtle()
teclab.hideturtle()
teclamas.hideturtle()
teclamenos.hideturtle()
contador1.hideturtle()
contador2.hideturtle()
contador3.hideturtle()
pizarra.hideturtle()
profesor1.hideturtle()
profesor2.hideturtle()
profesor3.hideturtle()
profesor4.hideturtle()
profesor5.hideturtle()

#variables
tuto=0
x=0
y=0
z=0
t=0
j=0
tiempo=0
vales=0
acciones=f"Presiona 1 para abrir el mapa\n" \
      f"Presiona 2 para ver el acertijo"
inventario=f"vales: {vales}"
mon=""
moneda=0
cua_tex=0
largo=280
alto=120
xinventario_d=120
yinventario=-290
xinventario_i=-390
puntos=0
y1=random.randint(-280,280)
y2=random.randint(-280,280)
y3=random.randint(-280,280)
y4=random.randint(-280,280)
y5=random.randint(-280,280)
mini=0
color_persona="Blue"
color_personaje="#D810CC"
color_cuadro="yellow"
xdialogo=-400
ydialogo=220
contador=0
maestro_1=0
maestro_2=0
maestro_3=0
maestro_4=0
maestro_5=0

#funcion para configurar cualquier texto de color blanco
def texto(turt):
    turt.speed(0)
    turt.color("white")
    turt.penup()
    turt.hideturtle()

#funcion para configurar el titulo
def titulo(turt):
    turt.speed(0)
    turt.color("white")
    turt.penup()
    turt.hideturtle()
    turt.goto(0,240)

#funcion mensaje de pasar a siguiente
def pas_espacio(turt):
    turt.color("white")
    turt.penup()
    turt.hideturtle()
    turt.goto(0,-60)
    turt.write(f"Presiona espacio para continuar",align="center",font=("Courier",15,"normal"))

#configuracion de tortuga para cambiar de parte
def cambio(turt):
    turt.hideturtle()
    turt.speed(0)
    turt.penup()
    turt.hideturtle()

#configuracion minima de una tortuga
def basico(turt):
    turt.speed(0)
    turt.penup()

#reasignar tortugas a 0
def tortugas():
    espacio.setx(0)
    tecla1.setx(0)
    tecla2.setx(0)
    tecla3.setx(0)
    tecla4.setx(0)
    tecla5.setx(0)
    tecla6.setx(0)
    tecla7.setx(0)
    tecla8.setx(0)
    tecla9.setx(0)
    tecla0.setx(0)
    teclaa.setx(0)
    teclab.setx(0)
    teclamas.setx(0)
    teclamenos.setx(0)

#reasignar ubicacion
def teclas():
    tespa=0
    t1=0
    t2=0
    t3=0
    t4=0
    t5=0
    t6=0
    t7=0
    t8=0
    t9=0
    t0=0
    ta=0
    tb=0
    tmas=0
    tmenos=0
    return tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos

#ejecutar la funcion sig en las tortugas de cambio
cambio(espacio)
cambio(tecla1)
cambio(tecla2)
cambio(tecla3)
cambio(tecla4)
cambio(tecla5)
cambio(tecla6)
cambio(tecla7)
cambio(tecla8)
cambio(tecla9)
cambio(tecla0)
cambio(teclaa)
cambio(teclab)
cambio(teclamas)
cambio(teclamenos)

#lectura de teclas
def esp():
    x=espacio.xcor()
    x+=1
    espacio.setx(x)
def op1():
    x=tecla1.xcor()
    x+=1
    tecla1.setx(x)
def op2():
    x=tecla2.xcor()
    x+=1
    tecla2.setx(x)
def op3():
    x=tecla3.xcor()
    x+=1
    tecla3.setx(x)
def op4():
    x=tecla4.xcor()
    x+=1
    tecla4.setx(x)
def op5():
    x=tecla5.xcor()
    x+=1
    tecla5.setx(x)
def op6():
    x=tecla6.xcor()
    x+=1
    tecla6.setx(x)
def op7():
    x=tecla7.xcor()
    x+=1
    tecla7.setx(x)
def op8():
    x=tecla8.xcor()
    x+=1
    tecla8.setx(x)
def op9():
    x=tecla9.xcor()
    x+=1
    tecla9.setx(x)
def op0():
    x=tecla0.xcor()
    x+=1
    tecla0.setx(x)
def opa():
    x=teclaa.xcor()
    x+=1
    teclaa.setx(x)
def opb():
    x=teclab.xcor()
    x+=1
    teclab.setx(x)
def opmas():
    x=teclamas.xcor()
    x+=1
    teclamas.setx(x)
def opmen():
    x=teclamenos.xcor()
    x+=1
    teclamenos.setx(x)
def arriba():
    y=personaje.ycor()
    y+=20
    personaje.sety(y)
def abajo():
    y=personaje.ycor()
    y-=20
    personaje.sety(y)
def izquierda():
    x=personaje.xcor()
    x-=20
    personaje.setx(x)
def derecha():
    x=personaje.xcor()
    x+=20
    personaje.setx(x)
def arriba_mini():
    y=personaje_mini.ycor()
    y+=20
    personaje_mini.sety(y)
def abajo_mini():
    y=personaje_mini.ycor()
    y-=20
    personaje_mini.sety(y)

wn.listen()
wn.onkeypress(esp,"space")
wn.onkeypress(op1,"1")
wn.onkeypress(op2,"2")
wn.onkeypress(op3,"3")
wn.onkeypress(op4,"4")
wn.onkeypress(op5,"5")
wn.onkeypress(op6,"6")
wn.onkeypress(op7,"7")
wn.onkeypress(op8,"8")
wn.onkeypress(op9,"9")
wn.onkeypress(op0,"0")
wn.onkeypress(opa,"a")
wn.onkeypress(opb,"b")
wn.onkeypress(opmas,"x")
wn.onkeypress(opmen,"z")
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(derecha,"Right")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(arriba_mini,"w")
wn.onkeypress(abajo_mini,"s")

#configurar contador1
contador1.color("green")
contador1.shape("circle")
contador1.shapesize(stretch_len=1,stretch_wid=1)

#configurar contador2
contador2.color("green")
contador2.shape("circle")
contador2.shapesize(stretch_len=1,stretch_wid=1)

#configurar contador3
contador3.color("green")
contador3.shape("circle")
contador3.shapesize(stretch_len=1,stretch_wid=1)

def limites():
    if personaje.xcor()<=-380:
        personaje.setx(-360)
    if personaje.xcor()>=380:
        personaje.setx(360)
    if personaje.ycor()>=280:
        personaje.sety(260)
    if personaje.ycor()<=-280:
        personaje.sety(-260)
def limites_ind():
    if (personaje.xcor()<=360 and personaje.xcor()>=100)and (personaje.ycor()<=-200):
        personaje.sety(-180)
def limites_ini():
    if (personaje.xcor()<=-120) and (personaje.ycor()<=-200):
        personaje.sety(-180)
def limites_ini2():
    if (personaje.xcor()<=300) and (personaje.ycor()<=-200):
        personaje.sety(-180)
def limites_auditorioden():
    if (personaje.xcor()>=-100 and personaje.xcor()<=260) and (personaje.ycor()==-220):
        personaje.sety(-240)
    if (personaje.xcor()>=-100 and personaje.xcor()<=260) and (personaje.ycor()==-200):
        personaje.sety(-180)
    if personaje.xcor()==280 and (personaje.ycor()>=-220 and personaje.ycor()<=-200):
        personaje.setx(300)

    if (personaje.xcor()>=-300 and personaje.xcor()<=280) and (personaje.ycor()==-140):
        personaje.sety(-160)
    if (personaje.xcor()>=-300 and personaje.xcor()<=280) and (personaje.ycor()==-120):
        personaje.sety(-100)
    if personaje.xcor()==300 and (personaje.ycor()>=-140 and personaje.ycor()<=-120):
        personaje.setx(320)
    if personaje.xcor()==-320 and (personaje.ycor()>=-140 and personaje.ycor()<=-120):
        personaje.setx(-340)

    if (personaje.xcor()>=-320 and personaje.xcor()<=260) and (personaje.ycor()==-60):
        personaje.sety(-80)
    if (personaje.xcor()>=-320 and personaje.xcor()<=260) and (personaje.ycor()==-40):
        personaje.sety(-20)
    if personaje.xcor()==280 and (personaje.ycor()>=-60 and personaje.ycor()<=-40):
        personaje.setx(300)
    if personaje.xcor()==-340 and (personaje.ycor()>=-60 and personaje.ycor()<=-40):
        personaje.setx(-360)

    if (personaje.xcor()>=-300 and personaje.xcor()<=280) and (personaje.ycor()==20):
        personaje.sety(0)
    if (personaje.xcor()>=-300 and personaje.xcor()<=280) and (personaje.ycor()==40):
        personaje.sety(60)
    if personaje.xcor()==300 and (personaje.ycor()>=20 and personaje.ycor()<=40):
        personaje.setx(320)
    if personaje.xcor()==-320 and (personaje.ycor()>=20 and personaje.ycor()<=40):
        personaje.setx(-340)
def limites_cafeteriaden():
    if (personaje.ycor()==-180) and (personaje.xcor()<=-180 and personaje.xcor()>=-200):
        personaje.sety(-200)
    if (personaje.ycor()==-160) and (personaje.xcor()==-220):
        personaje.setx(-240)
    if (personaje.ycor()==-140) and (personaje.xcor()<=-220 and personaje.xcor()>=-240):
        personaje.sety(-160)
    if (personaje.ycor()<=-100 and personaje.ycor()>=-140) and (personaje.xcor()==-260):
        personaje.setx(-280)
    if (personaje.ycor()==-80) and (personaje.xcor()<=-220 and personaje.xcor()>=-240):
        personaje.sety(-60)
    if (personaje.ycor()<=-40 and personaje.ycor()>=-60) and (personaje.xcor()==-220):
        personaje.setx(-240)
    if (personaje.ycor()==-40) and (personaje.xcor()<=-160 and personaje.xcor()>=-200):
        personaje.sety(-20)
    if (personaje.ycor()==-60) and (personaje.xcor()==-160):
        personaje.setx(-140)
    if (personaje.ycor()==-80) and (personaje.xcor()<=-120 and personaje.xcor()>=-160):
        personaje.sety(-60)
    if (personaje.ycor()<=-100 and personaje.ycor()>=-120) and (personaje.xcor()==-120):
        personaje.setx(-100)
    if (personaje.ycor()==-140) and (personaje.xcor()<=-120 and personaje.xcor()>=-160):
        personaje.sety(-160)
    if (personaje.ycor()<=-160 and personaje.ycor()>=-180) and (personaje.xcor()==-160):
        personaje.setx(-140)


    if (personaje.ycor()<=-180) and (personaje.xcor()==-360):
        personaje.sety(-160)
    if (personaje.ycor()<=-140 and personaje.ycor()>=-180) and (personaje.xcor()==-340):
        personaje.setx(-360)
    if (personaje.ycor()==-140) and (personaje.xcor()<=-300 and personaje.xcor()>=-320):
        personaje.sety(-120)
    if (personaje.ycor()==-160) and (personaje.xcor()==-280):
        personaje.setx(-260)
    if (personaje.ycor()==-180) and (personaje.xcor()<=-260 and personaje.xcor()>=-280):
        personaje.sety(-160)
    if (personaje.ycor()<=-200 and personaje.ycor()>=-220) and (personaje.xcor()==-240):
        personaje.setx(-220)
    if (personaje.ycor()==-240) and (personaje.xcor()<=-240 and personaje.xcor()>=-280):
        personaje.sety(-260)
    if (personaje.ycor()<=-260 and personaje.ycor()>=-280) and (personaje.xcor()<=-280):
        personaje.setx(-260)

    if (personaje.ycor()==-80) and (personaje.xcor()<=-320 and personaje.xcor()>=-340):
        personaje.sety(-100)
    if (personaje.ycor()==-80) and (personaje.xcor()==-340):
        personaje.setx(-360)
    if (personaje.ycor()<=0 and personaje.ycor()>=-60) and (personaje.xcor()==-360):
        personaje.sety(-80)
    if (personaje.ycor()<=60 and personaje.ycor()>=0) and (personaje.xcor()==-360):
        personaje.sety(80)
    if (personaje.ycor()==60) and (personaje.xcor()<=-300 and personaje.xcor()>=-340):
        personaje.sety(80)
    if (personaje.ycor()==40) and (personaje.xcor()==-300):
        personaje.setx(-280)
    if (personaje.ycor()==20) and (personaje.xcor()<=-260 and personaje.xcor()>=-300):
        personaje.sety(40)
    if (personaje.ycor()<=0 and personaje.ycor()>=-20) and (personaje.xcor()==-260):
        personaje.setx(-240)
    if (personaje.ycor()==-40) and (personaje.xcor()<=-260 and personaje.xcor()>=-300):
        personaje.sety(-60)
    if (personaje.ycor()<=-60 and personaje.ycor()>=-80) and (personaje.xcor()==-300):
        personaje.setx(-280)

    if (personaje.ycor()==-160) and (personaje.xcor()<=140 and personaje.xcor()>=120):
        personaje.sety(-180)
    if (personaje.ycor()==-140) and (personaje.xcor()==100):
        personaje.setx(80)
    if (personaje.ycor()==-120) and (personaje.xcor()<=100 and personaje.xcor()>=60):
        personaje.sety(-140)
    if (personaje.ycor()<=-80 and personaje.ycor()>=-100) and (personaje.xcor()==60):
        personaje.setx(40)
    if (personaje.ycor()==-80) and (personaje.xcor()<=100 and personaje.xcor()>=80):
        personaje.sety(-60)
    if (personaje.ycor()<=-40 and personaje.ycor()>=-60) and (personaje.xcor()==100):
        personaje.setx(80)
    if (personaje.ycor()==-20) and (personaje.xcor()<=160 and personaje.xcor()>=120):
        personaje.sety(0)
    if (personaje.ycor()==-40) and (personaje.xcor()==160):
        personaje.setx(180)
    if (personaje.ycor()==-60) and (personaje.xcor()<=180 and personaje.xcor()>=160):
        personaje.sety(-40)
    if (personaje.ycor()<=-80 and personaje.ycor()>=-100) and (personaje.xcor()==200):
        personaje.setx(220)
    if (personaje.ycor()==-120) and (personaje.xcor()<=200 and personaje.xcor()>=160):
        personaje.sety(-140)
    if (personaje.ycor()<=-140 and personaje.ycor()>=-160) and (personaje.xcor()==160):
        personaje.setx(180)

    if (personaje.ycor()==-180) and (personaje.xcor()==220):
        personaje.setx(200)
    if (personaje.ycor()==-180) and (personaje.xcor()<=260 and personaje.xcor()>=240):
        personaje.sety(-160)
    if (personaje.ycor()==-160) and (personaje.xcor()==260):
        personaje.setx(240)
    if (personaje.ycor()==-140) and (personaje.xcor()==280):
        personaje.setx(260)
    if (personaje.ycor()==-120) and (personaje.xcor()<=320 and personaje.xcor()>=280):
        personaje.sety(-100)
    if (personaje.ycor()==-140) and (personaje.xcor()==320):
        personaje.setx(340)
    if (personaje.ycor()==-60) and (personaje.xcor()<=180 and personaje.xcor()>=160):
        personaje.sety(-40)
    if (personaje.ycor()<=-160 and personaje.ycor()>=-180) and (personaje.xcor()<=360 and personaje.xcor()>=340):
        personaje.goto(360,-160)

    if (personaje.ycor()==-80) and (personaje.xcor()<=300 and personaje.xcor()>=280):
        personaje.sety(-100)
    if (personaje.ycor()==-60) and (personaje.xcor()==280):
        personaje.setx(260)
    if (personaje.ycor()==-40) and (personaje.xcor()<=280 and personaje.xcor()>=240):
        personaje.sety(-60)
    if (personaje.ycor()<=0 and personaje.ycor()>=-20) and (personaje.xcor()==220):
        personaje.setx(200)
    if (personaje.ycor()==20) and (personaje.xcor()<=260 and personaje.xcor()>=240):
        personaje.sety(40)
    if (personaje.ycor()==40) and (personaje.xcor()==260):
        personaje.setx(240)
    if (personaje.ycor()==60) and (personaje.xcor()==280):
        personaje.setx(260)
    if (personaje.ycor()==60) and (personaje.xcor()<=320 and personaje.xcor()>=300):
        personaje.sety(80)
    if (personaje.ycor()==40) and (personaje.xcor()==340):
        personaje.setx(360)
    if (personaje.ycor()==20) and (personaje.xcor()<=360 and personaje.xcor()>=340):
        personaje.sety(40)
    if (personaje.ycor()==-40) and (personaje.xcor()<=360 and personaje.xcor()>=340):
        personaje.sety(-60)
    if (personaje.ycor()<=-40 and personaje.ycor()>=-80) and (personaje.xcor()==320):
        personaje.setx(340)

    if (personaje.ycor()>=180) and (personaje.xcor()<=140):
        personaje.sety(160)
    if (personaje.ycor()>=200) and (personaje.xcor()<=160):
        personaje.setx(180)

    if (personaje.ycor()<=260 and personaje.ycor()>=240) and (personaje.xcor()==200):
        personaje.setx(180)
    if (personaje.ycor()>=240) and (personaje.xcor()<=320 and personaje.xcor()>=220):
        personaje.sety(220)
    if (personaje.ycor()<=260 and personaje.ycor()>=240) and (personaje.xcor()==340):
        personaje.setx(360)
def limites_fuente():
    if (personaje.xcor()<=120 and personaje.xcor()>=0) and (personaje.ycor()==-180):
        personaje.goto(140,-180)
    if (personaje.xcor()<=140 and personaje.xcor()>=0) and (personaje.ycor()==-160):
        personaje.goto(140,-180)
    if (personaje.xcor()<=160 and personaje.xcor()>=0) and (personaje.ycor()==-140):
        personaje.goto(180,-140)
    if (personaje.xcor()<=180 and personaje.xcor()>=0) and (personaje.ycor()==-120):
        personaje.goto(180,-140)
    if (personaje.xcor()<=200 and personaje.xcor()>=0) and (personaje.ycor()==-100):
        personaje.goto(220,-100)
    if (personaje.xcor()<=200 and personaje.xcor()>=0) and (personaje.ycor()==-80):
        personaje.goto(220,-80)
    if (personaje.xcor()<=200 and personaje.xcor()>=0) and (personaje.ycor()==-60):
        personaje.goto(220,-60)
    if (personaje.xcor()<=220 and personaje.xcor()>=0) and (personaje.ycor()==-40):
        personaje.goto(240,-40)
    if (personaje.xcor()<=220 and personaje.xcor()>=0) and (personaje.ycor()==-20):
        personaje.goto(240,-20)
    if (personaje.xcor()<=220 and personaje.xcor()>=0) and (personaje.ycor()==0):
        personaje.goto(240,0)
    if (personaje.xcor()<=220 and personaje.xcor()>=0) and (personaje.ycor()==20):
        personaje.goto(240,20)
    if (personaje.xcor()<=220 and personaje.xcor()>=0) and (personaje.ycor()==40):
        personaje.goto(240,40)
    if (personaje.xcor()<=200 and personaje.xcor()>=0) and (personaje.ycor()==60):
        personaje.goto(220,60)
    if (personaje.xcor()<=200 and personaje.xcor()>=0) and (personaje.ycor()==80):
        personaje.goto(220,80)
    if (personaje.xcor()<=200 and personaje.xcor()>=0) and (personaje.ycor()==100):
        personaje.goto(200,120)
    if (personaje.xcor()<=180 and personaje.xcor()>=0) and (personaje.ycor()==120):
        personaje.goto(200,120)
    if (personaje.xcor()<=180 and personaje.xcor()>=0) and (personaje.ycor()==140):
        personaje.goto(180,160)
    if (personaje.xcor()==160) and (personaje.ycor()==160):
        personaje.goto(180,160)
    if (personaje.xcor()==140) and (personaje.ycor()<=180 and personaje.ycor()>=0):
        personaje.goto(160,180)
    if (personaje.xcor()==120) and (personaje.ycor()<=180 and personaje.ycor()>=0):
        personaje.goto(120,200)
    if (personaje.xcor()==100) and (personaje.ycor()<=200 and personaje.ycor()>=0):
        personaje.goto(100,220)
    if (personaje.xcor()==80) and (personaje.ycor()<=200 and personaje.ycor()>=0):
        personaje.goto(80,220)
    if (personaje.xcor()==60) and (personaje.ycor()<=220 and personaje.ycor()>=0):
        personaje.goto(60,240)
    if (personaje.xcor()==40) and (personaje.ycor()<=220 and personaje.ycor()>=0):
        personaje.goto(40,240)
    if (personaje.xcor()==20) and (personaje.ycor()<=220 and personaje.ycor()>=0):
        personaje.goto(20,240)
    if (personaje.xcor()==0) and (personaje.ycor()<=220 and personaje.ycor()>=0):
        personaje.goto(0,240)
    if (personaje.xcor()==-20) and (personaje.ycor()<=220 and personaje.ycor()>=0):
        personaje.goto(-20,240)
    if (personaje.xcor()==-40) and (personaje.ycor()<=220 and personaje.ycor()>=0):
        personaje.goto(-40,240)
    if (personaje.xcor()==-60) and (personaje.ycor()<=220 and personaje.ycor()>=0):
        personaje.goto(-60,240)
    if (personaje.xcor()==-80) and (personaje.ycor()<=220 and personaje.ycor()>=0):
        personaje.goto(-80,240)
    if (personaje.xcor()==-100) and (personaje.ycor()<=200 and personaje.ycor()>=0):
        personaje.goto(-100,220)
    if (personaje.xcor()==-120) and (personaje.ycor()<=200 and personaje.ycor()>=0):
        personaje.goto(-140,200)
    if (personaje.xcor()==-140) and (personaje.ycor()<=180 and personaje.ycor()>=0):
        personaje.goto(-140,200)
    if (personaje.xcor()==-160) and (personaje.ycor()<=180 and personaje.ycor()>=0):
        personaje.goto(-180,180)
    if (personaje.xcor()>=-180 and personaje.xcor()<=0) and (personaje.ycor()==160):
        personaje.goto(-180,180)
    if (personaje.xcor()>=-180 and personaje.xcor()<=0) and (personaje.ycor()==140):
        personaje.goto(-200,140)
    if (personaje.xcor()>=-200 and personaje.xcor()<=0) and (personaje.ycor()==120):
        personaje.goto(-200,140)
    if (personaje.xcor()>=-200 and personaje.xcor()<=0) and (personaje.ycor()==100):
        personaje.goto(-220,100)
    if (personaje.xcor()>=-220 and personaje.xcor()<=0) and (personaje.ycor()==80):
        personaje.goto(-240,80)
    if (personaje.xcor()>=-220 and personaje.xcor()<=0) and (personaje.ycor()==60):
        personaje.goto(-240,60)
    if (personaje.xcor()>=-220 and personaje.xcor()<=0) and (personaje.ycor()==40):
        personaje.goto(-240,40)
    if (personaje.xcor()>=-220 and personaje.xcor()<=0) and (personaje.ycor()==20):
        personaje.goto(-240,20)
    if (personaje.xcor()>=-220 and personaje.xcor()<=0) and (personaje.ycor()==-60):
        personaje.goto(-240,-60)
    if (personaje.xcor()>=-220 and personaje.xcor()<=0) and (personaje.ycor()==-80):
        personaje.goto(-240,-80)
    if (personaje.xcor()>=-200 and personaje.xcor()<=0) and (personaje.ycor()==-100):
        personaje.goto(-220,-100)
    if (personaje.xcor()>=-200 and personaje.xcor()<=0) and (personaje.ycor()==-120):
        personaje.goto(-200,-140)
    if (personaje.xcor()>=-180 and personaje.xcor()<=0) and (personaje.ycor()==-140):
        personaje.goto(-200,-140)
    if (personaje.xcor()==-160) and (personaje.ycor()==-160):
        personaje.goto(-160,-180)
    if (personaje.xcor()==-140) and (personaje.ycor()>=-180 and personaje.ycor()<=0):
        personaje.goto(-160,-180)
    if (personaje.xcor()==-120) and (personaje.ycor()>=-200 and personaje.ycor()<=0):
        personaje.goto(-120,-220)
    if (personaje.xcor()==-100) and (personaje.ycor()>=-200 and personaje.ycor()<=0):
        personaje.goto(-100,-220)
    if (personaje.xcor()==-80) and (personaje.ycor()>=-200 and personaje.ycor()<=0):
        personaje.goto(-80,-220)
    if (personaje.xcor()==-60) and (personaje.ycor()>=-220 and personaje.ycor()<=0):
        personaje.goto(-60,-240)
    if (personaje.xcor()==-40) and (personaje.ycor()>=-220 and personaje.ycor()<=0):
        personaje.goto(-40,-240)
    if (personaje.xcor()==-20) and (personaje.ycor()>=-220 and personaje.ycor()<=0):
        personaje.goto(-20,-240)
    if (personaje.xcor()==0) and (personaje.ycor()>=-220 and personaje.ycor()<=0):
        personaje.goto(0,-240)
def limite_cuadro():
    if (personaje.xcor()<=400) and (personaje.ycor()>=220):
        personaje.sety(200)
def tiempoje(x):
    y=x/91.03
    h=int(y/3600)
    m=int((y%3600)/60)
    s=int(((y%3600)%60))
    ti=f"horas:{h} minutos:{m} segudos:{s}"
    return ti

#introduccion(intro)
def pantalla_inicio():

    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pen.goto(-390,-20)
    pen.write(f"        Hola {nombre} deja te recuerdo lo que está pasando.\n\n"
              f"Queda una semana para que el semestre termine en ITESA, tu\n"
              f"universidad, durante el semestre no hiciste nada y vas a reprobar\n"
              f"todo, si repruebas una materia tus papás te van a sacar de la\n"
              f"escuela, tienes que encontrar la manera de no reprobar.",font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write(f"REPROBADOS",align="center",font=("Courier",24,"normal"))
    pas_espacio(pasar)

#narra la historia de los vales(historia)
def pantalla_2():

    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pen.goto(-390,-20)
    pen.write(f"Pensando una manera para pasar recuerdas la leyenda de los vales\n"
              f"dorados, la leyenda dice que hay 5 vales en total y si los\n"
              f"encuentras, los puedes cambiar con los profesores y estos\n"
              f"automáticamente te pondrán 100, para encontrar el primero tienes\n"
              f"que resolver el acertijo:",font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#el primer acertijo(a1)
def acertijo1():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'“Si el primer vale quieres encontrar te debes aprender a relajar\n'
              f'y tu mente dejar volar, el árbol que jamás se va a enderezar te\n'
              f'puede ayudar”',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#el mapa completo
def mapa():
    wn.bgpic(os.path.join(directorio_script, "mapa1.gif"))

#tutorial
def tutorial():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pen.goto(-390,-20)
    pen.write(f"Utiliza las flechas para desplazarte y acércate a los objetos\n"
              f"para interactuar con ellos.\n",font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))
    pas_espacio(pasar)

#cancha con 0 vales
def cancha0():
    wn.bgpic(os.path.join(directorio_script, "cancha con arbol.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    basico(personaje)
    personaje.showturtle()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()

#arbol con 0 vales
def arbol0():
    wn.bgpic(os.path.join(directorio_script, "hueco1.gif"))
    if moneda==0:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para abrir la caja\n"
                    f"Presiona 4 para ver la moneda\n",font=("Courier",9,"normal"))
    elif moneda==1:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para abrir la caja\n"
                    f"{mon}",font=("Courier",9,"normal"))

#biblioteca con 0 vales
def biblio0():
    wn.bgpic(os.path.join(directorio_script, "biblioteca1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#fuente con 0 vales
def fuente0():
    wn.bgpic(os.path.join(directorio_script, "fuente0.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(60,-240)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

def ocupado():
    texto(dialogo)
    dialogo.goto(xdialogo+20,ydialogo)
    dialogo.color("black")
    dialogo.write(f"Ahora no, estoy ocupado.",font=("Courier",11,"normal"))

#dialogop persona 1 con 0 vales
def dialogo01():
    ocupado()

#dialogop persona 2 con 0 vales
def dialogo02():
    ocupado()

#dialogop persona 3 con 0 vales
def dialogo03():
    texto(dialogo)
    dialogo.goto(xdialogo+20,ydialogo)
    dialogo.color("black")
    dialogo.write(f"Te ves cansado, deberías ir a las canchas y descansar en el árbol que tiene un hoyo,\n"
                  f"es muy cómodo.",font=("Courier",11,"normal"))

#dialogop persona 4 con 0 vales
def dialogo04():
    ocupado()

#dialogop persona 5 con 0 vales
def dialogo05():
    ocupado()

#auditorio con 0 vales
def auditorio0():
    wn.bgpic(os.path.join(directorio_script, "auditorio1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{mon}",font=("Courier",9,"normal"))

#auditorio por dentro con 0 vales
def auditorio_den0():
    wn.bgpic(os.path.join(directorio_script, "auditorioDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_i,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ini()
    limites_auditorioden()

#cafeteria con 0 vales
def cafeteria0():
    wn.bgpic(os.path.join(directorio_script, "cafeteria1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{mon}",font=("Courier",9,"normal"))

#cafeteria por dentro con 0 vales
def cafeteria_den0():
    wn.bgpic(os.path.join(directorio_script, "cafeteriaDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_cafeteriaden()

#vale dorado
def vale():
    wn.bgpic(os.path.join(directorio_script, "valedorado1.gif"))
    pasar.goto(0,-140)
    pasar.color("white")
    pasar.penup()
    pasar.hideturtle()
    pasar.write(f"presioana espacio para continuar",align="center",font=("Courier",15,"normal"))

#caja
def caja():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'Dentro de la caja también encuentras otra pista que dice:\n',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#moneda
def moneda_n():
    wn.bgpic(os.path.join(directorio_script, "moneda1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_i,yinventario)
    inventari.write(f"Presiona 1 para quedártela\n"
                    f"Presiona 2 para regresarla\n"
                    f"{mon}",font=("Courier",9,"normal"))

#el segundo acertijo(a2)
def acertijo2():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'“Dirígete a la exposición de cuadros dentro de la biblioteca y\n'
              f'detrás del cuadro del director encontrarás el siguiente vale”\n',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#cancha con 1 vales
def cancha1():
    wn.bgpic(os.path.join(directorio_script, "cancha con arbol.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    basico(personaje)
    personaje.showturtle()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()

#arbol con 1 vales
def arbol1():
    wn.bgpic(os.path.join(directorio_script, "hueco1.gif"))
    inventari.goto(xinventario_d,yinventario)
    if moneda==0:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para ver la moneda\n"
                    f"{inventario}",font=("Courier",9,"normal"))
    elif moneda==1:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#biblioteca con 1 vales
def biblio1():
    wn.bgpic(os.path.join(directorio_script, "biblioteca1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para acercarte a la ventana\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#fuente con 1 vales
def fuente1():
    wn.bgpic(os.path.join(directorio_script, "fuente0.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(60,-240)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#dialogop persona 1 con 1 vales
def dialogo11():
    ocupado()

#dialogop persona 2 con 1 vales
def dialogo12():
    texto(dialogo)
    dialogo.goto(xdialogo+20,ydialogo)
    dialogo.color("black")
    dialogo.write(f"Ya viste la exposición de cuadros, es increíble.",font=("Courier",11,"normal"))

#dialogop persona 3 con 1 vales
def dialogo13():
    ocupado()

#dialogop persona 4 con 1 vales
def dialogo14():
    ocupado()

#dialogop persona 5 con 1 vales
def dialogo15():
    ocupado()

#auditorio con 1 vales
def auditorio1():
    wn.bgpic(os.path.join(directorio_script, "auditorio1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#auditorio por dentro con 1 vales
def auditorio_den1():
    wn.bgpic(os.path.join(directorio_script, "auditorioDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_i,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ini()
    limites_auditorioden()

#cafeteria con 1 vales
def cafeteria1():
    wn.bgpic(os.path.join(directorio_script, "cafeteria1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#cafeteria por dentro con 1 vales
def cafeteria_den1():
    wn.bgpic(os.path.join(directorio_script, "cafeteriaDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_cafeteriaden()

#ventana biblioteca
def ventana():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'Ves que la ventana esta abierta y entras pero ves que está\n'
              f'repleto de guardias por lo que los tienes que esquivar.',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#tutorial de polis
def tutorial_polis():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'Utiliza la w para subir y s para bajar al personaje.\n'
              f'Que no te toque los guardias.',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#configuracion de polis
wn.bgcolor("black")

basico(personaje_mini)
personaje_mini.shape("circle")
personaje_mini.color(color_personaje)
personaje_mini.goto(-350,0)
personaje_mini.shapesize(stretch_wid=2, stretch_len=2)


basico(poli1)
poli1.shape("square")
poli1.shapesize(stretch_wid=2, stretch_len=2)
poli1.color("blue")
poli1.dx=3

basico(poli2)
poli2.shape("square")
poli2.shapesize(stretch_wid=2, stretch_len=2)
poli2.color("blue")
poli2.dx=3

basico(poli3)
poli3.shape("square")
poli3.shapesize(stretch_wid=2, stretch_len=2)
poli3.color("blue")
poli3.dx=3

basico(poli4)
poli4.shape("square")
poli4.shapesize(stretch_wid=2, stretch_len=2)
poli4.color("blue")
poli4.dx=3

basico(poli5)
poli5.shape("square")
poli5.shapesize(stretch_wid=2, stretch_len=2)
poli5.color("blue")
poli5.dx=3


#cuadro del dire 1
def cuadro_dire1():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-370,-20)
    pen.write(f'Llegas al cuadro del director y le das la vuelta',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#cuadro del dire 2
def cuadro_dire2():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'Junto al vale esta otra pista, pero antes de leerla sales de la\n'
              f'biblioteca sin que te vean, una ves afuera lees el acertijo\n'
              f'que dice:',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#el tercer acertijo(a3)
def acertijo3():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'“Donde el agua te dice la hora debes esperar que la sombra\n'
              f'descanse a las C y la piedra indicada debes escoger”\n',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#cancha con 2 vales
def cancha2():
    wn.bgpic(os.path.join(directorio_script, "cancha con arbol.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    basico(personaje)
    personaje.showturtle()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()

#biblioteca con 2 vales
def biblio2():
    wn.bgpic(os.path.join(directorio_script, "biblioteca1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#fuente con 2 vales
def fuente2():
    wn.bgpic(os.path.join(directorio_script, "fuente0.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som1
def fuente2_1():
    wn.bgpic(os.path.join(directorio_script, "fuente1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som2
def fuente2_2():
    wn.bgpic(os.path.join(directorio_script, "fuente2.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som3
def fuente2_3():
    wn.bgpic(os.path.join(directorio_script, "fuente3.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som4
def fuente2_4():
    wn.bgpic(os.path.join(directorio_script, "fuente4.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som5
def fuente2_5():
    wn.bgpic(os.path.join(directorio_script, "fuente5.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som6
def fuente2_6():
    wn.bgpic(os.path.join(directorio_script, "fuente6.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som7
def fuente2_7():
    wn.bgpic(os.path.join(directorio_script, "fuente7.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som8
def fuente2_8():
    wn.bgpic(os.path.join(directorio_script, "fuente8.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som9
def fuente2_9():
    wn.bgpic(os.path.join(directorio_script, "fuente9.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som10
def fuente2_10():
    wn.bgpic(os.path.join(directorio_script, "fuente10.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som11
def fuente2_11():
    wn.bgpic(os.path.join(directorio_script, "fuente11.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#fuente som12
def fuente2_12():
    wn.bgpic(os.path.join(directorio_script, "fuente12.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona a para abrir el mapa\n"
                    f"Presiona b para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    texto(inventari2)
    inventari2.color("black")
    inventari2.goto(xinventario_i,yinventario)
    inventari2.write(f"Presiona los números para cambiar la hora\n"
                     f"Presiona 0 para las 10\n"
                     f"Presiona x para las 11\n"
                     f"Presiona z para las 12",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_ini2()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(360,0)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#ladrillo1
def ladrillo1():
    wn.bgpic(os.path.join(directorio_script, "piedrasuelta1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para regrsar a la fuente\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para mover el ladrillo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#ladrillo2
def ladrillo2():
    wn.bgpic(os.path.join(directorio_script, "piedrafloja2.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para regrsar el ladrillo\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para agarrar el vale\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#dialogop persona 1 con 2 vales
def dialogo21():
    ocupado()

#dialogop persona 2 con 2 vales ya
def dialogo22():
    ocupado()

#dialogop persona 3 con 2 vales ya
def dialogo23():
    ocupado()

#dialogop persona 4 con 2 vales
def dialogo24():
    ocupado()

#dialogop persona 5 con 2 vales ya
def dialogo25():
    texto(dialogo)
    dialogo.goto(xdialogo+20,ydialogo)
    dialogo.color("black")
    dialogo.write(f"No olvides que en hexadecimal A=10 B=11 C=12 D=13 E=14 F=15",font=("Courier",11,"normal"))

#auditorio con 2 vales
def auditorio2():
    wn.bgpic(os.path.join(directorio_script, "auditorio1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#auditorio por dentro con 2 vales
def auditorio_den2():
    wn.bgpic(os.path.join(directorio_script, "auditorioDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_i,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ini()
    limites_auditorioden()

#cafeteria con 2 vales
def cafeteria2():
    wn.bgpic(os.path.join(directorio_script, "cafeteria1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#cafeteria por dentro con 2 vales
def cafeteria_den2():
    wn.bgpic(os.path.join(directorio_script, "cafeteriaDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_cafeteriaden()

#arbol con 2 vales
def arbol2():
    wn.bgpic(os.path.join(directorio_script, "hueco1.gif"))
    if moneda==0:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para ver la moneda\n"
                    f"{inventario}",font=("Courier",9,"normal"))
    elif moneda==1:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#hueco
def hueco():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'Junto al vale también encuentras otra pista que dice:\n',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#el cuarto acertijo(a4)
def acertijo4():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'“Todos ven lo que hay arriba del escenario, pero lo que pasa\n'
              f'debajo no lo sabe ningún universitario”\n',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#cancha con 3 vales
def cancha3():
    wn.bgpic(os.path.join(directorio_script, "cancha con arbol.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    basico(personaje)
    personaje.showturtle()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()

#biblioteca con 3 vales
def biblio3():
    wn.bgpic(os.path.join(directorio_script, "biblioteca1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#fuente con 3 vales
def fuente3():
    wn.bgpic(os.path.join(directorio_script, "fuente0.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(60,-240)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#dialogop persona 1 con 3 vales
def dialogo31():
    texto(dialogo)
    dialogo.goto(xdialogo+20,ydialogo)
    dialogo.color("black")
    dialogo.write(f"En la parte de atrás del escenario hay unos símbolos raros.",font=("Courier",11,"normal"))

#dialogop persona 2 con 3 vales
def dialogo32():
    ocupado()

#dialogop persona 3 con 3 vales
def dialogo33():
    ocupado()

#dialogop persona 4 con 3 vales
def dialogo34():
    ocupado()

#dialogop persona 5 con 3 vales
def dialogo35():
    ocupado()

#auditorio con 3 vales
def auditorio3():
    wn.bgpic(os.path.join(directorio_script, "auditorio1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#auditorio por dentro con 3 vales
def auditorio_den3():
    wn.bgpic(os.path.join(directorio_script, "auditorioDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_i,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ini()
    limites_auditorioden()

def auditorio_den3_2():
    wn.bgpic(os.path.join(directorio_script, "auditorioDentro2.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_i,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ini()
    limites_auditorioden()

#backstage
def backstage():
    wn.bgpic(os.path.join(directorio_script, "backstage1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para regrsar\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#fondo del auditorio
def fondo():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(120,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limite_cuadro()

    texto(dialogo)
    dialogo.goto(xdialogo+20,ydialogo)
    dialogo.color("black")
    dialogo.write(f"Desplázate para encontrar los objetos.",font=("Courier",11,"normal"))

    pizarra.color("#FFD599")
    pizarra.shape("square")
    pizarra.shapesize(stretch_len=6,stretch_wid=3)

#pizarra1
def pizarra1():
    wn.bgpic(os.path.join(directorio_script, "pizarra1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para agarrar el vale\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#pizarra2
def pizarra2():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'Junto al vale también encuentras otra pista que dice:',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#cafeteria con 3 vales
def cafeteria3():
    wn.bgpic(os.path.join(directorio_script, "cafeteria1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#cafeteria por dentro con 3 vales
def cafeteria_den3():
    wn.bgpic(os.path.join(directorio_script, "cafeteriaDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_cafeteriaden()

#arbol con 3 vales
def arbol3():
    wn.bgpic(os.path.join(directorio_script, "hueco1.gif"))
    if moneda==0:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para ver la moneda\n"
                    f"{inventario}",font=("Courier",9,"normal"))
    elif moneda==1:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#el cuarto acertijo(a5)
def acertijo5():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'“Los estudiantes necesitan comer, si buscas bien con una\n'
              f'moneda la puedes hacer”',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#cancha con 4 vales
def cancha4():
    wn.bgpic(os.path.join(directorio_script, "cancha con arbol.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    basico(personaje)
    personaje.showturtle()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()

#biblioteca con 4 vales
def biblio4():
    wn.bgpic(os.path.join(directorio_script, "biblioteca1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#fuente con 4 vales
def fuente4():
    wn.bgpic(os.path.join(directorio_script, "fuente0.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(60,-240)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#dialogop persona 1 con 4 vales
def dialogo41():
    ocupado()

#dialogop persona 2 con 4 vales
def dialogo42():
    ocupado()

#dialogop persona 3 con 4 vales
def dialogo43():
    ocupado()

#dialogop persona 4 con 4 vales
def dialogo44():
    texto(dialogo)
    dialogo.goto(xdialogo+20,ydialogo)
    dialogo.color("black")
    dialogo.write(f"La maquina expendedora en la cafetería es muy barata, puedes comprar cosas con\n"
                  f"una sola moneda",font=("Courier",11,"normal"))

#dialogop persona 5 con 4 vales
def dialogo45():
    ocupado()

#auditorio con 4 vales
def auditorio4():
    wn.bgpic(os.path.join(directorio_script, "auditorio1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#auditorio por dentro con 4 vales
def auditorio_den4():
    wn.bgpic(os.path.join(directorio_script, "auditorioDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_i,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ini()
    limites_auditorioden()

#cafeteria con 4 vales
def cafeteria4():
    wn.bgpic(os.path.join(directorio_script, "cafeteria1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#cafeteria por dentro con 4 vales
def cafeteria_den4():
    wn.bgpic(os.path.join(directorio_script, "cafeteriaDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_cafeteriaden()

#vendingmachine1
def vendingmachine1():
    wn.bgpic(os.path.join(directorio_script, "vendingmachine1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para Presionar ???\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#vendingmachine2
def vendingmachine2():
    wn.bgpic(os.path.join(directorio_script, "vendingmachine2.gif"))
    if moneda==0:
        inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}",font=("Courier",9,"normal"))
    elif moneda==1:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para insetar moneda\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#arbol con 4 vales
def arbol4():
    wn.bgpic(os.path.join(directorio_script, "hueco1.gif"))
    if moneda==0:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para ver la moneda\n"
                    f"{inventario}",font=("Courier",9,"normal"))
    elif moneda==1:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#entregar
def entrega():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pas_espacio(pasar)
    pen.goto(-390,-20)
    pen.write(f'Has encontrado todos los vales ahora ve a entregárselos a los\n'
              f'profesores que están el auditorio.',font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write("REPROBADOS",align="center",font=("Courier",24,"normal"))

#cancha con 5 vales
def cancha5():
    wn.bgpic(os.path.join(directorio_script, "cancha con arbol.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    basico(personaje)
    personaje.showturtle()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()

#biblioteca con 5 vales
def biblio5():
    wn.bgpic(os.path.join(directorio_script, "biblioteca1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#fuente con 5 vales
def fuente5():
    wn.bgpic(os.path.join(directorio_script, "fuente0.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_fuente()
    persona1.showturtle()
    persona1.penup()
    persona1.color(color_persona)
    persona1.shape("circle")
    persona1.shapesize(stretch_len=2,stretch_wid=2)
    persona1.goto(60,-240)
    persona2.showturtle()
    persona2.penup()
    persona2.color(color_persona)
    persona2.shape("circle")
    persona2.shapesize(stretch_len=2,stretch_wid=2)
    persona2.goto(-360,180)
    persona3.showturtle()
    persona3.penup()
    persona3.color(color_persona)
    persona3.shape("circle")
    persona3.shapesize(stretch_len=2,stretch_wid=2)
    persona3.goto(360,-180)
    persona4.showturtle()
    persona4.penup()
    persona4.color(color_persona)
    persona4.shape("circle")
    persona4.shapesize(stretch_len=2,stretch_wid=2)
    persona4.goto(360,180)
    persona5.showturtle()
    persona5.penup()
    persona5.color(color_persona)
    persona5.shape("circle")
    persona5.shapesize(stretch_len=2,stretch_wid=2)
    persona5.goto(-240,-20)

#dialogop persona 1 con 5 vales
def dialogo51():
    ocupado()

#dialogop persona 2 con 5 vales
def dialogo52():
    ocupado()

#dialogop persona 3 con 5 vales
def dialogo53():
    ocupado()

#dialogop persona 4 con 5 vales
def dialogo54():
    ocupado()

#dialogop persona 5 con 5 vales
def dialogo55():
    ocupado()

#auditorio con 5 vales
def auditorio5():
    wn.bgpic(os.path.join(directorio_script, "auditorio1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#auditorio por dentro con 5 vales
def auditorio_den5():
    wn.bgpic(os.path.join(directorio_script, "auditorioDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_i,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ini()
    limites_auditorioden()

    profesor1.showturtle()
    profesor1.goto(240,200)
    profesor1.color("blue")
    profesor1.shape("circle")
    profesor1.shapesize(stretch_len=2,stretch_wid=2)

    profesor2.showturtle()
    profesor2.goto(160,200)
    profesor2.color("blue")
    profesor2.shape("circle")
    profesor2.shapesize(stretch_len=2,stretch_wid=2)

    profesor3.showturtle()
    profesor3.goto(80,200)
    profesor3.color("blue")
    profesor3.shape("circle")
    profesor3.shapesize(stretch_len=2,stretch_wid=2)

    profesor4.showturtle()
    profesor4.goto(0,200)
    profesor4.color("blue")
    profesor4.shape("circle")
    profesor4.shapesize(stretch_len=2,stretch_wid=2)

    profesor5.showturtle()
    profesor5.goto(-80,200)
    profesor5.color("blue")
    profesor5.shape("circle")
    profesor5.shapesize(stretch_len=2,stretch_wid=2)

#dialogo maestro 1
def maestro1():
    if maestro_1==0:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Entrégame un vale\n"
                      f"Presiona 3 para entregar vale",font=("Courier",11,"normal"))

    if maestro_1==1:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Ya me entregaste un vale",font=("Courier",11,"normal"))

#dialogo maestro 2
def maestro2():
    if maestro_2==0:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Entrégame un vale\n"
                      f"Presiona 3 para entregar vale",font=("Courier",11,"normal"))

    if maestro_2==1:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Ya me entregaste un vale",font=("Courier",11,"normal"))

#dialogo maestro 3
def maestro3():
    if maestro_3==0:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Entrégame un vale\n"
                      f"Presiona 3 para entregar vale",font=("Courier",11,"normal"))

    if maestro_3==1:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Ya me entregaste un vale",font=("Courier",11,"normal"))

#dialogo maestro 4
def maestro4():
    if maestro_4==0:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Entrégame un vale\n"
                      f"Presiona 3 para entregar vale",font=("Courier",11,"normal"))

    if maestro_4==1:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Ya me entregaste un vale",font=("Courier",11,"normal"))

#dialogo maestro 5
def maestro5():
    if maestro_5==0:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Entrégame un vale\n"
                      f"Presiona 3 para entregar vale",font=("Courier",11,"normal"))

    if maestro_5==1:
        texto(dialogo)
        dialogo.goto(xdialogo+20,ydialogo)
        dialogo.color("black")
        dialogo.write(f"Ya me entregaste un vale",font=("Courier",11,"normal"))

#cafeteria con 5 vales
def cafeteria5():
    wn.bgpic(os.path.join(directorio_script, "cafeteria1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"{acciones}\n"
                    f"Presiona 3 para entrar\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#cafeteria por dentro con 5 vales
def cafeteria_den5():
    wn.bgpic(os.path.join(directorio_script, "cafeteriaDentro1.gif"))
    texto(inventari)
    inventari.color("black")
    inventari.goto(xinventario_d,yinventario)
    inventari.write(f"Presiona 1 para salir\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))
    personaje.showturtle()
    personaje.penup()
    personaje.color(color_personaje)
    personaje.shape("circle")
    personaje.shapesize(stretch_len=2,stretch_wid=2)
    limites()
    limites_ind()
    limites_cafeteriaden()

#arbol con 5 vales
def arbol5():
    wn.bgpic(os.path.join(directorio_script, "hueco1.gif"))
    if moneda==0:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"Presiona 3 para ver la moneda\n"
                    f"{inventario}",font=("Courier",9,"normal"))
    elif moneda==1:
        inventari.write(f"Presiona 1 para regrsar a la cancha\n"
                    f"Presiona 2 para ver el acertijo\n"
                    f"{inventario}\n"
                    f"{mon}",font=("Courier",9,"normal"))

#cierre
def cierre():

    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pen.goto(-390,-20)
    pen.write(f"                      Felicidades {nombre}\n\n"
              f"has logrado pasar todas las materias y terminado el semestre,\n"
              f"disfruta tus vacaciones y nos vemos el próximo semestre en ITESA.",font=("Courier",15,"normal"))
    titulo(tilte)
    tilte.write(f"REPROBADOS",align="center",font=("Courier",24,"normal"))
    pas_espacio(pasar)

#fin
def fin():
    wn.bgpic(os.path.join(directorio_script, "fondo negro.gif"))
    texto(pen)
    pen.goto(-10,-80)
    pen.write(f"FIN",align="center",font=("Courier",100,"normal"))
    titulo(tilte)
    tilte.write(f"REPROBADOS",align="center",font=("Courier",24,"normal"))
    pasar.goto(0,-100)
    pasar.color("white")
    pasar.write(f"tu tiempo es {tiempoje(j)}",align="center",font=("Courier",15,"normal"))

#while principal
while True:
    wn.update()

    #ejecuta intro
    if x==0:
        pantalla_inicio()
        if espacio.xcor()!=tespa:
            pen.clear()
            tilte.clear()
            x=1
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #ejecuta historia
    elif x==1:
        pantalla_2()
        if espacio.xcor()!=tespa:
            pen.clear()
            pasar.clear()
            tilte.clear()
            x=2
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #ejecuta a1
    elif x==2:
        personaje.hideturtle()
        persona1.hideturtle()
        persona2.hideturtle()
        persona3.hideturtle()
        persona4.hideturtle()
        cuadro_dialogo.clear()
        dialogo.clear()
        dialogo_cua=0
        cua_tex=0
        persona5.hideturtle()
        acertijo1()
        if espacio.xcor()!=tespa:
            pen.clear()
            tilte.clear()
            pasar.clear()
            x=3
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #parte de juego con a1
    elif x==3:
        #mostrar mapa
        if y==0:
            personaje.hideturtle()
            persona1.hideturtle()
            persona2.hideturtle()
            persona3.hideturtle()
            persona4.hideturtle()
            persona5.hideturtle()
            mapa()
            if tecla1.xcor()!=t1:
                y=1

            elif tecla2.xcor()!=t2:
                y=2

            elif tecla3.xcor()!=t3:
                y=3

            elif tecla4.xcor()!=t4:
                y=4

            elif tecla5.xcor()!=t5:
                y=5
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #canchas
        elif y==1:
            if tuto==0:
                tutorial()
                if espacio.xcor()!=tespa:
                    pen.clear()
                    tilte.clear()
                    pasar.clear()
                    tuto=1
            if tuto==1:
                cancha0()
                if cua_tex==0:
                        cuadro_inventario.penup()
                        cuadro_inventario.color(color_cuadro)
                        cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                        cuadro_inventario.pendown()
                        cuadro_inventario.begin_fill()
                        cuadro_inventario.forward(largo)
                        cuadro_inventario.left(90)
                        cuadro_inventario.forward(alto)
                        cuadro_inventario.left(90)
                        cuadro_inventario.forward(largo)
                        cuadro_inventario.left(90)
                        cuadro_inventario.forward(alto)
                        cuadro_inventario.left(90)
                        cuadro_inventario.end_fill()
                        cua_tex=1

                if t1!=tecla1.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    y=0
                    personaje.goto(-360,-260)
                if t2!=tecla2.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    x=2
                tortugas()
                tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()
                if ((personaje.xcor()>=220 and personaje.xcor()<=360)
                    and (personaje.ycor()>=140 and personaje.ycor()<=260)):
                    y=6
                    inventari.clear()

        #biblioteca
        elif y==2:
                biblio0()
                if cua_tex==0:
                    cuadro_inventario.penup()
                    cuadro_inventario.color(color_cuadro)
                    cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                    cuadro_inventario.pendown()
                    cuadro_inventario.begin_fill()
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.end_fill()
                    cua_tex=1

                if t1!=tecla1.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    y=0
                if t2!=tecla2.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    x=2
                tortugas()
                tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente
        elif y==3:
            if tuto==0:
                tutorial()
                if espacio.xcor()!=tespa:
                    pen.clear()
                    tilte.clear()
                    pasar.clear()
                    tuto=1
            if tuto==1:
                fuente0()
                if cua_tex==0:
                    cuadro_inventario.penup()
                    cuadro_inventario.color(color_cuadro)
                    cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                    cuadro_inventario.pendown()
                    cuadro_inventario.begin_fill()
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.end_fill()
                    cua_tex=1

                if t1!=tecla1.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    personaje.goto(-360,-260)
                    cua_tex=0
                    y=0
                if t2!=tecla2.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cuadro_dialogo.clear()
                    dialogo.clear()
                    dialogo_cua=0
                    cua_tex=0
                    x=2
                if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo01()
                        personaje.goto(-280,-20)
                elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo05()
                        personaje.goto(20,-240)
                elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo04()
                        personaje.goto(-320,180)
                elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo02()
                        personaje.goto(360,-140)
                elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo03()
                        personaje.goto(320,180)
                else:
                    cuadro_dialogo.clear()
                    dialogo.clear()
                    dialogo_cua=0
                tortugas()
                tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #auditorio
        elif y==4:
                auditorio0()
                personaje.hideturtle()
                if cua_tex==0:
                    cuadro_inventario.penup()
                    cuadro_inventario.color(color_cuadro)
                    cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                    cuadro_inventario.pendown()
                    cuadro_inventario.begin_fill()
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.end_fill()
                    cua_tex=1

                if t1!=tecla1.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    y=0
                if t2!=tecla2.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    x=2
                if t3!=tecla3.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    personaje.goto(400,-300)
                    y=9
                tortugas()
                tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria
        elif y==5:
            cafeteria0()
            personaje.hideturtle()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=2
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.goto(-20,-300)
                cua_tex=0
                y=11
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #arbolo
        elif y==6:
            arbol0()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            personaje.hideturtle()
            if t1!=tecla1.xcor():
                inventari.clear()
                y=1
                personaje.goto(200,120)
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=2
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=7
                tval1=tiempoje(tiempo)
                tiempo=0


            if moneda==0:
                if t4!= tecla4.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    y=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #vale
        elif y==7:
            vale()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                y=10
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #moneda
        elif y==8:
            moneda_n()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            if tecla1.xcor()!=t1:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                mon="moneda"
                moneda=1
                inventari.goto(xinventario_d,yinventario)
            if tecla2.xcor()!=t2:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                moneda=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #auditorio dentro
        elif y==9:
            if tuto==0:
                tutorial()
                if espacio.xcor()!=tespa:
                    pen.clear()
                    tilte.clear()
                    pasar.clear()
                    tuto=1
            if tuto==1:
                auditorio_den0()
                if cua_tex==0:
                    cuadro_inventario.penup()
                    cuadro_inventario.color(color_cuadro)
                    cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                    cuadro_inventario.pendown()
                    cuadro_inventario.begin_fill()
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.end_fill()
                    cua_tex=1

                if t1!=tecla1.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    personaje.hideturtle()
                    personaje.goto(-360,-260)
                    y=4
                if t2!=tecla2.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    x=2
                tortugas()
                tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #caja
        elif y==10:
            caja()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                y=6
                x=4
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria dentro
        elif y==11:
            if tuto==0:
                tutorial()
                if espacio.xcor()!=tespa:
                    pen.clear()
                    tilte.clear()
                    pasar.clear()
                    tuto=1
            if tuto==1:
                cafeteria_den0()
                if cua_tex==0:
                    cuadro_inventario.penup()
                    cuadro_inventario.color(color_cuadro)
                    cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                    cuadro_inventario.pendown()
                    cuadro_inventario.begin_fill()
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(largo)
                    cuadro_inventario.left(90)
                    cuadro_inventario.forward(alto)
                    cuadro_inventario.left(90)
                    cuadro_inventario.end_fill()
                    cua_tex=1

                if t1!=tecla1.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    personaje.goto(-360,-260)
                    y=5
                if t2!=tecla2.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    x=2
                tortugas()
                tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #ejecuta a2
    elif x==4:
        acertijo2()
        persona1.hideturtle()
        persona2.hideturtle()
        persona3.hideturtle()
        persona4.hideturtle()
        persona5.hideturtle()
        personaje.hideturtle()
        cuadro_dialogo.clear()
        dialogo.clear()
        dialogo_cua=0
        cua_tex=0
        inventari.clear()

        if espacio.xcor()!=tespa:
            pen.clear()
            tilte.clear()
            pasar.clear()
            vales=1
            inventario=f"vales: {vales}"
            x=5
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #parte de juego con a2
    elif x==5:
        #mostrar mapa
        if y==0:
            personaje.hideturtle()
            persona1.hideturtle()
            persona2.hideturtle()
            persona3.hideturtle()
            persona4.hideturtle()
            persona5.hideturtle()
            mapa()
            if tecla1.xcor()!=t1:
                y=1

            elif tecla2.xcor()!=t2:
                y=2

            elif tecla3.xcor()!=t3:
                y=3

            elif tecla4.xcor()!=t4:
                y=4

            elif tecla5.xcor()!=t5:
                y=5
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #canchas
        elif y==1:
            cancha1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex = 1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.goto(-360,-260)
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=4
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()
            if ((personaje.xcor()>=220 and personaje.xcor()<=360)
                and (personaje.ycor()>=140 and personaje.ycor()<=260)):
                y=6
                inventari.clear()

        #biblioteca
        elif y==2:
            biblio1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=4
            if t3!= tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=9
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente
        elif y==3:
            fuente1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-400,-300)
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=4
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo11()
                        personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo15()
                        personaje.goto(20,-240)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo14()
                        personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo12()
                        personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo13()
                        personaje.goto(320,180)
            else:
                    cuadro_dialogo.clear()
                    dialogo.clear()
                    dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #auditorio
        elif y==4:
            auditorio1()
            personaje.hideturtle()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=4
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(400,-300)
                y=13

            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria
        elif y==5:
            cafeteria1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=4
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.goto(-20,-300)
                cua_tex=0
                y=15
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #arbolo
        elif y==6:
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            personaje.hideturtle()
            arbol1()
            if t1!=tecla1.xcor():
                inventari.clear()
                personaje.goto(200,120)
                y=1
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=4
            if moneda==0:
                if t3!= tecla3.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    y=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #moneda
        elif y==8:
            moneda_n()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            if tecla1.xcor()!=t1:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                mon="moneda"
                moneda=1
                inventari.goto(xinventario_d,yinventario)
            if tecla2.xcor()!=t2:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                moneda=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #ventana
        elif y==9:
            poli1.hideturtle()
            poli2.hideturtle()
            poli3.hideturtle()
            poli4.hideturtle()
            poli5.hideturtle()
            ventana()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                y=10
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #tutorial polis
        elif y==10:
            personaje_mini.hideturtle()
            poli1.hideturtle()
            poli2.hideturtle()
            poli3.hideturtle()
            poli4.hideturtle()
            poli5.hideturtle()
            tutorial_polis()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                poli1.goto(390,y1)
                poli2.goto(390,y2)
                poli3.goto(390,y3)
                poli4.goto(390,y4)
                poli5.goto(390,y5)
                y=11
                mini=1
                puntos=0
                personaje_mini.goto(-350,0)
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #polis
        elif y==11:
            if mini==1:
                if z<10:
                    time.sleep(0)
                    z+=1
                if z==10:
                    time.sleep(.03)
                    z=0

                if puntos<10:

                    personaje_mini.showturtle()
                    poli1.showturtle()
                    poli1.setx(poli1.xcor()-poli1.dx)
                    poli2.showturtle()
                    poli2.setx(poli2.xcor()-poli2.dx)
                    poli3.showturtle()
                    poli3.setx(poli3.xcor()-poli3.dx)
                    poli4.showturtle()
                    poli4.setx(poli4.xcor()-poli4.dx)
                    poli5.showturtle()
                    poli5.setx(poli5.xcor()-poli5.dx)



                    if poli1.xcor()<-390:
                        y1=random.randint(-280,280)
                        poli1.goto(390,y1)
                        y2=random.randint(-280,280)
                        poli2.goto(390,y2)
                        y3=random.randint(-280,280)
                        poli3.goto(390,y3)
                        y4=random.randint(-280,280)
                        poli4.goto(390,y4)
                        y5=random.randint(-280,280)
                        poli5.goto(390,y5)
                        puntos+=1

                    if personaje_mini.ycor()>=280:
                        personaje_mini.sety(260)

                    if personaje_mini.ycor()<-280:
                        personaje_mini.sety(-260)

                    if ((poli1.xcor()<-340 and poli1.xcor()>-350) and
                         (poli1.ycor()<personaje_mini.ycor()+40 and poli1.ycor()>personaje_mini.ycor()-40)):
                        mini=0
                        y=10

                    if ((poli2.xcor()<-340 and poli2.xcor()>-350) and
                         (poli2.ycor()<personaje_mini.ycor()+40 and poli2.ycor()>personaje_mini.ycor()-40)):
                        mini=0
                        y=10

                    if ((poli3.xcor()<-340 and poli3.xcor()>-350) and
                         (poli3.ycor()<personaje_mini.ycor()+40 and poli3.ycor()>personaje_mini.ycor()-40)):
                        mini=0
                        y=10

                    if ((poli4.xcor()<-340 and poli4.xcor()>-350) and
                         (poli4.ycor()<personaje_mini.ycor()+40 and poli4.ycor()>personaje_mini.ycor()-40)):
                        mini=0
                        y=10

                    if ((poli5.xcor()<-340 and poli5.xcor()>-350) and
                         (poli5.ycor()<personaje_mini.ycor()+40 and poli5.ycor()>personaje_mini.ycor()-40)):
                        mini=0
                        y=10

                if puntos==10:
                    y=16
                    tval2=tiempoje(tiempo)
                    tiempo=0

        #vale
        elif y==12:
            personaje_mini.hideturtle()
            poli1.hideturtle()
            poli2.hideturtle()
            poli3.hideturtle()
            poli4.hideturtle()
            poli5.hideturtle()
            vale()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                y=14
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #aduitorio dentro
        elif y==13:
            auditorio_den1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.goto(-360,-260)
                cua_tex=0
                y=4
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=4
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cuadro dire 2
        elif y==14:
            cuadro_dire2()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                y=2
                x=6
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria dentro
        elif y==15:
            cafeteria_den1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.hideturtle()
                personaje.goto(-360,-260)
                cua_tex=0
                y=5
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=4
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cuadro dire 1
        elif y==16:
            cuadro_dire1()
            personaje_mini.hideturtle()
            time.sleep(0)
            poli1.hideturtle()
            poli2.hideturtle()
            poli3.hideturtle()
            poli4.hideturtle()
            poli5.hideturtle()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                y=12
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #ejecuta a3
    elif x==6:
        acertijo3()
        personaje.hideturtle()
        persona1.hideturtle()
        persona2.hideturtle()
        persona3.hideturtle()
        persona4.hideturtle()
        persona5.hideturtle()
        cuadro_dialogo.clear()
        dialogo.clear()
        inventari.clear()
        dialogo_cua=0
        if espacio.xcor()!=tespa:
            pen.clear()
            tilte.clear()
            pasar.clear()
            vales=2
            inventario=f"vales: {vales}"
            x=7
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #parte de juego con a3
    elif x==7:
        #mapa
        if y==0:
            personaje.hideturtle()
            persona1.hideturtle()
            persona2.hideturtle()
            persona3.hideturtle()
            persona4.hideturtle()
            persona5.hideturtle()
            mapa()
            if tecla1.xcor()!=t1:
                y=1

            elif tecla2.xcor()!=t2:
                y=2

            elif tecla3.xcor()!=t3:
                y=3

            elif tecla4.xcor()!=t4:
                y=4

            elif tecla5.xcor()!=t5:
                y=5
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #canchas
        elif y==1:
            cancha2()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.goto(-360,-260)
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()
            if ((personaje.xcor()>=220 and personaje.xcor()<=360)
                and (personaje.ycor()>=140 and personaje.ycor()<=260)):
                y=6
                inventari.clear()

        #biblioteca
        elif y==2:
            biblio2()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente
        if y==3:
            fuente2()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #auditorio
        elif y==4:
            auditorio2()
            personaje.hideturtle()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(400,-300)
                y=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria
        elif y==5:
            cafeteria1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-20,-300)
                y=9
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #arbolo
        elif y==6:
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            personaje.hideturtle()
            arbol2()
            if t1!=tecla1.xcor():
                inventari.clear()
                personaje.goto(200,120)
                y=1
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            if moneda==0:
                if t3!= tecla3.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    y=7
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #moneda
        elif y==7:
            moneda_n()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            if tecla1.xcor()!=t1:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                mon="moneda"
                moneda=1
                inventari.goto(xinventario_d,yinventario)
            if tecla2.xcor()!=t2:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                moneda=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #aduitorio dentro
        elif y==8:
            auditorio_den2()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-360,-260)
                y=4
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria dentro
        elif y==9:
            cafeteria_den1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.hideturtle()
                personaje.goto(-360,-260)
                cua_tex=0
                y=5
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som1
        if y==10:
            fuente2_1()

            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som2
        if y==11:
            fuente2_2()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som3
        if y==12:
            fuente2_3()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som4
        if y==13:
            fuente2_4()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som5
        if y==14:
            fuente2_5()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21


            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som6
        if y==15:
            fuente2_6()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som7
        if y==16:
            fuente2_7()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.ycor()==240) and (personaje.xcor()>=-40 and personaje.xcor()<=20):
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=15
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som8
        if y==17:
            fuente2_8()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.ycor()==240) and (personaje.xcor()>=-40 and personaje.xcor()<=20):
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=15
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som9
        if y==18:
            fuente2_9()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.ycor()==240) and (personaje.xcor()>=-40 and personaje.xcor()<=20):
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=15
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som10
        if y==19:
            fuente2_10()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif tmas!=teclamas.xcor():
                y=20

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.ycor()==240) and (personaje.xcor()>=-40 and personaje.xcor()<=20):
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=15
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som11
        if y==20:
            fuente2_11()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmenos!=teclamenos.xcor():
                y=21

            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente som12
        if y==21:
            fuente2_12()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()

                cuadro_inventario2.penup()
                cuadro_inventario2.color(color_cuadro)
                cuadro_inventario2.goto(inventari2.xcor()-10,inventari2.ycor()-30)
                cuadro_inventario2.pendown()
                cuadro_inventario2.begin_fill()
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(300)
                cuadro_inventario2.left(90)
                cuadro_inventario2.forward(alto)
                cuadro_inventario2.left(90)
                cuadro_inventario2.end_fill()
                cua_tex=1

            if ta!=teclaa.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=0
            if tb!=teclab.xcor():
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                cua_tex=0
                x=6

            if 1==tecla1.xcor():
                y=10

            elif t2!=tecla2.xcor():
                y=11

            elif t3!=tecla3.xcor():
                y=12

            elif t4!=tecla4.xcor():
                y=13

            elif t5!=tecla5.xcor():
                y=14

            elif t6!=tecla6.xcor():
                y=15

            elif t7!=tecla7.xcor():
                y=16

            elif t8!=tecla8.xcor():
                y=17

            elif t9!=tecla9.xcor():
                y=18

            elif t0!=tecla0.xcor():
                y=19

            elif tmas!=teclamas.xcor():
                y=20

            if (personaje.ycor()==240) and (personaje.xcor()>=-40 and personaje.xcor()<=20):
                inventari.clear()
                inventari2.clear()
                cuadro_inventario.clear()
                cuadro_inventario2.clear()
                personaje.goto(-400,-300)
                cua_tex=0
                y=22
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo21()
                    personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo25()
                    personaje.goto(320,0)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo24()
                    personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo22()
                    personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    dialogo23()
                    personaje.goto(320,180)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #ladrillo1
        if y==22:
            personaje.hideturtle()
            persona1.hideturtle()
            persona2.hideturtle()
            persona3.hideturtle()
            persona4.hideturtle()
            persona5.hideturtle()
            ladrillo1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                personaje.goto(0,260)
                cua_tex=0
                y=21
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            if t3!= tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=23
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #ladrillo 2
        if y==23:
            inventari.clear()
            ladrillo2()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            if t1!=tecla1.xcor():
                inventari.clear()
                y=22
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=6
            if t3!= tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=24
                tval3=tiempoje(tiempo)
                tiempo=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #vale
        elif y==24:
            vale()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                y=25
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #hueco
        elif y==25:
            hueco()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                personaje.goto(0,260)
                y=3
                x=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #ejecuta a4
    elif x==8:
        acertijo4()
        personaje.hideturtle()
        persona1.hideturtle()
        persona2.hideturtle()
        persona3.hideturtle()
        persona4.hideturtle()
        persona5.hideturtle()
        cuadro_dialogo.clear()
        dialogo.clear()
        inventari.clear()
        dialogo_cua=0
        if espacio.xcor()!=tespa:
            pen.clear()
            tilte.clear()
            pasar.clear()
            vales=3
            inventario=f"vales: {vales}"
            x=9
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #parte de juego con a4
    elif x==9:
        #mapa
        if y==0:
            personaje.hideturtle()
            persona1.hideturtle()
            persona2.hideturtle()
            persona3.hideturtle()
            persona4.hideturtle()
            persona5.hideturtle()
            mapa()
            if tecla1.xcor()!=t1:
                y=1

            elif tecla2.xcor()!=t2:
                y=2

            elif tecla3.xcor()!=t3:
                y=3
                personaje.goto(-360,-260)

            elif tecla4.xcor()!=t4:
                y=4

            elif tecla5.xcor()!=t5:
                y=5
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #canchas
        elif y==1:
            cancha3()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.goto(-360,-260)
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()
            if ((personaje.xcor()>=220 and personaje.xcor()<=360)
                and (personaje.ycor()>=140 and personaje.ycor()<=260)):
                y=6
                inventari.clear()

        #biblioteca
        elif y==2:
            biblio3()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente
        elif y==3:
            fuente3()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-400,-300)
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo31()
                        personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo35()
                        personaje.goto(20,-240)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo34()
                        personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo32()
                        personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo33()
                        personaje.goto(320,180)
            else:
                    cuadro_dialogo.clear()
                    dialogo.clear()
                    dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #auditorio
        elif y==4:
            auditorio3()
            personaje.hideturtle()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(400,-300)
                y=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria
        elif y==5:
            cafeteria3()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-20,-300)
                y=9
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #arbolo
        elif y==6:
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            personaje.hideturtle()
            arbol3()
            if t1!=tecla1.xcor():
                inventari.clear()
                personaje.goto(200,120)
                y=1
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            if moneda==0:
                if t3!= tecla3.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    y=7
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #moneda
        elif y==7:
            moneda_n()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            if tecla1.xcor()!=t1:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                mon="moneda"
                moneda=1
                inventari.goto(xinventario_d,yinventario)
            if tecla2.xcor()!=t2:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                moneda=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #aduitorio dentro
        elif y==8:
            auditorio_den3()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(340,-260)
                contador1.hideturtle()
                contador2.hideturtle()
                contador3.hideturtle()
                contador=0
                y=4
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                contador1.hideturtle()
                contador2.hideturtle()
                contador3.hideturtle()
                x=8

            if (personaje.xcor()<=-320) and (personaje.ycor()>=240):
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=10
                contador1.hideturtle()
                contador2.hideturtle()
                contador3.hideturtle()
                contador=0

            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()
            if contador==0:
                if (personaje.xcor()>=100 and personaje.xcor()<=120) and (personaje.ycor()==140):
                    contador=1
                    contador1.showturtle()
            elif contador==1:
                if (personaje.xcor()==80) and (personaje.ycor()==180):
                    contador=2
                    contador2.showturtle()
                elif (personaje.xcor()==40) and (personaje.ycor()==140):
                    contador=0
                    contador1.hideturtle()
                elif (personaje.xcor()==160) and (personaje.ycor()>=160 and personaje.ycor()<=180):
                    contador=0
                    contador1.hideturtle()
            elif contador==2:
                if (personaje.xcor()==160) and (personaje.ycor()>=160 and personaje.ycor()<=180):
                    contador=3
                    contador3.showturtle()
                elif (personaje.xcor()==40) and (personaje.ycor()==140):
                    contador=0
                    contador1.hideturtle()
                    contador2.hideturtle()
            elif contador==3:
                if (personaje.xcor()==40) and (personaje.ycor()==140):
                    contador=4
            elif contador==4:
                y=11

        #cafeteria dentro
        elif y==9:
            cafeteria_den3()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.hideturtle()
                personaje.goto(-360,-260)
                cua_tex=0
                y=5
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #backstage
        elif y==10:
            personaje.hideturtle()
            backstage()

            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-360,220)
                y=8
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #aduitorio dentro2
        elif y==11:
            contador1.hideturtle()
            contador2.hideturtle()
            contador3.hideturtle()
            auditorio_den3_2()
            cuadro_dialogo.clear()
            dialogo_cua=0
            dialogo.clear()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(340,-260)
                y=4
                contador=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8

            if (personaje.xcor()<=-260 and personaje.xcor()>=-320) and (personaje.ycor()<=180 and personaje.ycor()>=140):
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-360,-260)
                y=12

            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fondo
        elif y==12:
            fondo()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-280,120)
                y=11
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                pizarra.hideturtle()
                cua_tex=0
                x=8

            if (personaje.xcor()>=-120 and personaje.xcor()<=120) and (personaje.ycor()>=40):
                pizarra.showturtle()
                if t2!=tecla2.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    pizarra.hideturtle()
                    cua_tex=0
                    x=8
            else:
                pizarra.hideturtle()

            if (personaje.xcor()>=-60 and personaje.xcor()<=60) and (personaje.ycor()>=140):
                y=13
                cuadro_dialogo.clear()
                dialogo.clear()
                cuadro_inventario.clear()
                inventari.clear()
                cua_tex=0

            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #pizarra1
        elif y==13:
            pizarra.hideturtle()
            personaje.hideturtle()
            pizarra1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                dialogo_cua=0
                personaje.goto(0,120)
                y=12
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=8
            if t3!= tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=14
                tval4=tiempoje(tiempo)
                tiempo=0

            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #vale
        elif y==14:
            vale()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                y=15
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #pizarra2
        elif y==15:
            pizarra2()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                personaje.goto(0,260)
                y=8
                x=10
                personaje.goto(-280,120)
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #ejecuta a5
    elif x==10:
        acertijo5()
        personaje.hideturtle()
        persona1.hideturtle()
        persona2.hideturtle()
        persona3.hideturtle()
        persona4.hideturtle()
        persona5.hideturtle()
        cuadro_dialogo.clear()
        dialogo.clear()
        inventari.clear()
        dialogo_cua=0
        if espacio.xcor()!=tespa:
            pen.clear()
            tilte.clear()
            pasar.clear()
            vales=4
            inventario=f"vales: {vales}"
            x=11
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #parte de juego con a5
    elif x==11:
        #mapa
        if y==0:
            personaje.hideturtle()
            persona1.hideturtle()
            persona2.hideturtle()
            persona3.hideturtle()
            persona4.hideturtle()
            persona5.hideturtle()
            mapa()
            if tecla1.xcor()!=t1:
                y=1

            elif tecla2.xcor()!=t2:
                y=2

            elif tecla3.xcor()!=t3:
                y=3

            elif tecla4.xcor()!=t4:
                y=4

            elif tecla5.xcor()!=t5:
                y=5
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #canchas
        elif y==1:
            cancha4()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.goto(-360,-260)
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()
            if ((personaje.xcor()>=220 and personaje.xcor()<=360)
                and (personaje.ycor()>=140 and personaje.ycor()<=260)):
                y=6
                inventari.clear()

        #biblioteca
        elif y==2:
            biblio4()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente
        elif y==3:
            fuente4()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-400,-300)
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo41()
                        personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo45()
                        personaje.goto(20,-240)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo44()
                        personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo42()
                        personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo43()
                        personaje.goto(320,180)
            else:
                    cuadro_dialogo.clear()
                    dialogo.clear()
                    dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #auditorio
        elif y==4:
            auditorio4()
            personaje.hideturtle()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(400,-300)
                y=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria
        elif y==5:
            cafeteria4()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-20,-300)
                y=9
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #arbolo
        elif y==6:
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            personaje.hideturtle()
            arbol4()
            if t1!=tecla1.xcor():
                inventari.clear()
                personaje.goto(200,120)
                y=1
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10
            if moneda==0:
                if t3!= tecla3.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    cua_tex=0
                    y=7
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #moneda
        elif y==7:
            moneda_n()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(200)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1
            if tecla1.xcor()!=t1:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                mon="moneda"
                moneda=1
                inventari.goto(xinventario_d,yinventario)
            if tecla2.xcor()!=t2:
                inventari.clear()
                cuadro_inventario.clear()
                inventari.goto(xinventario_d,yinventario)
                cua_tex=0
                y=6
                moneda=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #aduitorio dentro
        elif y==8:
            auditorio_den4()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-360,-260)
                y=4
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria dentro
        elif y==9:
            cafeteria_den4()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.hideturtle()
                personaje.goto(-360,-260)
                cua_tex=0
                y=5
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10

            if (personaje.xcor()>=220 and personaje.xcor()<=320) and (personaje.ycor()==220):
                inventari.clear()
                cuadro_inventario.clear()
                personaje.hideturtle()
                cua_tex=0
                y=10

            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #vendingmachine1
        elif y==10:
            vendingmachine1()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(280,200)
                y=9
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10
            if t3!= tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=11
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #vendingmachine2
        elif y==11:
            vendingmachine2()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(280,200)
                y=9
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=10

            if moneda==1:
                if t3!=tecla3.xcor():
                    inventari.clear()
                    cuadro_inventario.clear()
                    y=12
                    personaje.goto(280,200)
                    tval5=tiempoje(tiempo)
                    tiempo=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #vale
        elif y==12:
            vale()
            if espacio.xcor()!=tespa:
                pen.clear()
                tilte.clear()
                pasar.clear()
                x=12
                y=8
                mon=""
                vales=5
                inventario=f"vales: {vales}"
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #entrega
    elif x==12:
        entrega()
        personaje.hideturtle()
        persona1.hideturtle()
        persona2.hideturtle()
        persona3.hideturtle()
        persona4.hideturtle()
        persona5.hideturtle()
        cuadro_dialogo.clear()
        dialogo.clear()
        inventari.clear()
        dialogo_cua=0
        cua_tex=0
        if espacio.xcor()!=tespa:
            pen.clear()
            tilte.clear()
            pasar.clear()
            x=13
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #parte final del juego
    elif x==13:
        #mapa
        if y==0:
            personaje.hideturtle()
            persona1.hideturtle()
            persona2.hideturtle()
            persona3.hideturtle()
            persona4.hideturtle()
            persona5.hideturtle()
            mapa()
            if tecla1.xcor()!=t1:
                y=1

            elif tecla2.xcor()!=t2:
                y=2

            elif tecla3.xcor()!=t3:
                y=3

            elif tecla4.xcor()!=t4:
                y=4

            elif tecla5.xcor()!=t5:
                y=5
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #canchas
        elif y==1:
            cancha5()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.goto(-360,-260)
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=12
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()
            if ((personaje.xcor()>=220 and personaje.xcor()<=360)
                and (personaje.ycor()>=140 and personaje.ycor()<=260)):
                y=6
                inventari.clear()

        #biblioteca
        elif y==2:
            biblio5()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=12
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #fuente
        elif y==3:
            fuente5()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-400,-300)
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=12
            if (personaje.xcor()>=persona5.xcor()-40 and personaje.xcor()<=persona5.xcor()+40) and (personaje.ycor()>=persona5.ycor()-20 and personaje.ycor()<=persona5.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo51()
                        personaje.goto(-280,-20)
            elif (personaje.xcor()>=persona1.xcor()-40 and personaje.xcor()<=persona1.xcor()+40) and (personaje.ycor()>=persona1.ycor()-20 and personaje.ycor()<=persona1.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo55()
                        personaje.goto(20,-240)
            elif (personaje.xcor()>=persona2.xcor()-40 and personaje.xcor()<=persona2.xcor()+40) and (personaje.ycor()>=persona2.ycor()-20 and personaje.ycor()<=persona2.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo54()
                        personaje.goto(-320,180)
            elif (personaje.xcor()>=persona3.xcor()-20 and personaje.xcor()<=persona3.xcor()+20) and (personaje.ycor()>=persona3.ycor()-40 and personaje.ycor()<=persona3.ycor()+40):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo52()
                        personaje.goto(360,-140)
            elif (personaje.xcor()>=persona4.xcor()-40 and personaje.xcor()<=persona4.xcor()+40) and (personaje.ycor()>=persona4.ycor()-20 and personaje.ycor()<=persona4.ycor()+20):
                    if dialogo_cua==0:
                        cuadro_dialogo.penup()
                        cuadro_dialogo.color("white")
                        cuadro_dialogo.goto(xdialogo,ydialogo)
                        cuadro_dialogo.pendown()
                        cuadro_dialogo.begin_fill()
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(800)
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.forward(80)
                        cuadro_dialogo.end_fill()
                        cuadro_dialogo.left(90)
                        cuadro_dialogo.hideturtle()
                        dialogo_cua=1
                    if dialogo_cua==1:
                        dialogo53()
                        personaje.goto(320,180)
            else:
                    cuadro_dialogo.clear()
                    dialogo.clear()
                    dialogo_cua=0
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #auditorio
        elif y==4:
            auditorio5()
            personaje.hideturtle()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=12
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(400,-300)
                y=7
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria
        elif y==5:
            cafeteria5()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                y=0
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=12
            if t3!=tecla3.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(-20,-300)
                y=8
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #arbolo
        elif y==6:
            arbol5()
            personaje.hideturtle()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                personaje.goto(200,120)
                y=1
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=12
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #aduitorio dentro
        elif y==7:
            auditorio_den5()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                personaje.goto(340,-260)
                profesor1.hideturtle()
                profesor2.hideturtle()
                profesor3.hideturtle()
                profesor4.hideturtle()
                profesor5.hideturtle()
                y=4
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                profesor1.hideturtle()
                profesor2.hideturtle()
                profesor3.hideturtle()
                profesor4.hideturtle()
                profesor5.hideturtle()
                x=12

            if (personaje.xcor()>=profesor1.xcor()-20 and personaje.xcor()<=profesor1.xcor()+20) and (personaje.ycor()>=profesor1.ycor()-40 and personaje.ycor()<=profesor1.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    if maestro_1==0:
                        maestro1()
                        personaje.goto(240,160)
                        if t3!=tecla3.xcor():
                            vales-=1
                            inventario=f"vales: {vales}"
                            inventari.clear()
                            dialogo.clear()
                            maestro_1=1
                    if maestro_1==1:
                        maestro1()
                        personaje.goto(240,160)
            elif (personaje.xcor()>=profesor2.xcor()-20 and personaje.xcor()<=profesor2.xcor()+20) and (personaje.ycor()>=profesor2.ycor()-40 and personaje.ycor()<=profesor2.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    if maestro_2==0:
                        maestro2()
                        personaje.goto(160,160)
                        if t3!=tecla3.xcor():
                            vales-=1
                            inventario=f"vales: {vales}"
                            inventari.clear()
                            dialogo.clear()
                            maestro_2=1
                    if maestro_2==1:
                        maestro2()
                        personaje.goto(160,160)
            elif (personaje.xcor()>=profesor3.xcor()-20 and personaje.xcor()<=profesor3.xcor()+20) and (personaje.ycor()>=profesor3.ycor()-40 and personaje.ycor()<=profesor3.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    if maestro_3==0:
                        maestro3()
                        personaje.goto(80,160)
                        if t3!=tecla3.xcor():
                            vales-=1
                            inventario=f"vales: {vales}"
                            inventari.clear()
                            dialogo.clear()
                            maestro_3=1
                    if maestro_3==1:
                        maestro3()
                        personaje.goto(80,160)
            elif (personaje.xcor()>=profesor4.xcor()-20 and personaje.xcor()<=profesor4.xcor()+20) and (personaje.ycor()>=profesor4.ycor()-40 and personaje.ycor()<=profesor4.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    if maestro_4==0:
                        maestro4()
                        personaje.goto(0,160)
                        if t3!=tecla3.xcor():
                            vales-=1
                            inventario=f"vales: {vales}"
                            inventari.clear()
                            dialogo.clear()
                            maestro_4=1
                    if maestro_4==1:
                        maestro4()
                        personaje.goto(0,160)
            elif (personaje.xcor()>=profesor5.xcor()-20 and personaje.xcor()<=profesor5.xcor()+20) and (personaje.ycor()>=profesor5.ycor()-40 and personaje.ycor()<=profesor5.ycor()+20):
                if dialogo_cua==0:
                    cuadro_dialogo.penup()
                    cuadro_dialogo.color("white")
                    cuadro_dialogo.goto(xdialogo,ydialogo)
                    cuadro_dialogo.pendown()
                    cuadro_dialogo.begin_fill()
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(800)
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.forward(80)
                    cuadro_dialogo.end_fill()
                    cuadro_dialogo.left(90)
                    cuadro_dialogo.hideturtle()
                    dialogo_cua=1
                if dialogo_cua==1:
                    if maestro_5==0:
                        maestro5()
                        personaje.goto(-80,160)
                        if t3!=tecla3.xcor():
                            vales-=1
                            inventario=f"vales: {vales}"
                            inventari.clear()
                            dialogo.clear()
                            maestro_5=1
                    if maestro_5==1:
                        maestro5()
                        personaje.goto(-80,160)
            else:
                cuadro_dialogo.clear()
                dialogo.clear()
                dialogo_cua=0

            if vales==0:
                x=14
                tval0=tiempoje(tiempo)
                tiempo=0
                t=1
                inventari.clear()
                cuadro_inventario.clear()
                cuadro_dialogo.clear()
                dialogo.clear()
                personaje.hideturtle()
                profesor1.hideturtle()
                profesor2.hideturtle()
                profesor3.hideturtle()
                profesor4.hideturtle()
                profesor5.hideturtle()
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

        #cafeteria dentro
        elif y==8:
            cafeteria_den5()
            if cua_tex==0:
                cuadro_inventario.penup()
                cuadro_inventario.color(color_cuadro)
                cuadro_inventario.goto(inventari.xcor()-10,inventari.ycor()-30)
                cuadro_inventario.pendown()
                cuadro_inventario.begin_fill()
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(largo)
                cuadro_inventario.left(90)
                cuadro_inventario.forward(alto)
                cuadro_inventario.left(90)
                cuadro_inventario.end_fill()
                cua_tex=1

            if t1!=tecla1.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                personaje.hideturtle()
                personaje.goto(-360,-260)
                cua_tex=0
                y=5
            if t2!=tecla2.xcor():
                inventari.clear()
                cuadro_inventario.clear()
                cua_tex=0
                x=12
            tortugas()
            tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #cierre
    elif x==14:
        cierre()
        if espacio.xcor()!=tespa:
            pen.clear()
            tilte.clear()
            pasar.clear()
            x=15
        tortugas()
        tespa,t1,t2,t3,t4,t5,t6,t7,t8,t9,t0,ta,tb,tmas,tmenos=teclas()

    #fin
    elif x==15:
        fin()

    if t==0:
        tiempo+=1
        j+=1

turtle.done()