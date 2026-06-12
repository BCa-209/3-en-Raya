import pygame
from core.escena import Escena
from game.entities import Tablero, Cursor, X, O
from game.logic import TresEnRaya
from config import TECLA_IZQUIERDA, TECLA_DERECHA, TECLA_ARRIBA, TECLA_ABAJO, TECLA_ACEPTAR, TECLA_CANCELAR
class EscenaJuego(Escena):
    def __init__(self, game_state):
        self.game_state = game_state
        self.n = game_state.tam_tablero
        self.e = game_state.escala_celda  # se puede ajustar dinámicamente
        # Posición del tablero centrada
        ancho_tablero = self.n * 3 * self.e
        alto_tablero = self.n * 3 * self.e
        self.x_tablero = (game_state.ancho_pantalla - ancho_tablero) // 2
        self.y_tablero = 80

        self.tablero = Tablero(self.x_tablero, self.y_tablero, self.e, self.n)
        self.tablero.setColor((255,255,255))

        self.cursor = Cursor(self.n//2, self.n//2, self.n)  # inicio centrado
        self.juego = TresEnRaya(self.n)

        # Indicadores de turno (posiciones fijas, escala independiente)
        self.xTurno = X(320, 30, self.e//2)
        self.xTurno.setColor((255,0,0))
        self.oTurno = O(420, 30, self.e//2)
        self.oTurno.setColor((0,255,255))
        self.incXTurno = 0.5
        self.incYTurno = 0.5

    def input(self, evento):
        if self.juego.getGanador() != TresEnRaya.VACIO or self.juego.hayEmpate():
            return
        if evento.type != pygame.KEYDOWN:
            return

        if evento.key == TECLA_ARRIBA:
            self.cursor.moverArriba()
        elif evento.key == TECLA_ABAJO:
            self.cursor.moverAbajo()
        elif evento.key == TECLA_IZQUIERDA:
            self.cursor.moverIzquierda()
        elif evento.key == TECLA_DERECHA:
            self.cursor.moverDerecha()
        elif evento.key == TECLA_ACEPTAR:
            fila = self.cursor.getFila()
            columna = self.cursor.getColumna()
            if self.juego.jugar(fila, columna):
                # sonido de colocación (opcional)
                pass

    def update(self):
        if self.juego.getGanador() != TresEnRaya.VACIO:
            # Cambiar a escena de game over después de un breve retraso (opcional)
            from game.scenes.escena_game_over import GameOverScene
            self.game_state.cambiar_escena(GameOverScene(self.game_state, self.juego.getGanador()))
            return
        if self.juego.hayEmpate():
            from game.scenes.escena_game_over import GameOverScene
            self.game_state.cambiar_escena(GameOverScene(self.game_state, 0))
            return

        # Animación de indicador de turno
        if self.juego.getTurno() == TresEnRaya.FICHA_X:
            if self.xTurno.e >= 0.5*self.e or self.xTurno.e <= self.e//4:
                self.incXTurno = -self.incXTurno
            self.xTurno.e += self.incXTurno
        else:
            if self.oTurno.e >= 0.5*self.e or self.oTurno.e <= self.e//4:
                self.incYTurno = -self.incYTurno
            self.oTurno.e += self.incYTurno

    def render(self, pantalla):
        self.tablero.render(pantalla)
        # Dibujar cursor
        x = self.tablero.x + self.cursor.getColumna() * 3 * self.e
        y = self.tablero.y + self.cursor.getFila() * 3 * self.e
        self.cursor.render(pantalla, x, y, self.e, (255,255,0))

        matriz = self.juego.getMatriz()
        for fila in range(self.n):
            for columna in range(self.n):
                x = self.tablero.x + columna * 3 * self.e
                y = self.tablero.y + fila * 3 * self.e
                if matriz[fila][columna] == TresEnRaya.FICHA_X:
                    ficha = X(x, y, self.e)
                    ficha.setColor((255,0,0))
                    ficha.render(pantalla)
                elif matriz[fila][columna] == TresEnRaya.FICHA_O:
                    ficha = O(x, y, self.e)
                    ficha.setColor((0,255,255))
                    ficha.render(pantalla)

        self.xTurno.render(pantalla)
        self.oTurno.render(pantalla)

    def reiniciar(self):
        self.juego.reiniciar()
        self.cursor = Cursor(self.n//2, self.n//2)
        self.xTurno.alfa = 0
        self.oTurno.alfa = 0