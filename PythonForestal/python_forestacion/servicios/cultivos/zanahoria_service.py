"""
Servicio para cultivos Zanahoria.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio para operaciones sobre Zanahoria.
    Usa estrategia constante para absorcion (2L).
    """
    
    def __init__(self):
        """
        Inicializa el servicio de Zanahoria con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(2))
    
    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """
        Muestra datos de la zanahoria incluyendo tipo.
        
        Args:
            zanahoria: Zanahoria a mostrar
        """
        print(f"Tipo: Zanahoria")
        tipo = "Baby carrot" if zanahoria.get_es_baby() else "Regular"
        print(f"Tipo: {tipo}")
        print(f"Invernadero: {zanahoria.get_invernadero()}")
        super().mostrar_datos(zanahoria)