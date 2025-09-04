# snake.py

from config import GRID_WIDTH, GRID_HEIGHT

class Snake:
    def __init__(self):
        # Lista de coordenadas de la serpiente
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
    # Función para evitar invertir la dirección instantáneamente
    def change_direction(self, new_dir):
        opposites = {"UP":"DOWN", "DOWN":"UP", "LEFT":"RIGHT", "RIGHT":"LEFT"}
        if new_dir != opposites[self.direction]:
            self.next_direction = new_dir

    # Función para mover la serpiente
    def move(self):
        self.direction = self.next_direction
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        new_head = (head_x, head_y)
        self.body.insert(0, new_head)
        return new_head

    # Función para eliminar la cola (si no come)
    def shrink(self):
        self.body.pop()

    # Función para comprobar colisiones
    def check_collision(self):
        head = self.body[0]
        x, y = head
        # Bordes
        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
            return True
        # Auto-colisión
        if head in self.body[1:]:
            return True
        return False
