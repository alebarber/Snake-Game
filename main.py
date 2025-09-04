# main.py
import pygame
import sys
from config import *
from snake import Snake
from food import Food
from menu import main_menu


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Configurar ventana
pygame.display.set_caption("Snake Modular")
clock = pygame.time.Clock() # Controlar FPS

main_menu(screen) # Mostrar menú principal

snake = Snake()
food = Food(snake.body)
game_over = False # Crear variable de estado del juego
victory = False # Crear variable de estado de victoria

# Timer para movimiento
MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, MOVE_INTERVAL)

while True:
    for event in pygame.event.get():
        # Salir del juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mover la serpiente cada MOVE_INTERVAL ms
        elif event.type == MOVE_EVENT and not game_over and not victory:
            # Mover serpiente
            new_head = snake.move()

            # Comprobar colisiones
            if snake.check_collision():
                game_over = True

            # Comprobar si comió comida
            elif new_head in food.positions:
                # Comer comida: eliminar la que tocó y añadir 2 nuevas
                food.positions.remove(new_head)
                success = food.add_food(amount=2, snake_body=snake.body)
                if not success:
                    victory = True

            else:
                snake.shrink()  # no comer, eliminar cola

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
            elif event.key == pygame.K_r and (game_over or victory):
                # Reiniciar juego
                snake = Snake()
                food = Food(snake.body)
                game_over = False
                victory = False

    # Fondo negro
    screen.fill(BLACK)

    # Dibujar cuadrícula
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, DARK_GRAY, rect, 1)

    # Dibujar la cabeza de la serpiente
    head = snake.body[0]
    hx, hy = head[0] * CELL_SIZE, head[1] * CELL_SIZE
    rect = pygame.Rect(hx, hy, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, DARK_GREEN, rect)

    # Dibujar los ojos dentro de la cabeza
    eye_radius = CELL_SIZE // 6
    eye_offset_x = CELL_SIZE // 4
    eye_offset_y = CELL_SIZE // 4
    pygame.draw.circle(screen, (0,0,0), (hx + eye_offset_x, hy + eye_offset_y), eye_radius)
    pygame.draw.circle(screen, (0,0,0), (hx + 3*eye_offset_x, hy + eye_offset_y), eye_radius)



    # Dibujar el resto del cuerpo
    for segment in snake.body[1:]:
        rect = pygame.Rect(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

    # Dibujar todas las manzanas
    for fx, fy in food.positions:
        rect = pygame.Rect(fx*CELL_SIZE, fy*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)

    # Mensaje Game Over
    if game_over:
        font = pygame.font.SysFont(None, 30)
        text = font.render("GAME OVER! Presiona R para reiniciar", True, WHITE)
        x = WIDTH // 2 - text.get_width() // 2
        y = HEIGHT // 2 - text.get_height() // 2
        screen.blit(text, (x, y))
    elif victory:
        font = pygame.font.SysFont(None, 30)
        text = font.render("¡Ganaste! 🎉 Presiona R para reiniciar", True, GREEN)
        x = WIDTH // 2 - text.get_width() // 2
        y = HEIGHT // 2 - text.get_height() // 2
        screen.blit(text, (x, y))

    pygame.display.flip() # Actualizar pantalla
    clock.tick(FPS) # Mantener FPS
