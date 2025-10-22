"""
Estrategia de absorcion seasonal para arboles.
"""
from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion basada en estacion del año.
    Arboles absorben mas agua en verano.
    """
    
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula absorcion segun estacion.
        
        Args:
            fecha: Fecha actual
            temperatura: Temperatura ambiente (no usado)
            humedad: Humedad ambiente (no usado)
            cultivo: Cultivo que absorbe
            
        Returns:
            Litros a absorber
        """
        mes = fecha.month
        
        if MES_INICIO_VERANO <= mes or mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO