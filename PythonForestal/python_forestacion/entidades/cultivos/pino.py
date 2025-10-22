"""
Entidad Pino - arbol tipo Pino.
"""
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO
)


class Pino(Arbol):
    """
    Cultivo de tipo Pino.
    Es un arbol con variedad configurable.
    """
    
    def __init__(self, variedad: str):
        """
        Inicializa un Pino.
        
        Args:
            variedad: Variedad del pino (Parana, Elliott, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=2.0
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        """
        Obtiene la variedad del pino.
        
        Returns:
            Variedad del pino
        """
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad del pino.
        
        Args:
            variedad: Variedad del pino
        """
        self._variedad = variedad