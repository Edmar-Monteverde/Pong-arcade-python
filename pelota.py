import turtle


def crear_pelota():
    pelota = turtle.Turtle()
    pelota.speed(0)
    pelota.shape("circle")
    pelota.color("white")
    pelota.penup()
    pelota.goto(0, 0)

    # velocidad de la pelota
    pelota.dx = 2
    pelota.dy = 2
    return pelota
