from collections import deque

class TresEnRaya:
    VACIO = 0
    FICHA_X = 1
    FICHA_O = 2

    def __init__(self, n=3, infinito=False):
        self.n = n
        self.infinito = infinito
        self.matriz = [[self.VACIO] * n for _ in range(n)]
        self.movimientos = deque() if infinito else None  # cola FIFO sin límite fijo
        self.turno = self.FICHA_X
        self.ganador = self.VACIO
        self.ultima_ficha = None

        # Estadísticas (se mantienen entre partidas)
        self.partidas_jugadas = 0
        self.victorias_x = 0
        self.victorias_o = 0
        self.empates = 0

    def getMatriz(self):
        return self.matriz

    def getTurno(self):
        return self.turno

    def getGanador(self):
        return self.ganador

    def jugar(self, fila, columna):
        if self.ganador != self.VACIO:
            return False
        if self.matriz[fila][columna] != self.VACIO:
            return False

        # ---- MODO INFINITO: mantener solo los últimos 7 movimientos ----
        if self.infinito:
            if len(self.movimientos) == 7:
                f_vieja, c_vieja, _ = self.movimientos.popleft()
                self.matriz[f_vieja][c_vieja] = self.VACIO
            # Agregar el nuevo movimiento a la cola
            self.movimientos.append((fila, columna, self.turno))

        # Colocar la ficha en el tablero
        self.matriz[fila][columna] = self.turno
        self.ultima_ficha = (fila, columna)

        self.verificarGanador()

        if self.ganador == self.VACIO:
            self.turno = self.FICHA_O if self.turno == self.FICHA_X else self.FICHA_X

        return True

    def verificarGanador(self):
        n = self.n
        m = self.matriz
        
        # Verificar filas
        for i in range(n):
            for j in range(n - 2):  # solo hasta donde cabe un grupo de 3
                if m[i][j] != self.VACIO and m[i][j] == m[i][j+1] == m[i][j+2]:
                    self.ganador = m[i][j]
                    return
        
        # Verificar columnas
        for j in range(n):
            for i in range(n - 2):
                if m[i][j] != self.VACIO and m[i][j] == m[i+1][j] == m[i+2][j]:
                    self.ganador = m[i][j]
                    return
        
        # Verificar diagonal principal (\)
        for i in range(n - 2):
            for j in range(n - 2):
                if m[i][j] != self.VACIO and m[i][j] == m[i+1][j+1] == m[i+2][j+2]:
                    self.ganador = m[i][j]
                    return
        
        # Verificar diagonal secundaria (/)
        for i in range(n - 2):
            for j in range(2, n):
                if m[i][j] != self.VACIO and m[i][j] == m[i+1][j-1] == m[i+2][j-2]:
                    self.ganador = m[i][j]
                    return

    def hayEmpate(self):
        if self.infinito:
            return False
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
        if self.infinito:
            self.movimientos.clear()   # vaciar la cola

    def registrar_resultado(self):
        """Actualiza estadísticas al finalizar la partida"""
        self.partidas_jugadas += 1
        if self.ganador == self.FICHA_X:
            self.victorias_x += 1
        elif self.ganador == self.FICHA_O:
            self.victorias_o += 1
        else:
            self.empates += 1

    def reiniciar(self):
        self.matriz = [[self.VACIO] * self.n for _ in range(self.n)]
        self.turno = self.FICHA_X
        self.ganador = self.VACIO
        self.ultima_ficha = None
        if self.infinito:
            self.movimientos.clear()

    def reiniciar_juego_completo(self, nuevo_n=None, nuevo_infinito=None):
        """Reinicia el juego pero mantiene las estadísticas"""
        if nuevo_n is not None:
            self.n = nuevo_n
        if nuevo_infinito is not None:
            self.infinito = nuevo_infinito
        self.matriz = [[self.VACIO] * self.n for _ in range(self.n)]
        self.movimientos = deque() if self.infinito else None
        self.turno = self.FICHA_X
        self.ganador = self.VACIO
        self.ultima_ficha = None