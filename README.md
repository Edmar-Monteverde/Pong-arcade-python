# 🕹️ Pong Arcade - Python Turtle

Juego clásico **Pong** desarrollado en Python usando la librería **Turtle Graphics**.

El proyecto incluye menú interactivo, dificultad configurable, modo contra CPU, sistema de puntuación y efectos de sonido.

---

## 🎮 Características

- Menú principal
- Modo **Jugador vs Jugador**
- Modo **Jugador vs CPU**
- Dificultad: Fácil, Medio y Difícil
- IA básica para la CPU
- Sistema de puntuación (primer jugador en llegar a 5 gana)
- Sonidos para:
  - rebote
  - punto
  - victoria
- Posibilidad de volver al menú al terminar la partida

---

## 🛠️ Tecnologías usadas

- Python 3
- Turtle Graphics
- winsound (Windows)
- Programación modular
- Control de eventos con teclado

---

## ▶️ Cómo ejecutar el juego

1. Clona el repositorio o descarga el proyecto
2. Asegúrate de tener **Python 3** instalado
3. Ejecuta:

```bash
python main.py


▶️Controles 

Menú

1 → Jugar vs CPU

2 → Jugar vs Jugador

F / M / D → Seleccionar dificultad

Enter → Iniciar juego

Esc → Salir

Juego

Jugador 1: W / S

Jugador 2: ↑ / ↓

Esc → Salir


Estructura del Proyecto


Juego Arcade Pong/
│
├── main.py
├── menu.py
├── campo.py
├── paletas.py
├── pelota.py
├── marcador.py
├── movimiento_paletas.py
├── sonido.py
├── config.py
├── rebote.wav
├── punto.wav
├── victoria.wav
└── README.md

🚀 Posibles mejoras futuras

Pausa del juego

Música de fondo

Mejora de la IA

Portabilidad a otros sistemas

Refactorización usando clases