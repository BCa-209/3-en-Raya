import pygame
from core.escena import Escena
from config import ANCHO, ALTO, COLOR_BLANCO, COLOR_ROJO, COLOR_CYAN, TECLA_IZQUIERDA, TECLA_DERECHA, TECLA_ARRIBA, TECLA_ABAJO, TECLA_ACEPTAR, TECLA_CANCELAR

class GameOverScene(Escena):
    def __init__(self, game_state, ganador):
        self.game_state = game_state
        self.ganador = ganador  # 1 -> X, 2 -> O, 0 -> empate
        self.font_grande = pygame.font.Font(None, 72)
        self.font_pequena = pygame.font.Font(None, 36)

    def input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == TECLA_ACEPTAR or evento.key == TECLA_CANCELAR:
                # Volver al menú principal o reiniciar juego
                from game.scenes.escena_menu import MenuScene
                self.game_state.reiniciar_juego()  # opcional: reinicia el estado interno
                self.game_state.cambiar_escena(MenuScene(self.game_state))

    def update(self):
        # Podrías agregar animaciones o efectos aquí
        pass

    def render(self, pantalla):
        pantalla.fill((0,0,0))
        if self.ganador == 1:
            texto = self.font_grande.render("¡Jugador X Gana!", True, COLOR_ROJO)
        elif self.ganador == 2:
            texto = self.font_grande.render("¡Jugador O Gana!", True, COLOR_CYAN)
        else:
            texto = self.font_grande.render("¡Empate!", True, COLOR_BLANCO)

        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, ALTO//2 - 50))

        instruccion = self.font_pequena.render("Presiona ENTER o ESPACIO para continuar", True, COLOR_BLANCO)
        pantalla.blit(instruccion, (ANCHO//2 - instruccion.get_width()//2, ALTO - 80))

    def reiniciar(self):
        pass