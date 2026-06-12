import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sonidos = {}
        self.cargar_sonidos()
    
    def cargar_sonidos(self):
        """Cargar sonidos desde archivos MP3/WAV"""
        
        # Ruta base de los sonidos
        base_path = "assets/sounds/"
        
        # Definir los sonidos a cargar
        sonidos_config = {
            'movimiento': 'move.mp3',
            'colocar': 'select.mp3',
            'victoria': 'win.mp3',
            'empate': 'win.mp3',
            'error': 'error.mp3',
            'seleccion': 'select.mp3'
        }
        #    'movimiento': 'move.mp3',
        #    'colocar': 'place.mp3',
        #    'victoria': 'win.mp3',
        #    'empate': 'draw.mp3',
        #    'error': 'error.mp3',
        #    'seleccion': 'select.mp3'
        
        for nombre, archivo in sonidos_config.items():
            ruta_completa = os.path.join(base_path, archivo)
            try:
                if os.path.exists(ruta_completa):
                    self.sonidos[nombre] = pygame.mixer.Sound(ruta_completa)
                    print(f"✅ Sonido cargado: {nombre} -> {ruta_completa}")
                else:
                    print(f"⚠️ Archivo no encontrado: {ruta_completa}")
                    self.sonidos[nombre] = None
            except Exception as e:
                print(f"❌ Error cargando {nombre}: {e}")
                self.sonidos[nombre] = None
    
    def reproducir(self, nombre):
        """Reproducir un sonido por su nombre"""
        if nombre in self.sonidos and self.sonidos[nombre] is not None:
            try:
                self.sonidos[nombre].play()
            except:
                pass
    
    def detener_todos(self):
        """Detener todos los sonidos"""
        for sonido in self.sonidos.values():
            if sonido is not None:
                try:
                    sonido.stop()
                except:
                    pass
    
    def ajustar_volumen(self, nombre, volumen):
        """Ajustar volumen de un sonido (0.0 a 1.0)"""
        if nombre in self.sonidos and self.sonidos[nombre] is not None:
            try:
                self.sonidos[nombre].set_volume(volumen)
            except:
                pass