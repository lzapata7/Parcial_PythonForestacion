"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/entidades/personal
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/__init__.py
# ================================================================================

"""
Paquete de entidades de personal.
"""
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

__all__ = [
    'Trabajador',
    'Herramienta',
    'Tarea',
    'AptoMedico'
]

# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

"""
Entidad Herramienta - herramienta de trabajo.
"""


class Herramienta:
    """
    Representa una herramienta de trabajo con certificacion.
    """
    
    def __init__(self, id_herramienta: int, nombre: str, certificacion_hs: bool):
        """
        Inicializa una Herramienta.
        
        Args:
            id_herramienta: ID unico de la herramienta
            nombre: Nombre de la herramienta
            certificacion_hs: Si tiene certificacion de higiene y seguridad
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificacion_hs = certificacion_hs
    
    def get_id_herramienta(self) -> int:
        """
        Obtiene el ID de la herramienta.
        
        Returns:
            ID de la herramienta
        """
        return self._id_herramienta
    
    def set_id_herramienta(self, id_herramienta: int) -> None:
        """
        Establece el ID de la herramienta.
        
        Args:
            id_herramienta: ID de la herramienta
        """
        self._id_herramienta = id_herramienta
    
    def get_nombre(self) -> str:
        """
        Obtiene el nombre de la herramienta.
        
        Returns:
            Nombre de la herramienta
        """
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la herramienta.
        
        Args:
            nombre: Nombre de la herramienta
        """
        self._nombre = nombre
    
    def get_certificacion_hs(self) -> bool:
        """
        Indica si tiene certificacion H&S.
        
        Returns:
            True si tiene certificacion
        """
        return self._certificacion_hs
    
    def set_certificacion_hs(self, certificacion: bool) -> None:
        """
        Establece la certificacion H&S.
        
        Args:
            certificacion: True si tiene certificacion
        """
        self._certificacion_hs = certificacion

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/tarea.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

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

