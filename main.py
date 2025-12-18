## Practica de turtle graphics

import turtle
import time
from campo import campo_juego
from paletas import crear_paletas
from movimiento_paletas import subir_paleta, bajar_paleta
from pelota import crear_pelota
from marcador import crear_marcador, punto_j1, punto_j2


# Crear ventana de juego
ventana = turtle.Screen()  # Crear ventana
ventana.title("Campo de juego")  # Titulo de la ventana
ventana.bgcolor("black")
ventana.setup(width=800, height=600)  ## ajustar las dimensiones del campo de juego
ventana.tracer(0)  # para que no se vea el dibujo de la pelota y paletas

## Crear campo de juego
campo_juego()

# creamos la paleta izquierda
paleta_izq, paleta_der = crear_paletas()

## dibujar pelotas del juego
pelota = crear_pelota()
## crear el marcador de puntos
puntos_j1 = 0
puntos_j2 = 0
marcador = crear_marcador()

# funciones para mover las paletas

# asignar las teclas para mover las paletas
ventana.listen()  # ESCUCHAR LOS EVENTOS DEL TECLADO
ventana.onkeypress(
    lambda: subir_paleta(paleta_izq), "w"
)  # tecla w para subir la paleta izquierda
ventana.onkeypress(lambda: bajar_paleta(paleta_izq), "s")

ventana.onkeypress(
    lambda: subir_paleta(paleta_der), "Up"
)  # tecla flecha arriba para subir la paleta derecha
ventana.onkeypress(lambda: bajar_paleta(paleta_der), "Down")


## mover la pelota en un bucle infinito

while True:
    ventana.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    ## ajustar los limites de la ventana para la pelota
    if (
        pelota.ycor() > 270
    ):  # 270 por el radio de la pelota si no va pasar un poco el limite
        pelota.sety(
            270
        )  # si la pelota llega al limite superior la colocamos en el limite
        pelota.dy *= -1  # cambiamos la direccion de la pelota
    if (
        pelota.ycor() < -270
    ):  # 270 por el radio de la pelota si no va pasar un poco el limite
        pelota.sety(
            -270
        )  # si la pelota llega al limite inferior la colocamos en el limite
        pelota.dy *= -1  # cambiamos la direccion de la pelota

    ## Rebote con las paleta izquierda      #####################
    if (
        pelota.xcor() < -330 and pelota.xcor() > -350
    ):  # ajustamos   que la pelota este entre la palete y el rango de choque de la pelota
        if (
            pelota.ycor() < paleta_izq.ycor() + 60
            and pelota.ycor() > paleta_izq.ycor() - 60
        ):  # ajustamos que este dentro del tamaño de la paleta
            pelota.setx(-330)  # colocamos la pelota en el limite de la paleta
            pelota.dx *= -1  # cambiamos la direccion de la pelota

    # rebote de la paleta derecha  ############################

    if (
        pelota.xcor() > 330 and pelota.xcor() < 350
    ):  # ajustamos   que la pelota este entre la palete y el rango de choque de la pelota
        if (
            pelota.ycor()
            < paleta_der.ycor()
            + 60  ##  preguntamos el centro de la pelota esta dentro del rango superior de la paleta
            and pelota.ycor()
            > paleta_der.ycor()
            - 60  ##  preguntamos el centro de la pelota esta dentro del rango inferior de la paleta
        ):  # ajustamos que este dentro del tamaño de la paleta
            pelota.setx(330)  # colocamos la pelota en el limite de la paleta
            pelota.dx *= -1  # cambiamos la direccion de la pelota

    # condiciones para sumar puntos
    if pelota.xcor() > 390:
        puntos_j1, puntos_j2 = punto_j1(pelota, marcador, puntos_j1, puntos_j2)

    if pelota.xcor() < -390:
        puntos_j1, puntos_j2 = punto_j2(pelota, marcador, puntos_j1, puntos_j2)

    time.sleep(0.01)  # controlar la velocidad del juego
