
import pygame
import sys

from snake import Snake
from food import Food
from controls import handle_events
from render import draw_game, draw_menu

pygame.init()

# Dimensiones
ANCHO = 600
ALTO = 400

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi juego Snake")

reloj = pygame.time.Clock()

# Crear elementos
serpiente = Snake()
comida = Food()
comida.respawn(serpiente.body)

# Variables
ejecutando = True
estado = "menu"

puntuacion = 0
record = 0

while ejecutando:

    # -------------------------
    # MENU DE INICIO
    # -------------------------

    if estado == "menu":

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                ejecutando = False

            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_RETURN:
                    estado = "playing"

                elif evento.key == pygame.K_ESCAPE:
                    ejecutando = False

        draw_menu(pantalla, record)

    # -------------------------
    # JUEGO
    # -------------------------

    elif estado == "playing":

        ejecutando, reiniciar = handle_events(serpiente)

        if not ejecutando:
            break

        # Calcular siguiente posición
        x, y = serpiente.body[0]
        dx, dy = serpiente.direction

        siguiente_posicion = (x + dx, y + dy)

        # Comprobar si comerá
        comio = siguiente_posicion == comida.position

        # Mover serpiente
        serpiente.move(grow=comio)

        # Actualizar puntuación
        if comio:
            puntuacion += 10
            comida.respawn(serpiente.body)

        # Detectar colisiones
        if serpiente.check_wall_collision(ANCHO, ALTO):
            estado = "game_over"

        elif serpiente.check_self_collision():
            estado = "game_over"

        # Actualizar récord
        record = max(record, puntuacion)

        draw_game(
            pantalla,
            serpiente,
            comida,
            puntuacion,
            False,
            record
        )

    # -------------------------
    # GAME OVER
    # -------------------------

    elif estado == "game_over":

        ejecutando, reiniciar = handle_events(
            serpiente,
            game_over=True
        )

        if not ejecutando:
            break

        if reiniciar:

            serpiente = Snake()

            comida = Food()
            comida.respawn(serpiente.body)

            puntuacion = 0
            estado = "playing"

        draw_game(
            pantalla,
            serpiente,
            comida,
            puntuacion,
            True,
            record
        )

    reloj.tick(9)

pygame.quit()
sys.exit()
