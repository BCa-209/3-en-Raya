import pygame
from core.escena import Escena
from config import ANCHO, ALTO, COLOR_BLANCO, COLOR_NEGRO, COLOR_GRIS, COLOR_GRIS_CLARO, COLOR_AMARILLO, COLOR_ROJO, COLORES_FICHAS, COLORES_CURSOR, TECLA_ABAJO, TECLA_ACEPTAR, TECLA_ARRIBA, TECLA_CANCELAR, TECLA_DERECHA, TECLA_IZQUIERDA, COLOR_VERDE

class ConfiguracionScene(Escena):
    def __init__(self, game_state):
        self.game_state = game_state
        
        # Opciones de configuración
        self.opciones = [
            "Color de X",
            "Color de O", 
            "Color del cursor",
            "Guardar cambios",
            "Salir sin guardar"
        ]
        self.seleccion = 0
        self.sub_menu = False
        self.sub_seleccion = 0
        
        # Guardar copia de los colores originales para poder cancelar
        self.backup_colores = {
            'color_x_idx': game_state.color_x_idx,
            'color_o_idx': game_state.color_o_idx,
            'cursor_color_idx': game_state.cursor_color_idx,
            'color_x': game_state.color_x,
            'color_o': game_state.color_o,
            'cursor_color': game_state.cursor_color
        }
        
        # Fuentes
        self.font_titulo = pygame.font.Font(None, 48)
        self.font_opcion = pygame.font.Font(None, 36)
        self.font_valor = pygame.font.Font(None, 28)
        
    def input(self, evento):
        if evento.type != pygame.KEYDOWN:
            return
            
        if evento.key == TECLA_CANCELAR:
            if self.sub_menu:
                self.sub_menu = False
                self.sub_seleccion = 0
            else:
                # Preguntar si quiere salir sin guardar
                self.salir_sin_guardar()
            return
            
        if self.sub_menu:
            self.input_sub_menu(evento)
        else:
            self.input_principal(evento)
    
    def input_principal(self, evento):
        if evento.key == TECLA_ARRIBA:
            self.seleccion = (self.seleccion - 1) % len(self.opciones)
        elif evento.key == TECLA_ABAJO:
            self.seleccion = (self.seleccion + 1) % len(self.opciones)
        elif evento.key == TECLA_IZQUIERDA:
            self.modificar_valor(-1)
        elif evento.key == TECLA_DERECHA:
            self.modificar_valor(1)
        elif evento.key == TECLA_ACEPTAR:
            if self.seleccion == 3:  # Guardar cambios
                self.guardar_cambios()
            elif self.seleccion == 4:  # Salir sin guardar
                self.salir_sin_guardar()
            else:
                self.abrir_sub_menu()
    
    def input_sub_menu(self, evento):
        if evento.key == TECLA_ARRIBA:
            self.sub_seleccion = (self.sub_seleccion - 1) % self.get_sub_menu_len()
        elif evento.key == TECLA_ABAJO:
            self.sub_seleccion = (self.sub_seleccion + 1) % self.get_sub_menu_len()
        elif evento.key == TECLA_ACEPTAR:
            self.guardar_sub_menu()
            self.sub_menu = False
            self.sub_seleccion = 0
    
    def get_sub_menu_len(self):
        if self.seleccion == 0:  # Color X
            return len(COLORES_FICHAS)
        elif self.seleccion == 1:  # Color O
            return len(COLORES_FICHAS)
        elif self.seleccion == 2:  # Color cursor
            return len(COLORES_CURSOR)
        return 0
    
    def modificar_valor(self, delta):
        if self.seleccion == 0:  # Color X
            colores = COLORES_FICHAS
            idx = self.game_state.color_x_idx
            self.game_state.color_x_idx = (idx + delta) % len(colores)
            self.game_state.color_x = colores[self.game_state.color_x_idx][1]
        elif self.seleccion == 1:  # Color O
            colores = COLORES_FICHAS
            idx = self.game_state.color_o_idx
            self.game_state.color_o_idx = (idx + delta) % len(colores)
            self.game_state.color_o = colores[self.game_state.color_o_idx][1]
        elif self.seleccion == 2:  # Color cursor
            colores = COLORES_CURSOR
            idx = self.game_state.cursor_color_idx
            self.game_state.cursor_color_idx = (idx + delta) % len(colores)
            self.game_state.cursor_color = colores[self.game_state.cursor_color_idx][1]
    
    def abrir_sub_menu(self):
        self.sub_menu = True
        self.sub_seleccion = self.get_sub_menu_valor_actual()
    
    def get_sub_menu_valor_actual(self):
        if self.seleccion == 0:
            return self.game_state.color_x_idx
        elif self.seleccion == 1:
            return self.game_state.color_o_idx
        elif self.seleccion == 2:
            return self.game_state.cursor_color_idx
        return 0
    
    def guardar_sub_menu(self):
        if self.seleccion == 0:
            self.game_state.color_x_idx = self.sub_seleccion
            self.game_state.color_x = COLORES_FICHAS[self.sub_seleccion][1]
            # Actualizar backup
            self.backup_colores['color_x_idx'] = self.game_state.color_x_idx
            self.backup_colores['color_x'] = self.game_state.color_x
        elif self.seleccion == 1:
            self.game_state.color_o_idx = self.sub_seleccion
            self.game_state.color_o = COLORES_FICHAS[self.sub_seleccion][1]
            self.backup_colores['color_o_idx'] = self.game_state.color_o_idx
            self.backup_colores['color_o'] = self.game_state.color_o
        elif self.seleccion == 2:
            self.game_state.cursor_color_idx = self.sub_seleccion
            self.game_state.cursor_color = COLORES_CURSOR[self.sub_seleccion][1]
            self.backup_colores['cursor_color_idx'] = self.game_state.cursor_color_idx
            self.backup_colores['cursor_color'] = self.game_state.cursor_color
    
    def get_valor_actual(self):
        if self.seleccion == 0:
            return COLORES_FICHAS[self.game_state.color_x_idx][0]
        elif self.seleccion == 1:
            return COLORES_FICHAS[self.game_state.color_o_idx][0]
        elif self.seleccion == 2:
            return COLORES_CURSOR[self.game_state.cursor_color_idx][0]
        elif self.seleccion == 3 or self.seleccion == 4:
            return ""  # Los botones no muestran valor
        return ""
    
    def guardar_cambios(self):
        """Guarda los cambios y vuelve al menú"""
        from game.scenes.escena_menu import MenuScene
        self.game_state.cambiar_escena(MenuScene(self.game_state))
    
    def salir_sin_guardar(self):
        """Restaura los colores originales y vuelve al menú"""
        # Restaurar colores desde el backup
        self.game_state.color_x_idx = self.backup_colores['color_x_idx']
        self.game_state.color_x = self.backup_colores['color_x']
        self.game_state.color_o_idx = self.backup_colores['color_o_idx']
        self.game_state.color_o = self.backup_colores['color_o']
        self.game_state.cursor_color_idx = self.backup_colores['cursor_color_idx']
        self.game_state.cursor_color = self.backup_colores['cursor_color']
        
        from game.scenes.escena_menu import MenuScene
        self.game_state.cambiar_escena(MenuScene(self.game_state))
    
    def update(self):
        pass
    
    def render(self, pantalla):
        pantalla.fill(COLOR_NEGRO)
        
        if self.sub_menu:
            self.render_sub_menu(pantalla)
        else:
            self.render_principal(pantalla)
    
    def render_principal(self, pantalla):
        # Título
        titulo = self.font_titulo.render("CONFIGURACIÓN", True, COLOR_BLANCO)
        pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 40))
        
        # Opciones
        y_base = 130
        espaciado = 55
        
        for i, opcion in enumerate(self.opciones):
            # Color diferente para los botones
            if i == 3:
                color_texto = COLOR_VERDE if i == self.seleccion else COLOR_GRIS_CLARO
            elif i == 4:
                color_texto = COLOR_ROJO if i == self.seleccion else COLOR_GRIS_CLARO
            else:
                color_texto = COLOR_GRIS_CLARO if i == self.seleccion else COLOR_BLANCO
            
            texto = self.font_opcion.render(opcion, True, color_texto)
            pantalla.blit(texto, (100, y_base + i * espaciado))
            
            # Valor actual (solo para opciones de color)
            if i < 3:
                valor = self.get_valor_actual()
                texto_valor = self.font_valor.render(valor, True, COLOR_GRIS)
                
                # Mostrar color de muestra
                if i == 0:  # Color X
                    muestra_rect = pygame.Rect(ANCHO - 120, y_base + i * espaciado - 10, 30, 30)
                    pygame.draw.rect(pantalla, self.game_state.color_x, muestra_rect)
                    pantalla.blit(texto_valor, (ANCHO - 80, y_base + i * espaciado))
                elif i == 1:  # Color O
                    muestra_rect = pygame.Rect(ANCHO - 120, y_base + i * espaciado - 10, 30, 30)
                    pygame.draw.rect(pantalla, self.game_state.color_o, muestra_rect)
                    pantalla.blit(texto_valor, (ANCHO - 80, y_base + i * espaciado))
                elif i == 2:  # Color cursor
                    muestra_rect = pygame.Rect(ANCHO - 120, y_base + i * espaciado - 10, 30, 30)
                    pygame.draw.rect(pantalla, self.game_state.cursor_color, muestra_rect)
                    pantalla.blit(texto_valor, (ANCHO - 80, y_base + i * espaciado))
        
        # Instrucciones
        ayuda1 = self.font_valor.render("↑ ↓ mover | ← → cambiar valor | ENTER: seleccionar | ESC: salir", True, COLOR_GRIS)
        pantalla.blit(ayuda1, (ANCHO//2 - ayuda1.get_width()//2, ALTO - 50))
    
    def render_sub_menu(self, pantalla):
        # Fondo semitransparente
        overlay = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        pantalla.blit(overlay, (0, 0))
        
        # Título
        titulo = self.font_titulo.render(self.opciones[self.seleccion], True, COLOR_BLANCO)
        pantalla.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 80))
        
        # Opciones del submenú
        y_base = 160
        espaciado = 50
        
        if self.seleccion == 0:  # Colores X
            items = COLORES_FICHAS
        elif self.seleccion == 1:  # Colores O
            items = COLORES_FICHAS
        elif self.seleccion == 2:  # Colores cursor
            items = COLORES_CURSOR
        else:
            items = []
        
        for i, item in enumerate(items):
            color_texto = COLOR_AMARILLO if i == self.sub_seleccion else COLOR_BLANCO
            texto = self.font_opcion.render(item[0], True, color_texto)
            pantalla.blit(texto, (ANCHO//2 - texto.get_width()//2, y_base + i * espaciado))
            
            # Mostrar muestra de color
            if len(item) > 1:
                muestra_rect = pygame.Rect(ANCHO//2 + 150, y_base + i * espaciado - 10, 30, 30)
                pygame.draw.rect(pantalla, item[1], muestra_rect)
        
        # Instrucciones
        ayuda = self.font_valor.render("↑ ↓ mover | ENTER: seleccionar | ESC: cancelar", True, COLOR_GRIS)
        pantalla.blit(ayuda, (ANCHO//2 - ayuda.get_width()//2, ALTO - 50))
    
    def reiniciar(self):
        self.seleccion = 0
        self.sub_menu = False
        self.sub_seleccion = 0