"""
Entidad Zanahoria - hortaliza tipo Zanahoria.
"""
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Hortaliza):
    """
    Cultivo de tipo Zanahoria.
    Es una hortaliza con opcion de baby carrot.
    """
    
    def __init__(self, es_baby: bool):
        """
        Inicializa una Zanahoria.
        
        Args:
            es_baby: Si es baby carrot
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby = es_baby
    
    def get_es_baby(self) -> bool:
        """
        Indica si es baby carrot.
        
        Returns:
            True si es baby carrot
        """
        return self._es_baby
    
    def set_es_baby(self, es_baby: bool) -> None:
        """
        Establece si es baby carrot.
        
        Args:
            es_baby: True si es baby carrot
        """
        self._es_baby = es_baby