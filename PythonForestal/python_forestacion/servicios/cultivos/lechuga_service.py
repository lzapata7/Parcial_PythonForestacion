"""
Servicio para cultivos Lechuga.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """
    Servicio para operaciones sobre Lechuga.
    Usa estrategia constante para absorcion (1L).
    """
    
    def __init__(self):
        """
        Inicializa el servicio de Lechuga con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(1))
    
    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """
        Muestra datos de la lechuga incluyendo variedad.
        
        Args:
            lechuga: Lechuga a mostrar
        """
        print(f"Tipo: Lechuga")
        print(f"Variedad: {lechuga.get_variedad()}")
        print(f"Invernadero: {lechuga.get_invernadero()}")
        super().mostrar_datos(lechuga)