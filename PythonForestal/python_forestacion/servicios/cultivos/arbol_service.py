"""
Servicio base para arboles.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """
    Servicio base para arboles.
    Los arboles pueden crecer.
    """
    
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        """
        Inicializa el servicio de arboles.
        
        Args:
            estrategia: Estrategia de absorcion de agua
        """
        super().__init__(estrategia)
    
    def crecer(self, arbol: 'Arbol', incremento: float) -> None:
        """
        Hace crecer el arbol.
        
        Args:
            arbol: Arbol a crecer
            incremento: Incremento de altura en metros
        """
        altura_actual = arbol.get_altura()
        arbol.set_altura(altura_actual + incremento)
    
    def mostrar_datos(self, arbol: 'Arbol') -> None:
        """
        Muestra datos del arbol incluyendo altura.
        
        Args:
            arbol: Arbol a mostrar
        """
        super().mostrar_datos(arbol)
        print(f"Altura: {arbol.get_altura():.2f}m")