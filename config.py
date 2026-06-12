"""Constantes globales del juego"""

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Configuración de Pygame
FPS = 60
CAPTION = "3 en Raya"

# Colores (formato RGB)
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
COLOR_GRIS = (128, 128, 128)

COLOR_ROJO = (255, 0, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_AMARILLO = (255, 255, 0)
COLOR_VERDE = (0, 255, 0)

# Configuración del juego
ESCALA_BASE = 30
TAM_TABLERO_POR_DEFECTO = 3

# Teclas
import pygame
TECLA_IZQUIERDA = pygame.K_LEFT
TECLA_DERECHA = pygame.K_RIGHT
TECLA_ARRIBA = pygame.K_UP
TECLA_ABAJO = pygame.K_DOWN
TECLA_ACEPTAR = pygame.K_SPACE
TECLA_CANCELAR = pygame.K_ESCAPE
TECLA_REINICIAR = pygame.K_r

TECLAS = [
    TECLA_IZQUIERDA, 
    TECLA_DERECHA, 
    TECLA_ARRIBA, 
    TECLA_ABAJO, 
    TECLA_ACEPTAR, 
    TECLA_CANCELAR
]

COLORES = [
    COLOR_BLANCO, 
    COLOR_NEGRO, 
    COLOR_ROJO, 
    COLOR_CYAN, 
    COLOR_AMARILLO, 
    COLOR_VERDE
]

