import pygame
from core.escena import Escena
from game.entities import Tablero, Cursor, X, O
from game.logic import TresEnRaya

class EscenaJuego(Escena):
    """Orquestador principal de la escena de juego"""

    def __init__(self, e=30):
        self.e = e
        self.incXTurno = 0.5
        self.incYTurno = 0.5

        self.tablero = Tablero(10, 10, self.e)
        self.tablero.setColor((255, 255, 255))

        self.cursor = Cursor(1, 1)
        self.juego = TresEnRaya()

        self.xTurno = X(320, 50, self.e // 2)
        self.xTurno.setColor((255, 0, 0))

        self.oTurno = O(420, 50, self.e // 2)
        self.oTurno.setColor((0, 255, 255))

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
        elif evento.key == pygame.K_SPACE:
            fila = self.cursor.getFila()
            columna = self.cursor.getColumna()
            self.juego.jugar(fila, columna)

    def update(self):
        if self.juego.getGanador() != TresEnRaya.VACIO:
            return

        if self.juego.hayEmpate():
            return

        if self.juego.getTurno() == TresEnRaya.FICHA_X:
            if self.xTurno.e >= 0.5 * self.e or self.xTurno.e <= self.e // 4:
                self.incXTurno = -self.incXTurno
            self.xTurno.e += self.incXTurno
        else:
            if self.oTurno.e >= 0.5 * self.e or self.oTurno.e <= self.e // 4:
                self.incYTurno = -self.incYTurno
            self.oTurno.e += self.incYTurno

    def render(self, pantalla):
        self.tablero.render(pantalla)

        x = self.tablero.x + self.cursor.getColumna() * 3 * self.e
        y = self.tablero.y + self.cursor.getFila() * 3 * self.e
        self.cursor.render(pantalla, x, y, self.e, (255, 255, 0))

        matriz = self.juego.getMatriz()

        for fila in range(3):
            for columna in range(3):
                x = self.tablero.x + columna * 3 * self.e
                y = self.tablero.y + fila * 3 * self.e

                if matriz[fila][columna] == TresEnRaya.FICHA_X:
                    ficha = X(x, y, self.e)
                    ficha.setColor((255, 0, 0))
                    ficha.render(pantalla)
                elif matriz[fila][columna] == TresEnRaya.FICHA_O:
                    ficha = O(x, y, self.e)
                    ficha.setColor((0, 255, 255))
                    ficha.render(pantalla)

        self.xTurno.render(pantalla)
        self.oTurno.render(pantalla)

    def hayGanador(self):
        return self.juego.getGanador()

    def hayEmpate(self):
        return self.juego.hayEmpate()

    def reiniciar(self):
        self.juego.reiniciar()
        self.cursor = Cursor(1, 1)
        self.xTurno.alfa = 0
        self.oTurno.alfa = 0