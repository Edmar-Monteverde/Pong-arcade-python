import turtle


def crear_paleta(x, color):
    paleta = turtle.Turtle()
    paleta.speed(0)
    paleta.shape("square")
    paleta.color(color)
    paleta.shapesize(stretch_wid=6, stretch_len=1)
    paleta.penup()
    paleta.goto(x, 0)
    return paleta


def crear_paletas():
    paleta_izq = crear_paleta(-350, "blue")
    paleta_der = crear_paleta(350, "red")

    return paleta_izq, paleta_der
