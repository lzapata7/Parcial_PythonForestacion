"""
Entidad Plantacion - plantacion agricola.
"""
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """
    Representa una plantacion con cultivos y trabajadores.
    """
    
    def __init__(self, nombre: str, superficie_disponible: float, agua_disponible: int):
        """
        Inicializa una Plantacion.
        
        Args:
            nombre: Nombre de la plantacion
            superficie_disponible: Superficie disponible en m2
            agua_disponible: Agua disponible en litros
        """
        self._nombre = nombre
        self._superficie_disponible = superficie_disponible
        self._agua_disponible = agua_disponible
        self._cultivos = []
        self._trabajadores = []
    
    def get_nombre(self) -> str:
        """
        Obtiene el nombre.
        
        Returns:
            Nombre de la plantacion
        """
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre.
        
        Args:
            nombre: Nombre de la plantacion
        """
        self._nombre = nombre
    
    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie disponible.
        
        Returns:
            Superficie disponible en m2
        """
        return self._superficie_disponible
    
    def set_superficie_disponible(self, superficie: float) -> None:
        """
        Establece la superficie disponible.
        
        Args:
            superficie: Superficie disponible en m2
        """
        self._superficie_disponible = superficie
    
    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.
        
        Returns:
            Agua disponible en litros
        """
        return self._agua_disponible
    
    def set_agua_disponible(self, agua: int) -> None:
        """
        Establece el agua disponible.
        
        Args:
            agua: Agua disponible en litros
        """
        self._agua_disponible = agua
    
    def get_cultivos(self) -> List['Cultivo']:
        """
        Obtiene la lista de cultivos.
        
        Returns:
            Lista de cultivos
        """
        return self._cultivos.copy()
    
    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """
        Agrega un cultivo a la plantacion.
        
        Args:
            cultivo: Cultivo a agregar
        """
        self._cultivos.append(cultivo)
    
    def get_trabajadores(self) -> List['Trabajador']:
        """
        Obtiene la lista de trabajadores.
        
        Returns:
            Lista de trabajadores
        """
        return self._trabajadores.copy()
    
    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        """
        Agrega un trabajador a la plantacion.
        
        Args:
            trabajador: Trabajador a agregar
        """
        self._trabajadores.append(trabajador)