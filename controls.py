
import pygame

def handle_events(snake, game_over=False):
    reiniciar = False

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            return False, False

        if evento.type == pygame.KEYDOWN:

            # Si terminó la partida, permitir reiniciar
            if game_over:
                if evento.key == pygame.K_r:
                    reiniciar = True
                continue

            # Controles de movimiento
            if evento.key == pygame.K_UP:
                if snake.direction != (0, 20):
                    snake.direction = (0, -20)

            elif evento.key == pygame.K_DOWN:
                if snake.direction != (0, -20):
                    snake.direction = (0, 20)

            elif evento.key == pygame.K_LEFT:
                if snake.direction != (20, 0):
                    snake.direction = (-20, 0)

            elif evento.key == pygame.K_RIGHT:
                if snake.direction != (-20, 0):
                    snake.direction = (20, 0)

    return True, reiniciar

