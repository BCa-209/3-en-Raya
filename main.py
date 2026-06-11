import pygame
import sys
from config import ANCHO, ALTO, FPS, CAPTION
from game.scenes import EscenaJuego

def main():
    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(CAPTION)

    clock = pygame.time.Clock()
    escena = EscenaJuego()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            escena.input(evento)

        escena.update()

        pantalla.fill((0, 0, 0))
        escena.render(pantalla)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()