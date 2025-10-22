"""
Servicio base para cultivos.
"""
from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService:
    """
    Servicio base para operaciones sobre cultivos.
    Utiliza Strategy Pattern para absorcion de agua.
    """
    
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        """
        Inicializa el servicio con una estrategia de absorcion.
        
        Args:
            estrategia: Estrategia de absorcion de agua
        """
        self._estrategia = estrategia
    
    def absorver_agua(
        self,
        cultivo: 'Cultivo',
        fecha: date = None,
        temperatura: float = 20.0,
        humedad: float = 50.0
    ) -> int:
        """
        Calcula y aplica absorcion de agua usando estrategia.
        
        Args:
            cultivo: Cultivo que absorbe agua
            fecha: Fecha actual (default: hoy)
            temperatura: Temperatura ambiente
            humedad: Humedad ambiente
            
        Returns:
            Cantidad de agua absorbida en litros
        """
        if fecha is None:
            fecha = date.today()
        
        cantidad = self._estrategia.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        agua_actual = cultivo.get_agua()
        cultivo.set_agua(agua_actual + cantidad)
        
        return cantidad
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos basicos del cultivo.
        
        Args:
            cultivo: Cultivo a mostrar
        """
        print(f"Agua: {cultivo.get_agua()}L")
        print(f"Superficie: {cultivo.get_superficie()}m2")
        print(f"Fecha plantacion: {cultivo.get_fecha_plantacion()}")