import pygame
import sys
from core.escena import Escena
from config import *

class MenuScene(Escena):
    def __init__(self, game_state):
        self.game_state = game_state  # para compartir datos entre escenas
        self.opciones = ["Iniciar Juego", "Modos de Juego", "Salir"]
        self.seleccion = 0
        self.font = pygame.font.Font(None, 36)

    def input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == TECLA_ARRIBA:
                self.seleccion = (self.seleccion - 1) % len(self.opciones)
            elif evento.key == TECLA_ABAJO:
                self.seleccion = (self.seleccion + 1) % len(self.opciones)
            elif evento.key == TECLA_ACEPTAR:
                self.seleccionar_opcion()

    def seleccionar_opcion(self):
        if self.opciones[self.seleccion] == "Iniciar Juego":
            from game.scenes.escena_juego import EscenaJuego
            self.game_state.cambiar_escena(EscenaJuego(self.game_state))
        elif self.opciones[self.seleccion] == "Modos de Juego":
            from game.scenes.escena_modo import ModoScene
            self.game_state.cambiar_escena(ModoScene(self.game_state))
        elif self.opciones[self.seleccion] == "Salir":
            pygame.quit()
            sys.exit()

    def update(self):
        pass

    def render(self, pantalla):
        pantalla.fill(COLOR_NEGRO)
        titulo = self.font.render("TRES EN RAYA PRO+", True, COLOR_BLANCO)
        pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 50))

        for i, opcion in enumerate(self.opciones):
            color = COLOR_AMARILLO if i == self.seleccion else COLOR_BLANCO
            texto = self.font.render(opcion, True, color)
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 150 + i * 50))

    def reiniciar(self):
        self.seleccion = 0