
import pygame

def handle_events(snake):
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            return False

        if evento.type == pygame.KEYDOWN:

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

    return True
