"""
Entidad Tierra - terreno catastral.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """
    Representa un terreno catastral.
    """
    
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        """
        Inicializa una Tierra.
        
        Args:
            id_padron_catastral: Identificador unico del padron
            superficie: Superficie total en m2
            domicilio: Ubicacion del terreno
        """
        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = None
    
    def get_id_padron_catastral(self) -> int:
        """
        Obtiene el padron catastral.
        
        Returns:
            ID del padron catastral
        """
        return self._id_padron_catastral
    
    def set_id_padron_catastral(self, id_padron: int) -> None:
        """
        Establece el padron catastral.
        
        Args:
            id_padron: ID del padron catastral
        """
        self._id_padron_catastral = id_padron
    
    def get_superficie(self) -> float:
        """
        Obtiene la superficie.
        
        Returns:
            Superficie en m2
        """
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie.
        
        Args:
            superficie: Superficie en m2
        """
        self._superficie = superficie
    
    def get_domicilio(self) -> str:
        """
        Obtiene el domicilio.
        
        Returns:
            Domicilio del terreno
        """
        return self._domicilio
    
    def set_domicilio(self, domicilio: str) -> None:
        """
        Establece el domicilio.
        
        Args:
            domicilio: Domicilio del terreno
        """
        self._domicilio = domicilio
    
    def get_finca(self) -> 'Plantacion':
        """
        Obtiene la plantacion asociada.
        
        Returns:
            Plantacion del terreno
        """
        return self._finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        """
        Establece la plantacion asociada.
        
        Args:
            finca: Plantacion a asociar
        """
        self._finca = finca