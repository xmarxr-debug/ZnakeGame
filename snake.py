
class Snake:
    def __init__(self):
        # Posición inicial de la serpiente
        self.body = [
            (100, 200),
            (80, 200),
            (60, 200)
        ]

        # Dirección inicial: hacia la derecha
        self.direction = (20, 0)

        # Tamaño de cada segmento
        self.size = 20

    def move(self, grow=False):
        # Obtener la posición de la cabeza
        x, y = self.body[0]

        # Calcular la nueva posición
        dx, dy = self.direction

        new_head = (x + dx, y + dy)

        # Agregar la nueva cabeza
        self.body.insert(0, new_head)

        # Si no comió, eliminar el último segmento
        if not grow:
            self.body.pop()

    def change_direction(self, new_direction):
        # Evitar que la serpiente se mueva
        # directamente en dirección contraria
        opposite = (
            -self.direction[0],
            -self.direction[1]
        )

        if new_direction != opposite:
            self.direction = new_direction

    def grow(self):
        # El crecimiento se controla desde move()
        self.move(grow=True)

    def check_collision(self, width=600, height=400):
        head = self.body[0]

        x, y = head

        # Comprobar colisión con las paredes
        if x < 0 or x >= width or y < 0 or y >= height:
            return True

        # Comprobar colisión con el propio cuerpo
        if head in self.body[1:]:
            return True

        return False
