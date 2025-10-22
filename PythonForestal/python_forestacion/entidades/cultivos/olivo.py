"""
Entidad Olivo - arbol tipo Olivo.
"""
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO
)


class Olivo(Arbol):
    """
    Cultivo de tipo Olivo.
    Es un arbol con tipo de aceituna.
    """
    
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un Olivo.
        
        Args:
            tipo_aceituna: Tipo de aceituna del olivo
        """
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=0.0
        )
        self._tipo_aceituna = tipo_aceituna
    
    def get_tipo_aceituna(self) -> TipoAceituna:
        """
        Obtiene el tipo de aceituna.
        
        Returns:
            Tipo de aceituna
        """
        return self._tipo_aceituna
    
    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """
        Establece el tipo de aceituna.
        
        Args:
            tipo_aceituna: Tipo de aceituna
        """
        self._tipo_aceituna = tipo_aceituna