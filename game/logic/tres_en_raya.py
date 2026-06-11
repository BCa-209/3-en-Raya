class TresEnRaya:
    VACIO = 0
    FICHA_X = 1
    FICHA_O = 2

    def __init__(self, n=3):
        self.n = n  # tamaño del tablero (n x n)
        self.matriz = [[self.VACIO] * n for _ in range(n)]
        self.turno = self.FICHA_X
        self.ganador = self.VACIO
        self.ultima_ficha = None  # (fila, columna) para animaciones

    def getMatriz(self):
        return self.matriz

    def getTurno(self):
        return self.turno

    def getGanador(self):
        return self.ganador

    def jugar(self, fila, columna):
        if self.matriz[fila][columna] != self.VACIO:
            return False
        if self.ganador != self.VACIO:
            return False

        self.matriz[fila][columna] = self.turno
        self.ultima_ficha = (fila, columna)
        self.verificarGanador()

        if self.ganador == self.VACIO:
            self.turno = self.FICHA_O if self.turno == self.FICHA_X else self.FICHA_X
        return True

    def verificarGanador(self):
        n = self.n
        m = self.matriz

        # Filas
        for i in range(n):
            if all(m[i][j] == m[i][0] != self.VACIO for j in range(n)):
                self.ganador = m[i][0]
            return

        # Columnas
        for j in range(n):
            if all(m[i][j] == m[0][j] != self.VACIO for i in range(n)):
                self.ganador = m[0][j]
                return

        # Diagonal principal
        if all(m[i][i] == m[0][0] != self.VACIO for i in range(n)):
            self.ganador = m[0][0]
            return

        # Diagonal secundaria
        if all(m[i][n-1-i] == m[0][n-1] != self.VACIO for i in range(n)):
            self.ganador = m[0][n-1]
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
        self.matriz = [[self.VACIO] * self.n for _ in range(self.n)]
        self.turno = self.FICHA_X
        self.ganador = self.VACIO
        self.ultima_ficha = None