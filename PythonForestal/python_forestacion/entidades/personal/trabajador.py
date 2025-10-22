"""
Entidad Trabajador - trabajador agricola.
"""
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.tarea import Tarea
    from python_forestacion.entidades.personal.apto_medico import AptoMedico


class Trabajador:
    """
    Representa un trabajador agricola con tareas asignadas.
    """
    
    def __init__(self, dni: int, nombre: str, tareas: List['Tarea']):
        """
        Inicializa un Trabajador.
        
        Args:
            dni: DNI del trabajador
            nombre: Nombre del trabajador
            tareas: Lista de tareas asignadas
        """
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas
        self._apto_medico = None
    
    def get_dni(self) -> int:
        """
        Obtiene el DNI.
        
        Returns:
            DNI del trabajador
        """
        return self._dni
    
    def set_dni(self, dni: int) -> None:
        """
        Establece el DNI.
        
        Args:
            dni: DNI del trabajador
        """
        self._dni = dni
    
    def get_nombre(self) -> str:
        """
        Obtiene el nombre.
        
        Returns:
            Nombre del trabajador
        """
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre.
        
        Args:
            nombre: Nombre del trabajador
        """
        self._nombre = nombre
    
    def get_tareas(self) -> List['Tarea']:
        """
        Obtiene las tareas asignadas.
        
        Returns:
            Lista de tareas
        """
        return self._tareas.copy()
    
    def agregar_tarea(self, tarea: 'Tarea') -> None:
        """
        Agrega una tarea al trabajador.
        
        Args:
            tarea: Tarea a agregar
        """
        self._tareas.append(tarea)
    
    def get_apto_medico(self) -> Optional['AptoMedico']:
        """
        Obtiene el apto medico.
        
        Returns:
            Apto medico o None
        """
        return self._apto_medico
    
    def set_apto_medico(self, apto: 'AptoMedico') -> None:
        """
        Establece el apto medico.
        
        Args:
            apto: Apto medico
        """
        self._apto_medico = apto
    
    def tiene_apto_medico(self) -> bool:
        """
        Verifica si tiene apto medico valido.
        
        Returns:
            True si tiene apto medico
        """
        return self._apto_medico is not None