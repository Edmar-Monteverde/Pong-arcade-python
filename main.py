## Practica de turtle graphics

import turtle
import time

from campo import campo_juego
from paletas import crear_paletas
from movimiento_paletas import subir_paleta, bajar_paleta
from pelota import crear_pelota
from marcador import crear_marcador, punto_j1, punto_j2

from menu import crear_menu
from config import DIFICULTADES
from sonido import rebote, punto_marcado, victoria

# Crear ventana de juego
ventana = turtle.Screen()  # Crear ventana
ventana.title("Campo de juego")  # Titulo de la ventana
ventana.bgcolor("black")
ventana.setup(width=800, height=600)  ## ajustar las dimensiones del campo de juego
ventana.tracer(0)  # para que no se vea el dibujo de la pelota y paletas

ventana.listen()  # ESCUCHAR LOS EVENTOS DEL TECLADO


def nada():
    pass


def limpiar_teclas_menu():
    for tecla in ["1", "2", "f", "m", "d", "F", "M", "D", "Return", "Escape"]:
        ventana.onkeypress(nada, tecla)


## Mostrar menu de inicio

### Bucle Principal del juego ###

while True:

    # ------------------ MENÚ ------------------
    menu_turtle, estado_menu, acciones_menu = crear_menu()

    ventana.onkeypress(acciones_menu["set_modo_cpu"], "1")
    ventana.onkeypress(acciones_menu["set_modo_pvp"], "2")

    ventana.onkeypress(acciones_menu["set_dificultad_facil"], "f")
    ventana.onkeypress(acciones_menu["set_dificultad_medio"], "m")
    ventana.onkeypress(acciones_menu["set_dificultad_dificil"], "d")

    ventana.onkeypress(acciones_menu["set_dificultad_facil"], "F")
    ventana.onkeypress(acciones_menu["set_dificultad_medio"], "M")
    ventana.onkeypress(acciones_menu["set_dificultad_dificil"], "D")

    ventana.onkeypress(acciones_menu["iniciar_juego"], "Return")
    ventana.onkeypress(lambda: ventana.bye(), "Escape")

    while not estado_menu["iniciar"]:
        ventana.update()
        time.sleep(0.02)

    # leer selección
    modo_juego = estado_menu["modo_juego"]
    dificultad = estado_menu["dificultad"]
    configuracion = DIFICULTADES[dificultad]

    # limpiar menú y desactivar teclas del menú
    menu_turtle.clear()
    menu_turtle.hideturtle()
    limpiar_teclas_menu()

    ## Crear campo de juego
    campo_juego()
    # creamos la paletas
    paleta_izq, paleta_der = crear_paletas()
    ## dibujar pelotas del juego
    pelota = crear_pelota()

    ## Configurar la velocidad de la pelota y la CPU segun la dificultad seleccionada

    vel_bola = configuracion["vel_bola"]
    pelota.dx = vel_bola if pelota.dx >= 0 else -vel_bola
    pelota.dy = vel_bola if pelota.dy >= 0 else -vel_bola

    ## crear el marcador de puntos
    puntos_j1 = 0
    puntos_j2 = 0
    marcador = crear_marcador()

    # funciones para mover las paletas
    ventana.listen()
    # asignar las teclas para mover las paletas
    ventana.onkeypress(
        lambda: subir_paleta(paleta_izq), "w"
    )  # tecla w para subir la paleta izquierda
    ventana.onkeypress(lambda: bajar_paleta(paleta_izq), "s")

    if modo_juego == "PVP":
        ventana.listen()
        ventana.onkeypress(
            lambda: subir_paleta(paleta_der), "Up"
        )  # tecla flecha arriba para subir la paleta derecha
        ventana.onkeypress(lambda: bajar_paleta(paleta_der), "Down")

    ventana.onkeypress(lambda: ventana.bye(), "Escape")

    # ------------------ LOOP DE LA PARTIDA ------------------
    puntos_para_ganar = 5
    partida_terminada = False
    sleep_por_dificultad = {"FACIL": 0.02, "MEDIO": 0.015, "DIFICIL": 0.01}
    dt = sleep_por_dificultad[dificultad]

    while True:
        ventana.update()
        # movimiento de la pelota
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
            rebote()
        if (
            pelota.ycor() < -270
        ):  # 270 por el radio de la pelota que es 10 si no va pasar un poco el limite
            pelota.sety(
                -270
            )  # si la pelota llega al limite inferior la colocamos en el limite
            pelota.dy *= -1  # cambiamos la direccion de la pelota
            rebote()
        ### Juego con la CPU  ##########################

        if modo_juego == "CPU":
            cpu_speed = configuracion["cpu_speed"]
            margen_cpu = {"FACIL": 50, "MEDIO": 35, "DIFICIL": 10}[dificultad]
            if paleta_der.ycor() < pelota.ycor() - margen_cpu:
                paleta_der.sety(min(paleta_der.ycor() + cpu_speed, 215))
            elif paleta_der.ycor() > pelota.ycor() + margen_cpu:
                paleta_der.sety(max(paleta_der.ycor() - cpu_speed, -215))

        ## Rebote con las paleta izquierda      #####################
        if (
            -350 < pelota.xcor() < -330
        ):  # ajustamos   que la pelota este entre la palete y el rango de choque de la pelota
            if (
                pelota.ycor() < paleta_izq.ycor() + 60
                and pelota.ycor() > paleta_izq.ycor() - 60
            ):  # ajustamos que este dentro del tamaño de la paleta
                pelota.setx(-330)  # colocamos la pelota en el limite de la paleta
                pelota.dx *= -1  # cambiamos la direccion de la pelota
                rebote()
        # rebote de la paleta derecha  ############################

        if (
            330 < pelota.xcor() < 350
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
                rebote()

        # condiciones para sumar puntos y para ganar el juego ##########################

        if pelota.xcor() > 390:
            puntos_j1, puntos_j2 = punto_j1(pelota, marcador, puntos_j1, puntos_j2)
            punto_marcado()

        if pelota.xcor() < -390:
            puntos_j1, puntos_j2 = punto_j2(pelota, marcador, puntos_j1, puntos_j2)
            punto_marcado()

            ## verificar si alguien ha ganado
        if puntos_j1 >= puntos_para_ganar or puntos_j2 >= puntos_para_ganar:

            ganador = "Jugador 1" if puntos_j1 > puntos_j2 else "Jugador 2"
            marcador.clear()
            marcador.goto(0, 0)
            marcador.write(
                f"{ganador} ha ganado!",
                align="center",
                font=("Courier", 30, "bold"),
            )
            victoria()
            ventana.update()
            time.sleep(2)
            partida_terminada = True
            break  # salir del bucle del juego
        time.sleep(dt)

    # ------------------ LIMPIAR Y VOLVER AL MENÚ ------------------
    if partida_terminada:
        # ocultar / limpiar objetos (para que no se acumulen)
        try:
            pelota.hideturtle()
            paleta_izq.hideturtle()
            paleta_der.hideturtle()
            marcador.clear()
        except:
            pass

        # pequeña pausa antes del menú
        ventana.update()
        time.sleep(0.2)

        # volver al menú (continúa el while True externo)
        continue
