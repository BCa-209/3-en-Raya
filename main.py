import pygame
import sys
from config import ANCHO, ALTO, FPS, CAPTION, ESCALA_BASE, TAM_TABLERO_POR_DEFECTO
from game.scenes.escena_menu import MenuScene

class GameState:
    def __init__(self):
        self.ancho_pantalla = ANCHO
        self.alto_pantalla = ALTO
        self.tam_tablero = TAM_TABLERO_POR_DEFECTO
        self.escala_celda = ESCALA_BASE
        self.modo_infinito = False
        self.escena_actual = None

    def cambiar_escena(self, nueva_escena):
        self.escena_actual = nueva_escena

    def cambiar_tam_tablero(self, nuevo_tam):
        self.tam_tablero = nuevo_tam
        # Ajustar escala si es necesario (opcional)
        self.escala_celda = max(20, 60 - (nuevo_tam-3)*5)
    
    def cambiar_modo_infinito(self, infinito):
        self.modo_infinito = infinito

    def reiniciar_juego(self):
        # reinicia la lógica si es necesario
        pass

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
            pantalla.fill((0,0,0))
            game_state.escena_actual.render(pantalla)
        pygame.display.flip()

        clock.tick(FPS)

if __name__ == "__main__":
    main()