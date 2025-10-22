"""
Entidad Lechuga - hortaliza tipo Lechuga.
"""
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)


class Lechuga(Hortaliza):
    """
    Cultivo de tipo Lechuga.
    Es una hortaliza de invernadero con variedad configurable.
    """
    
    def __init__(self, variedad: str):
        """
        Inicializa una Lechuga.
        
        Args:
            variedad: Variedad de la lechuga
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        """
        Obtiene la variedad de la lechuga.
        
        Returns:
            Variedad de la lechuga
        """
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad de la lechuga.
        
        Args:
            variedad: Variedad de la lechuga
        """
        self._variedad = variedad