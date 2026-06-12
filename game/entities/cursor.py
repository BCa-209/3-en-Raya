import pygame

class Cursor:
    def __init__(self, fila, columna, n=3):
        self.fila = fila
        self.columna = columna
        self.n = n
        self.visible = True
        self.contador_parpadeo = 0

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
    
    def update_animacion(self):
        """Parpadeo suave del cursor"""
        self.contador_parpadeo += 1
        if self.contador_parpadeo >= 30:  # Más lento
            self.contador_parpadeo = 0
            self.visible = not self.visible
    
    def render(self, pantalla, x, y, e, color):
        if not self.visible:
            return
        
        lienzo = pygame.Surface((3*e, 3*e), pygame.SRCALPHA)
        
        # Borde simple pero más grueso
        grosor = max(2, e // 8)
        rect = pygame.Rect(e//2, e//2, 2*e, 2*e)
        pygame.draw.rect(lienzo, color, rect, grosor)

        Rotacion = pygame.transform.rotate(lienzo, 0)
        Traslacion = Rotacion.get_rect(topleft=(x, y))
        pantalla.blit(Rotacion, Traslacion)