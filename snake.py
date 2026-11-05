
import pygame

# PALETA DE COLORES
FONDO = (8, 11, 24)
CUADRICULA = (23, 32, 51)
TURQUESA = (0, 245, 212)
ROSA = (255, 46, 136)
MORADO = (168, 85, 247)
BLANCO = (248, 250, 252)


def draw_grid(pantalla):
    """Dibuja la cuadrícula futurista."""
    for x in range(0, 600, 20):
        pygame.draw.line(pantalla, CUADRICULA, (x, 0), (x, 400))

    for y in range(0, 400, 20):
        pygame.draw.line(pantalla, CUADRICULA, (0, y), (600, y))


def draw_snake(pantalla, serpiente):
    """Dibuja la serpiente sin difuminado."""
    for i, segmento in enumerate(serpiente.body):
        x, y = segmento

        pygame.draw.rect(
            pantalla,
            TURQUESA,
            (x + 1, y + 1, 18, 18),
            border_radius=4
        )

        if i == 0:
            pygame.draw.circle(pantalla, BLANCO, (x + 6, y + 6), 2)
            pygame.draw.circle(pantalla, BLANCO, (x + 14, y + 6), 2)


def draw_food(pantalla, comida):
    """Dibuja la comida rosa."""
    x, y = comida.position

    pygame.draw.circle(pantalla, ROSA, (x + 10, y + 10), 7)
    pygame.draw.circle(pantalla, BLANCO, (x + 8, y + 8), 2)


def draw_text(pantalla, texto, size, color, posicion):
    fuente = pygame.font.SysFont("consolas", size, bold=True)
    imagen = fuente.render(texto, True, color)
    pantalla.blit(imagen, posicion)


def draw_menu(pantalla, record=0):
    """Dibuja el menú principal."""
    pantalla.fill(FONDO)
    draw_grid(pantalla)

    draw_text(pantalla, "NEON SNAKE", 48, TURQUESA, (155, 90))
    draw_text(pantalla, "ARCADE EDITION", 20, MORADO, (210, 150))
    draw_text(pantalla, "PRESIONA ENTER PARA JUGAR", 18, BLANCO, (135, 240))
    draw_text(pantalla, f"RECORD: {record}", 18, ROSA, (230, 290))

    pygame.display.flip()


def draw_game(pantalla, serpiente, comida, puntuacion,
              game_over=False, record=0):
    """Dibuja la partida."""
    pantalla.fill(FONDO)
    draw_grid(pantalla)

    draw_snake(pantalla, serpiente)
    draw_food(pantalla, comida)

    draw_text(pantalla, f"SCORE: {puntuacion}", 18, TURQUESA, (15, 10))
    draw_text(pantalla, f"RECORD: {record}", 18, ROSA, (430, 10))

    if game_over:
        draw_text(pantalla, "GAME OVER", 42, ROSA, (185, 155))
        draw_text(
            pantalla,
            "PRESIONA R PARA REINICIAR",
            16,
            BLANCO,
            (145, 220)
        )

    pygame.display.flip()
