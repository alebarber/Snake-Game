import pygame
import sys
from config import *

## Función de recibe la pantalla de juego y crea el menú principal
def main_menu(screen):
    menu = True
    font_title = pygame.font.SysFont(None, 90)
    font_info = pygame.font.SysFont(None, 30)

    while menu:
        screen.fill(BLACK) # Fondo del menú

        title_text = font_title.render("Snake Game", True, GREEN)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//3))

        info_text = font_info.render("Presiona ENTER para empezar Fácil", True, WHITE)
        screen.blit(info_text, (WIDTH//2 - info_text.get_width()//2, HEIGHT//2))

        pygame.display.flip() # Actualizar pantalla

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Cerrar Pygame
                sys.exit() # Cerrar programa
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False  # salir del menú al juego
