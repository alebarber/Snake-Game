import random
from config import GRID_WIDTH, GRID_HEIGHT

class Food:

    def __init__(self, snake_body=[]):
        self.positions = [] #Lista de posiciones de manzanas     
        self.positions.append(self.spawn(snake_body)) # Añadir la primera manzana


    # Función para buscar una posición valida para colocar manzana
    def spawn(self, snake_body=[]):
        libres = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            ## Comprobar que la posición es válida (no está ocupada por 
            ## el cuerpo de la serpiente o por otra manzana)
            if (x, y) not in snake_body and (x, y) not in self.positions
        ]
        if not libres:
            return None  # mapa lleno
        return random.choice(libres)
    

    # Función para añadir manzanas al mapa (normalmente mas de una)
    def add_food(self, amount=1, snake_body=[]):
        for _ in range(amount):
            pos = self.spawn(snake_body)
            if pos is None:
                return False  # mapa lleno
            self.positions.append(pos)
        return True