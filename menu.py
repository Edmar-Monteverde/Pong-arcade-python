## Creamos el menu del juego, para seleccionar la dificultad, modo de juego, etc.

import turtle


def crear_menu():
    """Dibuja el menú y devuelve (texto, estado, acciones)."""

    texto = turtle.Turtle()

    texto.hideturtle()
    texto.penup()
    texto.color("white")

    estado = {
        "modo_juego": "PVP",  # Player vs Player o CPU vs Player
        "dificultad": "MEDIO",  # FACIL, MEDIO, DIFICIL
        "iniciar": False,
    }  # iniciar el juego o no

    def render():  ## Volver a dibujar el menu
        texto.clear()
        texto.goto(0, 140)
        texto.write("JUEGO PONG", align="center", font=("Courier", 44, "bold"))

        texto.goto(0, 60)
        texto.write("1) Jugar vs PC", align="center", font=("Courier", 20, "normal"))
        texto.goto(0, 25)
        texto.write(
            "2) Jugar vs Jugador", align="center", font=("Courier", 20, "normal")
        )

        modo_txt = "VS PC" if estado["modo_juego"] == "CPU" else "VS JUGADOR"
        texto.goto(0, -20)
        texto.write(
            f"Modo de Juego: {modo_txt}", align="center", font=("Courier", 20, "normal")
        )

        texto.goto(0, -60)
        texto.write(
            "Dificultad:  F=facil  M=medio  D=dificil",
            align="center",
            font=("Courier", 18, "normal"),
        )
        texto.goto(0, -90)
        texto.write(
            f'Dificultad: {estado["dificultad"]}',
            align="center",
            font=("Courier", 18, "normal"),
        )

        texto.goto(0, -140)
        texto.write(
            "ENTER= Empezar, ESC=Salir", align="center", font=("Courier", 18, "normal")
        )

    def set_modo_cpu():
        estado["modo_juego"] = "CPU"
        render()

    def set_modo_pvp():
        estado["modo_juego"] = "PVP"
        render()

    def set_dificultad_facil():
        estado["dificultad"] = "FACIL"
        render()

    def set_dificultad_medio():
        estado["dificultad"] = "MEDIO"
        render()

    def set_dificultad_dificil():
        estado["dificultad"] = "DIFICIL"
        render()

    def iniciar_juego():
        estado["iniciar"] = True

    render()  # dibujar el menu por primera vez

    return (
        texto,
        estado,
        {
            "set_modo_cpu": set_modo_cpu,
            "set_modo_pvp": set_modo_pvp,
            "set_dificultad_facil": set_dificultad_facil,
            "set_dificultad_medio": set_dificultad_medio,
            "set_dificultad_dificil": set_dificultad_dificil,
            "iniciar_juego": iniciar_juego,
        },
    )
