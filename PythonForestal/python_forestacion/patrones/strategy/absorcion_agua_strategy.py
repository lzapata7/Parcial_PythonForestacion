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