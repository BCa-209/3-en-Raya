import pygame
import sys
from core.escena import Escena
from config import *

class MenuScene(Escena):
    def __init__(self, game_state):
        self.game_state = game_state  # para compartir datos entre escenas
        self.opciones = ["Iniciar Juego", "Modos de Juego", "Configuración", "Ver Estadísticas", "Salir"]
        self.seleccion = 0
        self.font_grande = pygame.font.Font(None, 48)
        self.font_mediana = pygame.font.Font(None, 36)
        self.font_pequeno = pygame.font.Font(None, 28)

    def input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == TECLA_ARRIBA:
                self.seleccion = (self.seleccion - 1) % len(self.opciones)
                self.game_state.reproducir_sonido('movimiento')
            elif evento.key == TECLA_ABAJO:
                self.seleccion = (self.seleccion + 1) % len(self.opciones)
                self.game_state.reproducir_sonido('movimiento')
            elif evento.key == TECLA_ACEPTAR:
                self.game_state.reproducir_sonido('seleccion')
                self.seleccionar_opcion()

    def seleccionar_opcion(self):
        if self.opciones[self.seleccion] == "Iniciar Juego":
            from game.scenes.escena_juego import EscenaJuego
            self.game_state.crear_nuevo_juego()
            self.game_state.cambiar_escena(EscenaJuego(self.game_state))

        elif self.opciones[self.seleccion] == "Modos de Juego":
            from game.scenes.escena_modo import ModoScene
            self.game_state.cambiar_escena(ModoScene(self.game_state))

        elif self.opciones[self.seleccion] == "Configuración":
            from game.scenes.escena_config import ConfiguracionScene
            self.game_state.cambiar_escena(ConfiguracionScene(self.game_state))

        elif self.opciones[self.seleccion] == "Ver Estadísticas":
            from game.scenes.escena_estadisticas import EstadisticasScene
            self.game_state.cambiar_escena(EstadisticasScene(self.game_state))

        elif self.opciones[self.seleccion] == "Salir":
            pygame.quit()
            sys.exit()

    def update(self):
        pass

    def render(self, pantalla):
        pantalla.fill(COLOR_NEGRO)
        titulo = self.font_grande.render("TRES EN RAYA PRO+", True, COLOR_BLANCO)
        pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 50))

        for i, opcion in enumerate(self.opciones):
            color = COLOR_AMARILLO if i == self.seleccion else COLOR_BLANCO
            texto = self.font_mediana.render(opcion, True, color)
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, 150 + i * 50))

        # Mostrar estadísticas resumidas en la parte inferior
        stats = self.game_state.get_estadisticas()
        y_stats = ALTO - 100
        stats_texto = f"Partidas: {stats['partidas']} | X: {stats['victorias_x']} | O: {stats['victorias_o']} | Empates: {stats['empates']}"
        texto_stats = self.font_pequeno.render(stats_texto, True, COLOR_VERDE)
        pantalla.blit(texto_stats, (ANCHO//2 - texto_stats.get_width()//2, y_stats))
        
        # Instrucción
        instruccion = self.font_pequeno.render("↑ ↓ para mover | ENTER para seleccionar", True, COLOR_GRIS)
        pantalla.blit(instruccion, (ANCHO//2 - instruccion.get_width()//2, ALTO - 30))

    def reiniciar(self):
        self.seleccion = 0