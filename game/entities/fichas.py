import pygame
from core.entidad_base import Base

class X(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)

    def render(self, pantalla):
        e = self.e
        lienzo = pygame.Surface((3*e, 3*e), pygame.SRCALPHA)
        
        pygame.draw.line(lienzo, self.color, (0, 0), (3*e, 3*e), 1)
        pygame.draw.line(lienzo, self.color, (3*e, 0), (0, 3*e), 1)

        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(topleft=(self.x, self.y))
        pantalla.blit(Rotacion, Traslacion)


class O(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)

    def render(self, pantalla):
        e = self.e
        lienzo = pygame.Surface((3*e, 3*e), pygame.SRCALPHA)
        pygame.draw.circle(lienzo, self.color, (3*e/2, 3*e/2), (3*e/2), 1)

        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(topleft=(self.x, self.y))
        pantalla.blit(Rotacion, Traslacion)