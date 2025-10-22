"""
Entidad AptoMedico - certificacion medica de trabajador.
"""
from datetime import date


class AptoMedico:
    """
    Representa una certificacion medica de un trabajador.
    """
    
    def __init__(self, fecha_emision: date, observaciones: str):
        """
        Inicializa un AptoMedico.
        
        Args:
            fecha_emision: Fecha de emision del apto
            observaciones: Observaciones medicas
        """
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones
    
    def get_fecha_emision(self) -> date:
        """
        Obtiene la fecha de emision.
        
        Returns:
            Fecha de emision
        """
        return self._fecha_emision
    
    def set_fecha_emision(self, fecha: date) -> None:
        """
        Establece la fecha de emision.
        
        Args:
            fecha: Fecha de emision
        """
        self._fecha_emision = fecha
    
    def get_observaciones(self) -> str:
        """
        Obtiene las observaciones.
        
        Returns:
            Observaciones medicas
        """
        return self._observaciones
    
    def set_observaciones(self, observaciones: str) -> None:
        """
        Establece las observaciones.
        
        Args:
            observaciones: Observaciones medicas
        """
        self._observaciones = observaciones