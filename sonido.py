### Creamos el archivo sonido.py para gestionar los sonidos del juego Pong
import winsound
import os

BASE = os.path.dirname(__file__)


def play(nombre):
    ruta = os.path.join(BASE, nombre)
    winsound.PlaySound(
        ruta, winsound.SND_ASYNC | winsound.SND_FILENAME
    )  ###  Reproducir sonido de forma asincrona


def rebote():
    play("rebote.wav")


def punto_marcado():
    play("punto.wav")


def victoria():
    play("victoria.wav")
