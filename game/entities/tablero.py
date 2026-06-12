import pygame
from core.entidad_base import Base

class Tablero(Base):
    def __init__(self, x, y, e, n=3):
        super().__init__(x, y, e)
        self.n = n

    def render(self, pantalla):
        e = self.e
        n = self.n
        lienzo = pygame.Surface((3*n*e, 3*n*e), pygame.SRCALPHA)
        
        # Grosor de líneas (un poco más grueso que antes)
        grosor = max(2, e // 8)
        
        # Dibujar líneas verticales
        for i in range(1, n):
            pygame.draw.line(lienzo, self.color, 
                           (3*i*e, 0), 
                           (3*i*e, 3*n*e), 
                           grosor)
        
        # Dibujar líneas horizontales
        for i in range(1, n):
            pygame.draw.line(lienzo, self.color, 
                           (0, 3*i*e), 
                           (3*n*e, 3*i*e), 
                           grosor)

        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(topleft=(self.x, self.y))
        pantalla.blit(Rotacion, Traslacion)