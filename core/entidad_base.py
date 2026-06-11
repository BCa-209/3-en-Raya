class Base:
    """Clase base para entidades con transformaciones geométricas"""
    
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