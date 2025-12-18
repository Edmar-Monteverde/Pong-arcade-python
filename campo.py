import turtle


def campo_juego():

    # creamos el objeto turtle para dibujar
    mesa = turtle.Turtle()
    mesa.speed(0)  ## velocidad de dibujo
    mesa.color("white")  ## color del lapiz
    mesa.pensize(3)  ## grosor del lapiz
    mesa.hideturtle()  # que no se vea el cursor
    # dibujar el borde del campo de juego

    mesa.penup()
    mesa.goto(-380, 280)
    mesa.pendown()

    for lado in range(2):
        mesa.forward(760)  # ancho
        mesa.right(90)
        mesa.forward(560)  # altura
        mesa.right(90)

    ## dibujar la linea central
    mesa.penup()
    mesa.goto(0, 280)
    mesa.setheading(-90)  ## direccion hacia abajo

    for linea in range(19):
        mesa.pendown()
        mesa.forward(15)  # largo de la linea
        mesa.penup()
        mesa.forward(15)  # espacio entre lineas
