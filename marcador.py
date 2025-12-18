import turtle
import time


def crear_marcador():  # crear el marcador de puntos
    marcador = turtle.Turtle()
    marcador.speed(3)
    marcador.color("white")
    marcador.penup()
    marcador.hideturtle()  ##ocultar el turtle
    marcador.goto(0, 280)
    marcador.write(
        "Jugador 1: 0  Jugador 2: 0",
        align="center",
        font=("Courier", 18, "normal"),  # fuente, tamaño, estilo
    )

    return marcador


def Reiniciar_pelota(pelota):  # reiniciar la posicion de la pelota al centro
    pelota.goto(0, 0)
    pelota.dx *= -1
    time.sleep(0.3)


def punto_j1(pelota, marcador, puntos_j1, puntos_j2):  # sumar punto al jugador 1
    puntos_j1 += 1
    marcador.clear()
    marcador.write(
        f"Jugador 1: {puntos_j1}  Jugador 2: {puntos_j2}",
        align="center",
        font=("Courier", 18, "normal"),
    )
    Reiniciar_pelota(pelota)

    return puntos_j1, puntos_j2


def punto_j2(pelota, marcador, puntos_j1, puntos_j2):  # sumar punto al jugador 2
    puntos_j2 += 1
    marcador.clear()
    marcador.write(
        f"Jugador 1: {puntos_j1}  Jugador 2: {puntos_j2}",
        align="center",
        font=("Courier", 18, "normal"),
    )
    Reiniciar_pelota(pelota)

    return puntos_j1, puntos_j2
