import pygame
import sys
from config import ANCHO, ALTO, COLOR_NEGRO, FPS, CAPTION, ESCALA_BASE, TAM_TABLERO_POR_DEFECTO, COLORES_FICHAS, COLORES_CURSOR
from game.scenes.escena_menu import MenuScene
from game.sounds.sonidos import SoundManager

class GameState:
    def __init__(self):
        self.ancho_pantalla = ANCHO
        self.alto_pantalla = ALTO
        self.tam_tablero = TAM_TABLERO_POR_DEFECTO
        self.escala_celda = ESCALA_BASE
        self.modo_infinito = False
        self.escena_actual = None
    
        # config colores
        self.color_x_idx = 0
        self.color_x = COLORES_FICHAS[0][1]
        self.color_o_idx = 3
        self.color_o = COLORES_FICHAS[3][1]
        self.cursor_color_idx = 0
        self.cursor_color = COLORES_CURSOR[0][1]

        # estadisticas globales
        self.partidas_jugadas = 0
        self.victorias_x = 0
        self.victorias_o = 0
        self.empates = 0

        # sonidos
        print("iniciando sonidosssssss")
        self.sonidos = SoundManager()
        self.sonido_activado = True

        # control sonido
        self.sonido_activado = True
    
    def toggle_sonido(self):
        """Activar/desactivar sonidos"""
        self.sonido_activado = not self.sonido_activado
        if not self.sonido_activado:
            self.sonidos.detener_todos()
        print(f"Sonido {'activado' if self.sonido_activado else 'desactivado'}")
    
    def reproducir_sonido(self, nombre):
        """Reproducir sonido si está activado"""
        if self.sonido_activado:
            self.sonidos.reproducir(nombre)

    def cambiar_escena(self, nueva_escena):
        self.escena_actual = nueva_escena

    def cambiar_tam_tablero(self, nuevo_tam):
        self.tam_tablero = nuevo_tam
        # Ajustar escala si es necesario (opcional)
        max_celdas = max(3, nuevo_tam)
        self.escala_celda = max(15, min(35, 300 // (3 * max_celdas) * 10))
    
    def cambiar_modo_infinito(self, infinito):
        self.modo_infinito = infinito

    def reiniciar_juego(self):
        # reinicia la lógica si es necesario
        pass

    def crear_nuevo_juego(self):
        """Crea una nueva instancia del juego (mantiene estadísticas)"""
        pass

    def registrar_victoria_x(self):
        self.partidas_jugadas += 1
        self.victorias_x += 1

    def registrar_victoria_o(self):
        self.partidas_jugadas += 1
        self.victorias_o += 1

    def registrar_empate(self):
        self.partidas_jugadas += 1
        self.empates += 1

    def reiniciar_estadisticas(self):
        """Reinicia todas las estadísticas (cuando se cambia de modo)"""
        self.partidas_jugadas = 0
        self.victorias_x = 0
        self.victorias_o = 0
        self.empates = 0

    def get_estadisticas(self):
        total = self.partidas_jugadas
        porcentaje_x = (self.victorias_x / total * 100) if total > 0 else 0
        porcentaje_o = (self.victorias_o / total * 100) if total > 0 else 0
        return {
            'partidas': self.partidas_jugadas,
            'victorias_x': self.victorias_x,
            'victorias_o': self.victorias_o,
            'empates': self.empates,
            'porcentaje_x': porcentaje_x,
            'porcentaje_o': porcentaje_o
        }

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    game_state = GameState()
    game_state.cambiar_escena(MenuScene(game_state))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_state.escena_actual:
                game_state.escena_actual.input(evento)

        if game_state.escena_actual:
            game_state.escena_actual.update()
            pantalla.fill(COLOR_NEGRO)
            game_state.escena_actual.render(pantalla)
            pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()