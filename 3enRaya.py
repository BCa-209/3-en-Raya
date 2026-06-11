import pygame
import math

class Base:
    def __init__(self, x, y, e):
        self.x = x
        self.y = y
        self.e = e
        self.color = (255, 255, 255)
        self.alfa = 0

    def setColor(self, color):
        self.color = color

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def setEscala(self, e):
        self.e = e

class X(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)

    def render(self, pantalla):
        e=self.e
        lienzo = pygame.Surface((3*e,3*e), pygame.SRCALPHA)
        
        pygame.draw.line(lienzo,self.color,(0,0),(3*e,3*e),1)
        pygame.draw.line(lienzo,self.color,(3*e,0),(0,3*e),1)

        Rotacion = pygame.transform.rotate(lienzo,self.alfa)
        Traslacion = Rotacion.get_rect(topleft=(self.x,self.y))
        pantalla.blit(Rotacion,Traslacion)

class O(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)

    def render(self, pantalla):
        e=self.e
        lienzo = pygame.Surface((3*e,3*e), pygame.SRCALPHA)

        pygame.draw.circle(lienzo,self.color,(3*e/2,3*e/2),(3*e/2),1)

        Rotacion = pygame.transform.rotate(lienzo,self.alfa)
        Traslacion = Rotacion.get_rect(topleft=(self.x,self.y))
        pantalla.blit(Rotacion,Traslacion)

class Tablero(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)
    
    def render(self, pantalla):
        e=self.e
        lienzo = pygame.Surface((9*e,9*e), pygame.SRCALPHA)

        pygame.draw.line(lienzo,self.color,(3*e,0),(3*e,9*e),1)
        pygame.draw.line(lienzo,self.color,(6*e,0),(6*e,9*e),1)
        pygame.draw.line(lienzo,self.color,(0,3*e),(9*e,3*e),1)
        pygame.draw.line(lienzo,self.color,(0,6*e),(9*e,6*e),1)

        Rotacion = pygame.transform.rotate(lienzo,self.alfa)
        Traslacion = Rotacion.get_rect(topleft=(self.x,self.y))
        pantalla.blit(Rotacion,Traslacion)

class Cursor:
    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna
    
    def moverArriba(self):
        if self.fila > 0:
            self.fila -= 1

    def moverAbajo(self):
        if self.fila < 2:
            self.fila += 1

    def moverIzquierda(self):
        if self.columna > 0:
            self.columna -= 1

    def moverDerecha(self):
        if self.columna < 2:
            self.columna += 1

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
    
    def getPosicion(self):
        return (self.fila, self.columna)
    
    def render(self, pantalla,x,y,e,color):
        lienzo = pygame.Surface((3*e,3*e), pygame.SRCALPHA)

        pygame.draw.rect(lienzo,color,(e//2,e//2,2*e,2*e),1)

        Rotacion = pygame.transform.rotate(lienzo,0)
        Traslacion = Rotacion.get_rect(topleft=(x,y))
        pantalla.blit(Rotacion,Traslacion)

class TresEnRaya:

    VACIO = 0
    FICHA_X = 1
    FICHA_O = 2

    def __init__(self):

        self.matriz = [
            [self.VACIO, self.VACIO, self.VACIO],
            [self.VACIO, self.VACIO, self.VACIO],
            [self.VACIO, self.VACIO, self.VACIO]
        ]

        self.turno = self.FICHA_X
        self.ganador = self.VACIO

    def getMatriz(self):
        return self.matriz

    def getTurno(self):
        return self.turno

    def getGanador(self):
        return self.ganador

    def jugar(self, fila, columna):
        if self.matriz[fila][columna] != self.VACIO:
            return False

        self.matriz[fila][columna] = self.turno

        self.verificarGanador()

        if self.ganador == self.VACIO:
            if self.turno == self.FICHA_X:
                self.turno = self.FICHA_O
            else:
                self.turno = self.FICHA_X

        return True

    def verificarGanador(self):

        m = self.matriz

        for fila in range(3):
            if m[fila][0] != self.VACIO and \
               m[fila][0] == m[fila][1] == m[fila][2]:

                self.ganador = m[fila][0]
                return

        for columna in range(3):
            if m[0][columna] != self.VACIO and \
               m[0][columna] == m[1][columna] == m[2][columna]:

                self.ganador = m[0][columna]
                return

        if m[0][0] != self.VACIO and \
           m[0][0] == m[1][1] == m[2][2]:

            self.ganador = m[0][0]
            return

        if m[0][2] != self.VACIO and \
           m[0][2] == m[1][1] == m[2][0]:

            self.ganador = m[0][2]
            return

    def hayEmpate(self):

        if self.ganador != self.VACIO:
            return False

        for fila in self.matriz:
            for casilla in fila:
                if casilla == self.VACIO:
                    return False

        return True

    def reiniciar(self):

        self.matriz = [
            [self.VACIO, self.VACIO, self.VACIO],
            [self.VACIO, self.VACIO, self.VACIO],
            [self.VACIO, self.VACIO, self.VACIO]
        ]

        self.turno = self.FICHA_X
        self.ganador = self.VACIO

class EscenaTresEnRaya:

    def __init__(self):
        self.e = 30

        self.incXTurno = 0.5
        self.incYTurno = 0.5

        self.tablero = Tablero(10, 10, self.e)
        self.tablero.setColor((255,255,255))

        self.cursor = Cursor(1,1)

        self.juego = TresEnRaya()

        self.xTurno = X(320,50,self.e//2)
        self.xTurno.setColor((255,0,0))

        self.oTurno = O(420,50,self.e//2)
        self.oTurno.setColor((0,255,255))

    def input(self, evento):
        if evento.type != pygame.KEYDOWN:
            return

        if evento.key == pygame.K_UP:
            self.cursor.moverArriba()

        elif evento.key == pygame.K_DOWN:
            self.cursor.moverAbajo()

        elif evento.key == pygame.K_LEFT:
            self.cursor.moverIzquierda()

        elif evento.key == pygame.K_RIGHT:
            self.cursor.moverDerecha()

        elif evento.key == pygame.K_RETURN:

            fila = self.cursor.getFila()
            columna = self.cursor.getColumna()

            self.juego.jugar(fila,columna)

    def update(self):
        if self.juego.getGanador() != TresEnRaya.VACIO:
            return

        if self.juego.hayEmpate():
            return

        if self.juego.getTurno() == TresEnRaya.FICHA_X:
            if self.xTurno.e >= 0.5*self.e or self.xTurno.e <= self.e//4:
                self.incXTurno = -self.incXTurno
            self.xTurno.e += self.incXTurno
        else:
            if self.oTurno.e >= 0.5*self.e or self.oTurno.e <= self.e//4:
                self.incYTurno = -self.incYTurno
            self.oTurno.e += self.incYTurno

    def render(self,pantalla):
        self.tablero.render(pantalla)
        x = self.tablero.x + self.cursor.getColumna() * 3 * self.e
        y = self.tablero.y + self.cursor.getFila() * 3 * self.e

        self.cursor.render(pantalla,x,y,self.e,(255,255,0))

        matriz = self.juego.getMatriz()

        for fila in range(3):
            for columna in range(3):
                x = self.tablero.x + columna * 3 * self.e
                y = self.tablero.y + fila * 3 * self.e

                if matriz[fila][columna] == TresEnRaya.FICHA_X:
                    ficha = X(x,y,self.e)
                    ficha.setColor((255,0,0))
                    ficha.render(pantalla)

                elif matriz[fila][columna] == TresEnRaya.FICHA_O:
                    ficha = O(x,y,self.e)
                    ficha.setColor((0,255,255))
                    ficha.render(pantalla)

        self.xTurno.render(pantalla)
        self.oTurno.render(pantalla)

    def hayGanador(self):
        return self.juego.getGanador()

    def hayEmpate(self):
        return self.juego.hayEmpate()

    def reiniciar(self):

        self.juego.reiniciar()

        self.cursor = Cursor(1,1)

        self.xTurno.alfa = 0
        self.oTurno.alfa = 0

pygame.init()

ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("3 en Raya")

clock = pygame.time.Clock()

escena = EscenaTresEnRaya()

while True:
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        escena.input(evento)

    escena.update()

    pantalla.fill((0,0,0))

    escena.render(pantalla)

    pygame.display.flip()

    clock.tick(60)