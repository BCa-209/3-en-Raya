import pygame
from core.escena import Escena
from game.entities import Tablero, Cursor, X, O
from game.logic import TresEnRaya
from config import *

class EscenaJuego(Escena):
    def __init__(self, game_state):
        self.game_state = game_state
        self.n = game_state.tam_tablero
        
        # Calcular escala automática para que quepa en pantalla
        margen_superior = 100   # espacio para el título/indicadores
        margen_inferior = 50
        margen_lateral = 40
        ancho_disponible = game_state.ancho_pantalla - 2 * margen_lateral
        alto_disponible = game_state.alto_pantalla - margen_superior - margen_inferior
        
        # La celda ocupa 3*e de ancho/alto, y hay n celdas por lado
        e_por_ancho = ancho_disponible / (3 * self.n)
        e_por_alto = alto_disponible / (3 * self.n)
        self.e = min(e_por_ancho, e_por_alto)  # usar la que quepa
        
        # Posición del tablero centrada
        ancho_tablero = self.n * 3 * self.e
        alto_tablero = self.n * 3 * self.e
        self.x_tablero = (game_state.ancho_pantalla - ancho_tablero) // 2
        self.y_tablero = margen_superior

        self.tablero = Tablero(self.x_tablero, self.y_tablero, self.e, self.n)
        self.tablero.setColor((255,255,255))

        self.cursor = Cursor(self.n//2, self.n//2, self.n)
        self.juego = TresEnRaya(self.n, infinito=game_state.modo_infinito)

        # Indicadores de turno (escala relativa a la celda, pero con límite)
        tam_turno = max(15, min(30, self.e // 2))
        self.xTurno = X(50, 30, tam_turno)
        self.xTurno.setColor((255,0,0))
        self.oTurno = O(game_state.ancho_pantalla - 50 - tam_turno*3, 30, tam_turno)
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
                pass

    def update(self):
        if self.juego.getGanador() != TresEnRaya.VACIO:
            from game.scenes.escena_game_over import GameOverScene
            self.game_state.cambiar_escena(GameOverScene(self.game_state, self.juego.getGanador()))
            return
        if self.juego.hayEmpate():
            from game.scenes.escena_game_over import GameOverScene
            self.game_state.cambiar_escena(GameOverScene(self.game_state, 0))
            return

        # Animación del indicador de turno
        if self.juego.getTurno() == TresEnRaya.FICHA_X:
            if self.xTurno.e >= 0.5*self.e or self.xTurno.e <= self.e//4:
                self.incXTurno = -self.incXTurno
            self.xTurno.e += self.incXTurno
            # Evitar que crezca demasiado
            if self.xTurno.e > self.e:
                self.xTurno.e = self.e
        else:
            if self.oTurno.e >= 0.5*self.e or self.oTurno.e <= self.e//4:
                self.incYTurno = -self.incYTurno
            self.oTurno.e += self.incYTurno
            if self.oTurno.e > self.e:
                self.oTurno.e = self.e

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
        self.cursor = Cursor(self.n//2, self.n//2, self.n)
        self.xTurno.alfa = 0
        self.oTurno.alfa = 0