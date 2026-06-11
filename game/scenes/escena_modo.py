import pygame
from core.escena import Escena
from config import ANCHO, ALTO, COLOR_BLANCO, COLOR_VERDE

class ModoScene(Escena):
    def __init__(self, game_state):
        self.game_state = game_state
        self.tamanos = [3, 4, 5]  # opciones: 3x3, 4x4, 5x5
        self.seleccion = self.tamanos.index(self.game_state.tam_tablero)
        self.font = pygame.font.Font(None, 36)

    def input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                self.seleccion = (self.seleccion - 1) % len(self.tamanos)
            elif evento.key == pygame.K_RIGHT:
                self.seleccion = (self.seleccion + 1) % len(self.tamanos)
            elif evento.key == pygame.K_RETURN:
                nuevo_tam = self.tamanos[self.seleccion]
                self.game_state.cambiar_tam_tablero(nuevo_tam)
                from game.scenes.menu_scene import MenuScene
                self.game_state.cambiar_escena(MenuScene(self.game_state))
            elif evento.key == pygame.K_ESCAPE:
                from game.scenes.menu_scene import MenuScene
                self.game_state.cambiar_escena(MenuScene(self.game_state))

    def update(self):
        pass

    def render(self, pantalla):
        pantalla.fill((0,0,0))
        texto = self.font.render("Selecciona tamaño del tablero:", True, COLOR_BLANCO)
        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 100))

        for i, tam in enumerate(self.tamanos):
            color = COLOR_VERDE if i == self.seleccion else COLOR_BLANCO
            txt = self.font.render(f"{tam} x {tam}", True, color)
            x = ANCHO//2 + (i - 1) * 120
            pantalla.blit(txt, (x - txt.get_width()//2, 200))

        ayuda = self.font.render("← →  mover   ENTER: elegir   ESC: volver", True, COLOR_BLANCO)
        pantalla.blit(ayuda, (ANCHO//2 - ayuda.get_width()//2, ALTO - 50))

    def reiniciar(self):
        self.seleccion = self.tamanos.index(self.game_state.tam_tablero)