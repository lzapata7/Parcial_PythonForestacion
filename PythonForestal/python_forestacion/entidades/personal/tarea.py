"""
Entidad Tarea - tarea asignada a trabajador.
"""
from datetime import date


class Tarea:
    """
    Representa una tarea agricola asignada.
    """
    
    def __init__(self, id_tarea: int, descripcion: str, fecha_programada: date):
        """
        Inicializa una Tarea.
        
        Args:
            id_tarea: ID unico de la tarea
            descripcion: Descripcion de la tarea
            fecha_programada: Fecha programada para ejecutar
        """
        self._id_tarea = id_tarea
        self._descripcion = descripcion
        self._fecha_programada = fecha_programada
        self._completada = False
    
    def get_id_tarea(self) -> int:
        """
        Obtiene el ID de la tarea.
        
        Returns:
            ID de la tarea
        """
        return self._id_tarea
    
    def set_id_tarea(self, id_tarea: int) -> None:
        """
        Establece el ID de la tarea.
        
        Args:
            id_tarea: ID de la tarea
        """
        self._id_tarea = id_tarea
    
    def get_descripcion(self) -> str:
        """
        Obtiene la descripcion.
        
        Returns:
            Descripcion de la tarea
        """
        return self._descripcion
    
    def set_descripcion(self, descripcion: str) -> None:
        """
        Establece la descripcion.
        
        Args:
            descripcion: Descripcion de la tarea
        """
        self._descripcion = descripcion
    
    def get_fecha_programada(self) -> date:
        """
        Obtiene la fecha programada.
        
        Returns:
            Fecha programada
        """
        return self._fecha_programada
    
    def set_fecha_programada(self, fecha: date) -> None:
        """
        Establece la fecha programada.
        
        Args:
            fecha: Fecha programada
        """
        self._fecha_programada = fecha
    
    def get_completada(self) -> bool:
        """
        Indica si esta completada.
        
        Returns:
            True si esta completada
        """
        return self._completada
    
    def set_completada(self, completada: bool) -> None:
        """
        Establece el estado de completitud.
        
        Args:
            completada: True si esta completada
        """
        self._completada = completada