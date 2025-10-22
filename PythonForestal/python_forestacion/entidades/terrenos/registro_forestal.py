"""
Entidad RegistroForestal - registro completo de tierra y plantacion.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """
    Vincula tierra con plantacion y propietario.
    """
    
    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa un RegistroForestal.
        
        Args:
            id_padron: ID del padron catastral
            tierra: Tierra asociada
            plantacion: Plantacion asociada
            propietario: Nombre del propietario
            avaluo: Avaluo fiscal
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo
    
    def get_id_padron(self) -> int:
        """
        Obtiene el ID del padron.
        
        Returns:
            ID del padron
        """
        return self._id_padron
    
    def set_id_padron(self, id_padron: int) -> None:
        """
        Establece el ID del padron.
        
        Args:
            id_padron: ID del padron
        """
        self._id_padron = id_padron
    
    def get_tierra(self) -> 'Tierra':
        """
        Obtiene la tierra.
        
        Returns:
            Tierra asociada
        """
        return self._tierra
    
    def set_tierra(self, tierra: 'Tierra') -> None:
        """
        Establece la tierra.
        
        Args:
            tierra: Tierra a asociar
        """
        self._tierra = tierra
    
    def get_plantacion(self) -> 'Plantacion':
        """
        Obtiene la plantacion.
        
        Returns:
            Plantacion asociada
        """
        return self._plantacion
    
    def set_plantacion(self, plantacion: 'Plantacion') -> None:
        """
        Establece la plantacion.
        
        Args:
            plantacion: Plantacion a asociar
        """
        self._plantacion = plantacion
    
    def get_propietario(self) -> str:
        """
        Obtiene el propietario.
        
        Returns:
            Nombre del propietario
        """
        return self._propietario
    
    def set_propietario(self, propietario: str) -> None:
        """
        Establece el propietario.
        
        Args:
            propietario: Nombre del propietario
        """
        self._propietario = propietario
    
    def get_avaluo(self) -> float:
        """
        Obtiene el avaluo.
        
        Returns:
            Avaluo fiscal
        """
        return self._avaluo
    
    def set_avaluo(self, avaluo: float) -> None:
        """
        Establece el avaluo.
        
        Args:
            avaluo: Avaluo fiscal
        """
        self._avaluo = avaluo