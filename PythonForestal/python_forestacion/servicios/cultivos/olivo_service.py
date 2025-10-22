"""
Servicio para cultivos Olivo.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """
    Servicio para operaciones sobre Olivo.
    Usa estrategia seasonal para absorcion.
    """
    
    def __init__(self):
        """
        Inicializa el servicio de Olivo con estrategia seasonal.
        """
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, olivo: 'Olivo') -> None:
        """
        Hace crecer el olivo con incremento especifico.
        
        Args:
            olivo: Olivo a crecer
        """
        super().crecer(olivo, CRECIMIENTO_OLIVO)
    
    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """
        Muestra datos del olivo incluyendo tipo de aceituna.
        
        Args:
            olivo: Olivo a mostrar
        """
        print(f"Tipo: Olivo")
        print(f"Tipo aceituna: {olivo.get_tipo_aceituna().value}")
        super().mostrar_datos(olivo)