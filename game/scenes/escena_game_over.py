import pygame
from core.escena import Escena
from config import ANCHO, ALTO, COLOR_BLANCO, COLOR_NEGRO, COLOR_ROJO, COLOR_CYAN, TECLA_ACEPTAR, COLOR_GRIS, TECLA_REINICIAR

class GameOverScene(Escena):
    def __init__(self, game_state, ganador):
        self.game_state = game_state
        self.ganador = ganador  # 1 -> X, 2 -> O, 0 -> empate
        self.font_grande = pygame.font.Font(None, 72)
        self.font_mediana = pygame.font.Font(None, 48)
        self.font_pequena = pygame.font.Font(None, 36)

        if ganador == 1 :
            self.game_state.registrar_victoria_x()
        elif ganador == 2:
            self.game_state.registrar_victoria_o()
        else:
            self.game_state.registrar_empate()

    def input(self, evento):
            if evento.type == pygame.KEYDOWN:
                if evento.key == TECLA_ACEPTAR:
                    # Volver al menú principal
                    from game.scenes.escena_menu import MenuScene
                    self.game_state.cambiar_escena(MenuScene(self.game_state))
                elif evento.key == TECLA_REINICIAR:
                    # Reiniciar la misma partida (mismo modo)
                    from game.scenes.escena_juego import EscenaJuego
                    self.game_state.crear_nuevo_juego()
                    self.game_state.cambiar_escena(EscenaJuego(self.game_state))

    def update(self):
        # Podrías agregar animaciones o efectos aquí
        pass

    def render(self, pantalla):
        pantalla.fill(COLOR_NEGRO)
        if self.ganador == 1:
            texto = self.font_grande.render("¡Jugador X Gana!", True, COLOR_ROJO)
        elif self.ganador == 2:
            texto = self.font_grande.render("¡Jugador O Gana!", True, COLOR_CYAN)
        else:
            texto = self.font_grande.render("¡Empate!", True, COLOR_BLANCO)

        pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, ALTO//2 - 50))

        # Mostrar estadísticas actualizadas
        stats = self.game_state.get_estadisticas()
        texto_stats = self.font_mediana.render(f"X: {stats['victorias_x']}  |  O: {stats['victorias_o']}  |  Empates: {stats['empates']}", True, COLOR_BLANCO)
        pantalla.blit(texto_stats, (ANCHO//2 - texto_stats.get_width()//2, ALTO//2))
        
        # Opciones
        reinicio = self.font_pequena.render("Presiona ENTER o ESPACIO para volver al menú", True, COLOR_BLANCO)
        pantalla.blit(reinicio, (ANCHO//2 - reinicio.get_width()//2, ALTO - 80))
        
        reinicio_mismo = self.font_pequena.render("Presiona R para jugar de nuevo (mismo modo)", True, COLOR_GRIS)
        pantalla.blit(reinicio_mismo, (ANCHO//2 - reinicio_mismo.get_width()//2, ALTO - 50))

    def reiniciar(self):
        pass