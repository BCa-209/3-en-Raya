import pygame
from core.entidad_base import Base

class Tablero(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)
    
    def render(self, pantalla):
        e = self.e
        lienzo = pygame.Surface((9*e, 9*e), pygame.SRCALPHA)

        pygame.draw.line(lienzo, self.color, (3*e, 0), (3*e, 9*e), 1)
        pygame.draw.line(lienzo, self.color, (6*e, 0), (6*e, 9*e), 1)
        pygame.draw.line(lienzo, self.color, (0, 3*e), (9*e, 3*e), 1)
        pygame.draw.line(lienzo, self.color, (0, 6*e), (9*e, 6*e), 1)

        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(topleft=(self.x, self.y))
        pantalla.blit(Rotacion, Traslacion)