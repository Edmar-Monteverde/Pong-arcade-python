# movimiento_paletas.py

# límites del campo para las paletas
LIMITE_SUPERIOR = 215
LIMITE_INFERIOR = -215
PASO = 20  # cuánto se mueve la paleta


def subir_paleta(paleta):
    y = paleta.ycor()
    nuevo_y = y + PASO
    if nuevo_y > LIMITE_SUPERIOR:
        nuevo_y = LIMITE_SUPERIOR
    paleta.sety(nuevo_y)


def bajar_paleta(paleta):
    y = paleta.ycor()
    nuevo_y = y - PASO
    if nuevo_y < LIMITE_INFERIOR:
        nuevo_y = LIMITE_INFERIOR
    paleta.sety(nuevo_y)
