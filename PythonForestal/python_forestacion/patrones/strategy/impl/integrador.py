"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================

"""
Implementaciones del patron Strategy.
"""
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionSeasonalStrategy',
    'AbsorcionConstanteStrategy'
]

# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

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

