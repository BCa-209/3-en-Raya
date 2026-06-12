"""Constantes globales del juego"""

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Configuración de Pygame
FPS = 60
CAPTION = "3 en Raya Pro+"

# Colores (formato RGB)
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
COLOR_GRIS = (128, 128, 128)
COLOR_GRIS_CLARO = (200, 200, 200)

COLOR_ROJO = (255, 0, 0)
COLOR_AZUL = (0, 0, 255)
COLOR_VERDE = (0, 255, 0)
COLOR_AMARILLO = (255, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_MAGENTA = (255, 0, 255)
COLOR_NARANJA = (255, 165, 0)
COLOR_ROSA = (255, 192, 203)
COLOR_MORADO = (128, 0, 128)


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

COLORES_FICHAS = [
    ("Rojo", COLOR_ROJO),
    ("Azul", COLOR_AZUL),
    ("Verde", COLOR_VERDE),
    ("Amarillo", COLOR_AMARILLO),
    ("Cyan", COLOR_CYAN),
    ("Magenta", COLOR_MAGENTA),
    ("Naranja", COLOR_NARANJA),
    ("Rosa", COLOR_ROSA),
    ("Morado", COLOR_MORADO),
    ("Blanco", COLOR_BLANCO),
]

COLORES_CURSOR = [
    ("Amarillo", COLOR_AMARILLO),
    ("Blanco", COLOR_BLANCO),
    ("Cyan", COLOR_CYAN),
    ("Verde", COLOR_VERDE),
    ("Rojo", COLOR_ROJO)
]
