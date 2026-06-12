import pygame
import math
from core.entidad_base import Base

class X(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)
        self.animacion_escala = 1.0
        self.animacion_direccion = 0.008  # Más lento
        self.parpadeo = 0
        self.parpadeo_direccion = 2  # Más suave
        self.es_turno = False

    def set_turno(self, es_turno):
        """Activar/desactivar animación de turno"""
        self.es_turno = es_turno

    def update_animacion(self):
        """Actualizar animación si es el turno actual"""
        if self.es_turno:
            # Animación de pulsación suave
            self.animacion_escala += self.animacion_direccion
            if self.animacion_escala >= 1.08:
                self.animacion_escala = 1.08
                self.animacion_direccion = -0.008
            elif self.animacion_escala <= 0.92:
                self.animacion_escala = 0.92
                self.animacion_direccion = 0.008
            
            # Animación de parpadeo suave
            self.parpadeo += self.parpadeo_direccion
            if self.parpadeo >= 60:
                self.parpadeo = 60
                self.parpadeo_direccion = -2
            elif self.parpadeo <= 0:
                self.parpadeo = 0
                self.parpadeo_direccion = 2
        else:
            # Volver al estado normal gradualmente
            self.animacion_escala = self.animacion_escala * 0.95 + 1.0 * 0.05
            self.parpadeo = self.parpadeo * 0.95

    def render(self, pantalla):
        e = self.e
        escala_actual = e * self.animacion_escala if self.es_turno else e
        
        # Crear superficie
        tamaño = int(3 * escala_actual)
        lienzo = pygame.Surface((tamaño, tamaño), pygame.SRCALPHA)
        
        # Grosor de línea más grueso
        grosor = max(3, e // 5)
        
        # Coordenadas relativas dentro de la superficie
        offset = (tamaño - 3 * e) // 2 if self.es_turno else 0
        x1, y1 = offset, offset
        x2, y2 = 3 * e - offset, 3 * e - offset
        
        # Dibujar X
        pygame.draw.line(lienzo, self.color, (x1, y1), (x2, y2), grosor)
        pygame.draw.line(lienzo, self.color, (x2, y1), (x1, y2), grosor)
        
        # Aplicar transparencia suave (menos agresiva)
        if self.parpadeo > 0 and self.es_turno:
            alpha = max(180, 255 - self.parpadeo // 2)
            lienzo.set_alpha(alpha)

        # Aplicar rotación
        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(center=(self.x + 1.5 * e, self.y + 1.5 * e))
        pantalla.blit(Rotacion, Traslacion)


class O(Base):
    def __init__(self, x, y, e):
        super().__init__(x, y, e)
        self.animacion_escala = 1.0
        self.animacion_direccion = 0.008  # Más lento
        self.parpadeo = 0
        self.parpadeo_direccion = 2  # Más suave
        self.es_turno = False

    def set_turno(self, es_turno):
        """Activar/desactivar animación de turno"""
        self.es_turno = es_turno

    def update_animacion(self):
        """Actualizar animación si es el turno actual"""
        if self.es_turno:
            # Animación de pulsación suave
            self.animacion_escala += self.animacion_direccion
            if self.animacion_escala >= 1.08:
                self.animacion_escala = 1.08
                self.animacion_direccion = -0.008
            elif self.animacion_escala <= 0.92:
                self.animacion_escala = 0.92
                self.animacion_direccion = 0.008
            
            # Animación de parpadeo suave
            self.parpadeo += self.parpadeo_direccion
            if self.parpadeo >= 60:
                self.parpadeo = 60
                self.parpadeo_direccion = -2
            elif self.parpadeo <= 0:
                self.parpadeo = 0
                self.parpadeo_direccion = 2
        else:
            # Volver al estado normal gradualmente
            self.animacion_escala = self.animacion_escala * 0.95 + 1.0 * 0.05
            self.parpadeo = self.parpadeo * 0.95

    def render(self, pantalla):
        e = self.e
        escala_actual = e * self.animacion_escala if self.es_turno else e
        
        # Crear superficie
        tamaño = int(3 * escala_actual)
        lienzo = pygame.Surface((tamaño, tamaño), pygame.SRCALPHA)
        
        # Grosor del círculo
        grosor = max(3, e // 5)
        
        # Calcular centro y radio
        offset = (tamaño - 3 * e) // 2 if self.es_turno else 0
        centro = (tamaño // 2, tamaño // 2)
        radio = int(1.5 * e - offset // 2)
        
        # Dibujar círculo
        pygame.draw.circle(lienzo, self.color, centro, radio, grosor)
        
        # Aplicar transparencia suave
        if self.parpadeo > 0 and self.es_turno:
            alpha = max(180, 255 - self.parpadeo // 2)
            lienzo.set_alpha(alpha)
        
        # Aplicar rotación
        Rotacion = pygame.transform.rotate(lienzo, self.alfa)
        Traslacion = Rotacion.get_rect(center=(self.x + 1.5 * e, self.y + 1.5 * e))
        pantalla.blit(Rotacion, Traslacion)