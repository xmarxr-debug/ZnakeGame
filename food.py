
import random


class Food:
    def __init__(self):
        self.size = 20
        self.position = (0, 0)
        self.respawn([])

    def respawn(self, snake_body):
        """Genera una nueva posición para la comida."""
        positions = []

        for x in range(0, 600, self.size):
            for y in range(0, 400, self.size):
                position = (x, y)

                if position not in snake_body:
                    positions.append(position)

        if positions:
            self.position = random.choice(positions)
