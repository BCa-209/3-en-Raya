class TresEnRaya:
    """Lógica pura del juego Tres en Raya (sin dependencias de Pygame)"""

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
            self.turno = self.FICHA_O if self.turno == self.FICHA_X else self.FICHA_X

        return True

    def verificarGanador(self):
        m = self.matriz

        # Filas
        for fila in range(3):
            if m[fila][0] != self.VACIO and m[fila][0] == m[fila][1] == m[fila][2]:
                self.ganador = m[fila][0]
                return

        # Columnas
        for columna in range(3):
            if m[0][columna] != self.VACIO and m[0][columna] == m[1][columna] == m[2][columna]:
                self.ganador = m[0][columna]
                return

        # Diagonal principal
        if m[0][0] != self.VACIO and m[0][0] == m[1][1] == m[2][2]:
            self.ganador = m[0][0]
            return

        # Diagonal secundaria
        if m[0][2] != self.VACIO and m[0][2] == m[1][1] == m[2][0]:
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