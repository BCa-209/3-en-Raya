import pygame
from core.escena import Escena
from game.entities import Tablero, Cursor, X, O
from game.logic import TresEnRaya
from config import *

class EscenaJuego(Escena):
    def __init__(self, game_state):
        self.game_state = game_state
        self.n = game_state.tam_tablero
        self.e = game_state.escala_celda
        
        # Posición del tablero centrada
        ancho_tablero = self.n * 3 * self.e
        alto_tablero = self.n * 3 * self.e
        self.x_tablero = (game_state.ancho_pantalla - ancho_tablero) // 2
        self.y_tablero = 80

        self.tablero = Tablero(self.x_tablero, self.y_tablero, self.e, self.n)
        self.tablero.setColor(COLOR_BLANCO)

        self.cursor = Cursor(self.n//2, self.n//2, self.n)
        self.juego = TresEnRaya(self.n, infinito=game_state.modo_infinito)

        # Indicadores de turno
        self.xTurno = X(50, 30, self.e//2)
        self.xTurno.setColor(self.game_state.color_x)
        self.oTurno = O(ANCHO - 80, 30, self.e//2)
        self.oTurno.setColor(self.game_state.color_o)

    def input(self, evento):
        if self.juego.getGanador() != TresEnRaya.VACIO or self.juego.hayEmpate():
            return
        if evento.type != pygame.KEYDOWN:
            return

        if evento.key == TECLA_ARRIBA:
            self.cursor.moverArriba()
            self.game_state.reproducir_sonido('movimiento')
        elif evento.key == TECLA_ABAJO:
            self.cursor.moverAbajo()
            self.game_state.reproducir_sonido('movimiento')
        elif evento.key == TECLA_IZQUIERDA:
            self.cursor.moverIzquierda()
            self.game_state.reproducir_sonido('movimiento')
        elif evento.key == TECLA_DERECHA:
            self.cursor.moverDerecha()
            self.game_state.reproducir_sonido('movimiento')
        elif evento.key == TECLA_ACEPTAR:
            fila = self.cursor.getFila()
            columna = self.cursor.getColumna()
            if self.juego.jugar(fila, columna):
                self.game_state.reproducir_sonido('colocar')
            else:
                self.game_state.reproducir_sonido('error')

    def update(self):
        # Verificar fin del juego
        if self.juego.getGanador() != TresEnRaya.VACIO:
            from game.scenes.escena_game_over import GameOverScene
            self.game_state.cambiar_escena(GameOverScene(self.game_state, self.juego.getGanador()))
            self.game_state.reproducir_sonido('victoria')
            return
        if self.juego.hayEmpate():
            from game.scenes.escena_game_over import GameOverScene
            self.game_state.cambiar_escena(GameOverScene(self.game_state, 0))
            self.game_state.reproducir_sonido('empate')
            return

        # Actualizar animación del cursor
        self.cursor.update_animacion()
        
        # Actualizar animación de turno
        turno_actual = self.juego.getTurno()
        
        # Activar animación en la ficha que tiene el turno
        self.xTurno.set_turno(turno_actual == TresEnRaya.FICHA_X)
        self.oTurno.set_turno(turno_actual == TresEnRaya.FICHA_O)
        
        # Actualizar animaciones de las fichas de turno
        self.xTurno.update_animacion()
        self.oTurno.update_animacion()

    def render(self, pantalla):
        self.tablero.render(pantalla)
        
        # Dibujar cursor
        x = self.tablero.x + self.cursor.getColumna() * 3 * self.e
        y = self.tablero.y + self.cursor.getFila() * 3 * self.e
        self.cursor.render(pantalla, x, y, self.e, self.game_state.cursor_color)

        matriz = self.juego.getMatriz()
        for fila in range(self.n):
            for columna in range(self.n):
                x = self.tablero.x + columna * 3 * self.e
                y = self.tablero.y + fila * 3 * self.e
                if matriz[fila][columna] == TresEnRaya.FICHA_X:
                    ficha = X(x, y, self.e)
                    ficha.setColor(self.game_state.color_x)
                    ficha.render(pantalla)
                elif matriz[fila][columna] == TresEnRaya.FICHA_O:
                    ficha = O(x, y, self.e)
                    ficha.setColor(self.game_state.color_o)
                    ficha.render(pantalla)

        self.xTurno.render(pantalla)
        self.oTurno.render(pantalla)

    def reiniciar(self):
        self.juego.reiniciar()
        self.cursor = Cursor(self.n//2, self.n//2, self.n)