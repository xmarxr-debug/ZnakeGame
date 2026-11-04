
import pygame

# Colores del juego
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

def draw_game(pantalla, serpiente):

    # Dibujar el fondo
    pantalla.fill(NEGRO)

    # Dibujar la serpiente
    serpiente.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.update()
