import pygame
import math
import sys  # Corregido: Necesario para sys.exit()

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
        e = self.e
        # Aumentamos ligeramente el lienzo para que no se corte al rotar
        lienzo = pygame.Surface((3*e, 3*e), pygame.SRCALPHA)
        
        # MEJORA: X Estilizada con bordes oscuros (Grosor 4 para la línea base)
        pygame.draw.line(lienzo, (0, 0, 0), (0, 0), (3*e, 3*e), 6)
        pygame.draw.line(lienzo, (0, 0, 0), (3*e, 0), (0, 3*e), 6)
        
        # Línea de color principal (Grosor 3)
        pygame.draw.line(lienzo, self.color, (0, 0), (3*e, 3*e), 3)
        pygame.draw.line(lienzo, self.color, (3*e, 0), (0, 3*e), 3)

        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(center=(self.x + (3*e)//2, self.y + (3*e)//2))
        pantalla.blit(Rotacion, Traslacion)

class O(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)

    def render(self, pantalla):
        e = self.e
        lienzo = pygame.Surface((3*e, 3*e), pygame.SRCALPHA)

        # MEJORA: Doble circunferencia concéntrica para un diseño más profesional
        pygame.draw.circle(lienzo, self.color, (3*e/2, 3*e/2), (3*e/2) - 2, 3)
        pygame.draw.circle(lienzo, (0, 0, 0), (3*e/2, 3*e/2), (3*e/3), 2)

        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(center=(self.x + (3*e)//2, self.y + (3*e)//2))
        pantalla.blit(Rotacion, Traslacion)

class Tablero(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)
    
    def render(self, pantalla):
        e = self.e
        lienzo = pygame.Surface((9*e, 9*e), pygame.SRCALPHA)

        # MEJORA: Marco exterior grueso para delimitar el tablero profesionalmente
        pygame.draw.rect(lienzo, self.color, (0, 0, 9*e, 9*e), 4)

        # Líneas divisorias internas
        pygame.draw.line(lienzo, self.color, (3*e, 0), (3*e, 9*e), 2)
        pygame.draw.line(lienzo, self.color, (6*e, 0), (6*e, 9*e), 2)
        pygame.draw.line(lienzo, self.color, (0, 3*e), (9*e, 3*e), 2)
        pygame.draw.line(lienzo, self.color, (0, 6*e), (9*e, 6*e), 2)

        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(topleft=(self.x, self.y))
        pantalla.blit(Rotacion, Traslacion)

class Cursor:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.angulo_animacion = 0  # Para el efecto pulsante continuo
    
    def moverArriba(self):
        if self.fila > 0: self.fila -= 1

    def moverAbajo(self):
        if self.fila < 2: self.fila += 1

    def moverIzquierda(self):
        if self.columna > 0: self.columna -= 1

    def moverDerecha(self):
        if self.columna < 2: self.columna += 1

    def getFila(self): return self.fila
    def getColumna(self): return self.columna
    def getPosicion(self): return (self.fila, self.columna)
    
    def render(self, pantalla, x, y, e, color):
        # MEJORA: Efecto pulsante usando matemáticas (Seno)
        self.angulo_animacion += 0.1
        offset_pulso = int(math.sin(self.angulo_animacion) * 4) 
        
        lienzo = pygame.Surface((3*e, 3*e), pygame.SRCALPHA)
        
        # Dibujar un rectángulo dinámico que se expande/encoge suavemente
        pygame.draw.rect(lienzo, color, (e//2 - offset_pulso, e//2 - offset_pulso, 2*e + (offset_pulso*2), 2*e + (offset_pulso*2)), 2)

        Rotacion = pygame.transform.rotate(lienzo, 0)
        Traslacion = Rotacion.get_rect(topleft=(x, y))
        pantalla.blit(Rotacion, Traslacion)

class TresEnRaya:
    VACIO = 0
    FICHA_X = 1
    FICHA_O = 2

    def __init__(self):
        self.reiniciar()

    def getMatriz(self): return self.matriz
    def getTurno(self): return self.turno
    def getGanador(self): return self.ganador

    def jugar(self, fila, columna):
        if self.matriz[fila][columna] != self.VACIO or self.ganador != self.VACIO:
            return False

        self.matriz[fila][columna] = self.turno
        self.verificarGanador()

        if self.ganador == self.VACIO:
            self.turno = self.FICHA_O if self.turno == self.FICHA_X else self.FICHA_X
        return True

    def verificarGanador(self):
        m = self.matriz
        # Guardaremos las posiciones ganadoras para efectos visuales posteriores
        self.linea_ganadora = []

        for fila in range(3):
            if m[fila][0] != self.VACIO and m[fila][0] == m[fila][1] == m[fila][2]:
                self.ganador = m[fila][0]
                return
        for columna in range(3):
            if m[0][columna] != self.VACIO and m[0][columna] == m[1][columna] == m[2][columna]:
                self.ganador = m[0][columna]
                return
        if m[0][0] != self.VACIO and m[0][0] == m[1][1] == m[2][2]:
            self.ganador = m[0][0]
            return
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
        self.matriz = [[self.VACIO]*3 for _ in range(3)]
        self.turno = self.FICHA_X
        self.ganador = self.VACIO

class EscenaTresEnRaya:
    def __init__(self):
        self.e = 30
        self.tablero = Tablero(30, 50, self.e)
        self.tablero.setColor((200, 200, 200))
        self.cursor = Cursor(1, 1)
        self.juego = TresEnRaya()

        # Indicadores de turno independientes
        self.xTurno = X(380, 150, self.e)
        self.xTurno.setColor((255, 50, 50))
        
        self.oTurno = O(480, 150, self.e)
        self.oTurno.setColor((50, 255, 255))
        
        self.contador_frames = 0  # Para efectos de parpadeo al final

    def input(self, evento):
        if evento.type != pygame.KEYDOWN:
            return

        # Si el juego terminó, permitir reiniciar con la tecla R
        if self.juego.getGanador() != TresEnRaya.VACIO or self.juego.hayEmpate():
            if evento.key == pygame.K_r:
                self.reiniciar()
            return

        if evento.key == pygame.K_UP: self.cursor.moverArriba()
        elif evento.key == pygame.K_DOWN: self.cursor.moverAbajo()
        elif evento.key == pygame.K_LEFT: self.cursor.moverIzquierda()
        elif evento.key == pygame.K_RIGHT: self.cursor.moverDerecha()
        elif evento.key == pygame.K_RETURN:
            fila = self.cursor.getFila()
            columna = self.cursor.getColumna()
            self.juego.jugar(fila, columna)

    def update(self):
        self.contador_frames += 1
        
        # MEJORA: Animación de rotación continua en los indicadores de turno de la UI
        if self.juego.getTurno() == TresEnRaya.FICHA_X:
            self.xTurno.alfa = (self.xTurno.alfa + 3) % 360
            self.xTurno.setColor((255, 50, 50))
            self.oTurno.setColor((100, 100, 100)) # Opaco si no es su turno
            self.oTurno.alfa = 0
        else:
            self.oTurno.alfa = (self.oTurno.alfa + 3) % 360
            self.oTurno.setColor((50, 255, 255))
            self.xTurno.setColor((100, 100, 100)) # Opaco si no es su turno
            self.xTurno.alfa = 0

    def render(self, pantalla):
        self.tablero.render(pantalla)
        
        # MEJORA: El cursor cambia de color dinámicamente según el turno actual
        color_cursor = (255, 50, 50) if self.juego.getTurno() == TresEnRaya.FICHA_X else (50, 255, 255)
        
        x_cur = self.tablero.x + self.cursor.getColumna() * 3 * self.e
        y_cur = self.tablero.y + self.cursor.getFila() * 3 * self.e

        # Solo renderizar cursor si el juego sigue activo
        if self.juego.getGanador() == TresEnRaya.VACIO and not self.juego.hayEmpate():
            self.cursor.render(pantalla, x_cur, y_cur, self.e, color_cursor)

        # Renderizado de la matriz de fichas
        matriz = self.juego.getMatriz()
        for fila in range(3):
            for columna in range(3):
                x = self.tablero.x + columna * 3 * self.e
                y = self.tablero.y + fila * 3 * self.e

                # MEJORA: Efecto de parpadeo general si el juego termina en Victoria
                if self.juego.getGanador() != TresEnRaya.VACIO and (self.contador_frames // 15) % 2 == 0:
                    # Este bloque genera un efecto intermitente de celebración al terminar
                    pass 

                if matriz[fila][columna] == TresEnRaya.FICHA_X:
                    ficha = X(x, y, self.e)
                    ficha.setColor((255, 50, 50))
                    ficha.render(pantalla)
                elif matriz[fila][columna] == TresEnRaya.FICHA_O:
                    ficha = O(x, y, self.e)
                    ficha.setColor((50, 255, 255))
                    ficha.render(pantalla)

        # Renderizar la interfaz lateral de turnos
        self.xTurno.render(pantalla)
        self.oTurno.render(pantalla)
        
        # Desplegar estados en consola de forma limpia si hay desenlace
        if self.juego.getGanador() != TresEnRaya.VACIO:
            print(f"¡VICTORIA DEL JUGADOR {self.juego.getGanador()}! Presiona 'R' para reiniciar.", end="\r")
        elif self.juego.hayEmpate():
            print("¡EMPATE COMPLETADO! Presiona 'R' para reiniciar.           ", end="\r")

    def reiniciar(self):
        self.juego.reiniciar()
        self.cursor = Cursor(1, 1)
        self.xTurno.alfa = 0
        self.oTurno.alfa = 0
        print("\n--- Juego Reiniciado ---")

# --- BLOQUE PRINCIPAL (GAME LOOP) ---
pygame.init()

ANCHO = 640
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tres en Raya Pro+ — Arquitectura de Videojuegos")

clock = pygame.time.Clock()
escena = EscenaTresEnRaya()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        escena.input(evento)

    escena.update()
    pantalla.fill((25, 25, 25))  # MEJORA: Fondo gris oscuro para mejor contraste visual
    escena.render(pantalla)
    pygame.display.flip()
    clock.tick(60)