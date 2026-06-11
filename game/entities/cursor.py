import pygame

class Cursor:
    def __init__(self, fila, columna, n=3):
        self.fila = fila
        self.columna = columna
        self.n = n

    def moverArriba(self):
        if self.fila > 0:
            self.fila -= 1

    def moverAbajo(self):
        if self.fila < self.n - 1:
            self.fila += 1

    def moverIzquierda(self):
        if self.columna > 0:
            self.columna -= 1

    def moverDerecha(self):
        if self.columna < self.n - 1:
            self.columna += 1

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
    
    def getPosicion(self):
        return (self.fila, self.columna)
    
    def render(self, pantalla, x, y, e, color):
        lienzo = pygame.Surface((3*e, 3*e), pygame.SRCALPHA)
        pygame.draw.rect(lienzo, color, (e//2, e//2, 2*e, 2*e), 1)
        Rotacion = pygame.transform.rotate(lienzo, 0)
        Traslacion = Rotacion.get_rect(topleft=(x, y))
        pantalla.blit(Rotacion, Traslacion)