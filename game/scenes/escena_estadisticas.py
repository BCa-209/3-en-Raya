import pygame
from core.escena import Escena
from config import ANCHO, ALTO, COLOR_BLANCO, COLOR_ROJO, COLOR_CYAN, COLOR_VERDE, COLOR_GRIS, TECLA_ACEPTAR, TECLA_CANCELAR

class EstadisticasScene(Escena):
    def __init__(self, game_state):
        self.game_state = game_state
        self.font_titulo = pygame.font.Font(None, 48)
        self.font_texto = pygame.font.Font(None, 32)
        self.font_pequena = pygame.font.Font(None, 24)

    def input(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == TECLA_CANCELAR or evento.key == TECLA_ACEPTAR:
                from game.scenes.escena_menu import MenuScene
                self.game_state.cambiar_escena(MenuScene(self.game_state))

    def update(self):
        pass

    def render(self, pantalla):
        pantalla.fill((0,0,0))
        
        # Título
        titulo = self.font_titulo.render("ESTADÍSTICAS DEL JUEGO", True, COLOR_BLANCO)
        pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 40))
        
        stats = self.game_state.get_estadisticas()
        
        # Recuadro de estadísticas
        y_base = 120
        espaciado = 50
        
        textos = [
            ("Partidas jugadas:", str(stats['partidas']), COLOR_BLANCO),
            ("Victorias de X:", str(stats['victorias_x']), COLOR_ROJO),
            ("Victorias de O:", str(stats['victorias_o']), COLOR_CYAN),
            ("Empates:", str(stats['empates']), COLOR_VERDE),
            ("", "", COLOR_BLANCO),
            ("Porcentaje de victorias X:", f"{stats['porcentaje_x']:.1f}%", COLOR_ROJO),
            ("Porcentaje de victorias O:", f"{stats['porcentaje_o']:.1f}%", COLOR_CYAN),
        ]
        
        for i, (label, value, color) in enumerate(textos):
            if label:
                texto_label = self.font_texto.render(label, True, COLOR_BLANCO)
                pantalla.blit(texto_label, (ANCHO//2 - 200, y_base + i * espaciado))
                texto_valor = self.font_texto.render(value, True, color)
                pantalla.blit(texto_valor, (ANCHO//2 + 50, y_base + i * espaciado))
        
        # Mensaje de salida
        instruccion = self.font_pequena.render("Presiona ENTER o ESC para volver al menú", True, COLOR_GRIS)
        pantalla.blit(instruccion, (ANCHO//2 - instruccion.get_width()//2, ALTO - 50))

    def reiniciar(self):
        pass