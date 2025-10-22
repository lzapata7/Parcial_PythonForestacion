"""
Estrategia de absorcion constante para hortalizas.
"""
from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion constante independiente de estacion.
    Hortalizas absorben siempre la misma cantidad.
    """
    
    def __init__(self, cantidad_constante: int):
        """
        Inicializa la estrategia con cantidad fija.
        
        Args:
            cantidad_constante: Litros a absorber siempre
        """
        self._cantidad_constante = cantidad_constante
    
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula absorcion constante.
        
        Args:
            fecha: Fecha actual (no usado)
            temperatura: Temperatura ambiente (no usado)
            humedad: Humedad ambiente (no usado)
            cultivo: Cultivo que absorbe (no usado)
            
        Returns:
            Litros a absorber (siempre constante)
        """
        return self._cantidad_constante