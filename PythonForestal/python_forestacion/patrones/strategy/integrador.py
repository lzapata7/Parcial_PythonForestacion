"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/__init__.py
# ================================================================================

"""
Paquete del patron Strategy.
"""
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

__all__ = ['AbsorcionAguaStrategy']

# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

"""
Interfaz Strategy para algoritmos de absorcion de agua.
"""
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz para estrategias de absorcion de agua.
    """
    
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua a absorber.
        
        Args:
            fecha: Fecha actual
            temperatura: Temperatura ambiente
            humedad: Humedad ambiente
            cultivo: Cultivo que absorbe agua
            
        Returns:
            Cantidad de agua a absorber en litros
        """
        pass

