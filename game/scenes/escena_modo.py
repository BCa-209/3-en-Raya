import pygame
from core.escena import Escena
from config import *

class ModoScene(Escena):
    def __init__(self, game_state):
        self.game_state = game_state
        self.opciones = [
            ("3x3 Clásico", 3, False),
            ("4x4 Clásico", 4, False),
            ("5x5 Clásico", 5, False),
            ("Infinito (3x3)", 3, True),
        ]
        self.seleccion = 0
        self.font = pygame.font.Font(None, 36)

    def input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == TECLA_ARRIBA:
                self.seleccion = (self.seleccion - 1) % len(self.opciones)
            elif evento.key == TECLA_ABAJO:
                self.seleccion = (self.seleccion + 1) % len(self.opciones)
            elif evento.key == TECLA_ACEPTAR:
                _, tam, infinito = self.opciones[self.seleccion]
                self.game_state.cambiar_tam_tablero(tam)
                self.game_state.cambiar_modo_infinito(infinito)
                from game.scenes.escena_menu import MenuScene
                self.game_state.cambiar_escena(MenuScene(self.game_state))
            elif evento.key == TECLA_CANCELAR:
                from game.scenes.escena_menu import MenuScene
                self.game_state.cambiar_escena(MenuScene(self.game_state))

    def render(self, pantalla):
        pantalla.fill((0,0,0))
        titulo = self.font.render("Selecciona modo de juego", True, COLOR_BLANCO)
        pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 50))

        for i, (texto, _, _) in enumerate(self.opciones):
            color = COLOR_VERDE if i == self.seleccion else COLOR_BLANCO
            txt = self.font.render(texto, True, color)
            pantalla.blit(txt, (ANCHO//2 - txt.get_width()//2, 150 + i * 50))

        ayuda = self.font.render("ARRIBA/ABAJO: mover   ESPACIO: elegir   ESC: volver", True, COLOR_BLANCO)
        pantalla.blit(ayuda, (ANCHO//2 - ayuda.get_width()//2, ALTO - 50))

    def reiniciar(self):
        self.seleccion = 0

    def update(self):
        pass
