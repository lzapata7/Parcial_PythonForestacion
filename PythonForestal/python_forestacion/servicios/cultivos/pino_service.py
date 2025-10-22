"""
Servicio para cultivos Pino.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio para operaciones sobre Pino.
    Usa estrategia seasonal para absorcion.
    """
    
    def __init__(self):
        """
        Inicializa el servicio de Pino con estrategia seasonal.
        """
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, pino: 'Pino') -> None:
        """
        Hace crecer el pino con incremento especifico.
        
        Args:
            pino: Pino a crecer
        """
        super().crecer(pino, CRECIMIENTO_PINO)
    
    def mostrar_datos(self, pino: 'Pino') -> None:
        """
        Muestra datos del pino incluyendo variedad.
        
        Args:
            pino: Pino a mostrar
        """
        print(f"Tipo: Pino")
        print(f"Variedad: {pino.get_variedad()}")
        super().mostrar_datos(pino)