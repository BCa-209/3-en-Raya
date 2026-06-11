from abc import ABC, abstractmethod

class Escena(ABC):
    """Interfase abstracta para todas las escenas del juego"""
    
    @abstractmethod
    def input(self, evento):
        """Procesa eventos de entrada"""
        pass
    
    @abstractmethod
    def update(self):
        """Actualiza la lógica de la escena"""
        pass
    
    @abstractmethod
    def render(self, pantalla):
        """Renderiza la escena en la pantalla"""
        pass
    
    @abstractmethod
    def reiniciar(self):
        """Reinicia el estado de la escena"""
        pass