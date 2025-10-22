"""
Entidad base Cultivo - interfaz para todos los cultivos del sistema.
"""
from abc import ABC
from datetime import date


class Cultivo(ABC):
    """
    Clase abstracta base para todos los cultivos.
    Define la interfaz comun que deben implementar todos los tipos de cultivos.
    """
    
    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo con sus propiedades basicas.
        
        Args:
            agua: Agua inicial en litros
            superficie: Superficie que ocupa en m2
        """
        self._agua = agua
        self._superficie = superficie
        self._fecha_plantacion = date.today()
    
    def get_agua(self) -> int:
        """
        Obtiene el agua del cultivo.
        
        Returns:
            Agua en litros
        """
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        """
        Establece el agua del cultivo.
        
        Args:
            agua: Agua en litros
        """
        self._agua = agua
    
    def get_superficie(self) -> float:
        """
        Obtiene la superficie del cultivo.
        
        Returns:
            Superficie en m2
        """
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie del cultivo.
        
        Args:
            superficie: Superficie en m2
        """
        self._superficie = superficie
    
    def get_fecha_plantacion(self) -> date:
        """
        Obtiene la fecha de plantacion.
        
        Returns:
            Fecha de plantacion
        """
        return self._fecha_plantacion
    
    def set_fecha_plantacion(self, fecha: date) -> None:
        """
        Establece la fecha de plantacion.
        
        Args:
            fecha: Fecha de plantacion
        """
        self._fecha_plantacion = fecha