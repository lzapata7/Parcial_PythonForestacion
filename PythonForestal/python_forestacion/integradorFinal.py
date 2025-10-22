"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/lzapata/PythonForestal/python_forestacion/
Fecha de generacion: 2025-10-21 22:13:25
Total de archivos integrados: 63
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades/cultivos
#   4. __init__.py
#   5. arbol.py
#   6. cultivo.py
#   7. hortaliza.py
#   8. lechuga.py
#   9. olivo.py
#   10. pino.py
#   11. tipo_aceituna.py
#   12. zanahoria.py
#
# DIRECTORIO: entidades/personal
#   13. __init__.py
#   14. apto_medico.py
#   15. herramienta.py
#   16. tarea.py
#   17. trabajador.py
#
# DIRECTORIO: entidades/terrenos
#   18. __init__.py
#   19. plantacion.py
#   20. registro_forestal.py
#   21. tierra.py
#
# DIRECTORIO: excepciones
#   22. __init__.py
#   23. agua_agotada_exception.py
#   24. forestacion_exception.py
#   25. mensajes_exception.py
#   26. persistencia_exception.py
#   27. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   28. __init__.py
#
# DIRECTORIO: patrones/factory
#   29. __init__.py
#   30. cultivo_factory.py
#
# DIRECTORIO: patrones/observer
#   31. __init__.py
#   32. observable.py
#   33. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#   34. __init__.py
#
# DIRECTORIO: patrones/singleton
#   35. __init__.py
#
# DIRECTORIO: patrones/strategy
#   36. __init__.py
#   37. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   38. __init__.py
#   39. absorcion_constante_strategy.py
#   40. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   41. __init__.py
#
# DIRECTORIO: riego/control
#   42. __init__.py
#   43. control_riego_task.py
#
# DIRECTORIO: riego/sensores
#   44. __init__.py
#   45. humedad_reader_task.py
#   46. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   47. __init__.py
#
# DIRECTORIO: servicios/cultivos
#   48. __init__.py
#   49. arbol_service.py
#   50. cultivo_service.py
#   51. cultivo_service_registry.py
#   52. lechuga_service.py
#   53. olivo_service.py
#   54. pino_service.py
#   55. zanahoria_service.py
#
# DIRECTORIO: servicios/negocio
#   56. __init__.py
#   57. paquete.py
#
# DIRECTORIO: servicios/personal
#   58. __init__.py
#   59. trabajador_service.py
#
# DIRECTORIO: servicios/terrenos
#   60. __init__.py
#   61. plantacion_service.py
#   62. registro_forestal_service.py
#   63. tierra_service.py
#
# DIRECTORIO: PythonForestal
#   64. main.py



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/64: __init__.py
# Directorio: .
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/__init__.py
# ==============================================================================

"""
Sistema de Gestion Forestal - Paquete principal.

Este sistema demuestra la implementacion de multiples patrones de diseno:
- Singleton: CultivoServiceRegistry
- Factory Method: CultivoFactory
- Observer: Sistema de sensores
- Strategy: Estrategias de absorcion de agua
- Registry: Despacho polimorfico

Version: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Sistema Forestal"

# ==============================================================================
# ARCHIVO 2/64: constantes.py
# Directorio: .
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/constantes.py
# ==============================================================================

"""
Constantes centralizadas del sistema de gestion forestal.
Todas las constantes magicas del proyecto se definen aqui.
"""

# ============================================================================
# CONSTANTES DE AGUA
# ============================================================================
AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# ============================================================================
# CONSTANTES DE RIEGO
# ============================================================================
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50

# ============================================================================
# CONSTANTES DE CULTIVOS - PINO
# ============================================================================
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
CRECIMIENTO_PINO = 0.10

# ============================================================================
# CONSTANTES DE CULTIVOS - OLIVO
# ============================================================================
SUPERFICIE_OLIVO = 1.5
AGUA_INICIAL_OLIVO = 2
CRECIMIENTO_OLIVO = 0.01

# ============================================================================
# CONSTANTES DE CULTIVOS - LECHUGA
# ============================================================================
SUPERFICIE_LECHUGA = 0.5
AGUA_INICIAL_LECHUGA = 1

# ============================================================================
# CONSTANTES DE CULTIVOS - ZANAHORIA
# ============================================================================
SUPERFICIE_ZANAHORIA = 0.3
AGUA_INICIAL_ZANAHORIA = 2

# ============================================================================
# CONSTANTES DE ABSORCION DE AGUA
# ============================================================================
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
MES_INICIO_VERANO = 12
MES_FIN_VERANO = 3

# ============================================================================
# CONSTANTES DE SENSORES
# ============================================================================
INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0
INTERVALO_CONTROL_RIEGO = 2.5

TEMP_MIN_SENSOR = -25
TEMP_MAX_SENSOR = 50
HUMEDAD_MIN_SENSOR = 0
HUMEDAD_MAX_SENSOR = 100

# ============================================================================
# CONSTANTES DE PERSISTENCIA
# ============================================================================
DIRECTORIO_DATOS = "data"
EXTENSION_ARCHIVO = ".dat"

# ============================================================================
# CONSTANTES DE SISTEMA
# ============================================================================
TIMEOUT_THREAD = 1.0


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/64: __init__.py
# Directorio: entidades
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/__init__.py
# ==============================================================================

"""
Paquete de entidades del sistema forestal.
Contiene todos los objetos de dominio (DTOs).
"""


################################################################################
# DIRECTORIO: entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 4/64: __init__.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================

"""
Paquete de entidades de cultivos.
"""
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna

__all__ = [
    'Cultivo',
    'Arbol',
    'Hortaliza',
    'Pino',
    'Olivo',
    'Lechuga',
    'Zanahoria',
    'TipoAceituna'
]

# ==============================================================================
# ARCHIVO 5/64: arbol.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

"""
Entidad base Arbol - base para todos los arboles del sistema.
"""
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Arbol(Cultivo):
    """
    Clase base para cultivos arboreos.
    Los arboles tienen altura y pueden crecer.
    """
    
    def __init__(self, agua: int, superficie: float, altura: float):
        """
        Inicializa un arbol.
        
        Args:
            agua: Agua inicial en litros
            superficie: Superficie en m2
            altura: Altura inicial en metros
        """
        super().__init__(agua, superficie)
        self._altura = altura
    
    def get_altura(self) -> float:
        """
        Obtiene la altura del arbol.
        
        Returns:
            Altura en metros
        """
        return self._altura
    
    def set_altura(self, altura: float) -> None:
        """
        Establece la altura del arbol.
        
        Args:
            altura: Altura en metros
        """
        self._altura = altura

# ==============================================================================
# ARCHIVO 6/64: cultivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

"""
Entidad base Cultivo - interfaz para todos los cultivos del sistema.
"""
from abc import ABC
from datetime import date


class Cultivo(ABC):
    """
    Clase abstracta base para todos los cultivos.
    Define la interfaz comun que deben implementar todos los tipos de cultivos.
    """
    
    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo con sus propiedades basicas.
        
        Args:
            agua: Agua inicial en litros
            superficie: Superficie que ocupa en m2
        """
        self._agua = agua
        self._superficie = superficie
        self._fecha_plantacion = date.today()
    
    def get_agua(self) -> int:
        """
        Obtiene el agua del cultivo.
        
        Returns:
            Agua en litros
        """
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        """
        Establece el agua del cultivo.
        
        Args:
            agua: Agua en litros
        """
        self._agua = agua
    
    def get_superficie(self) -> float:
        """
        Obtiene la superficie del cultivo.
        
        Returns:
            Superficie en m2
        """
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie del cultivo.
        
        Args:
            superficie: Superficie en m2
        """
        self._superficie = superficie
    
    def get_fecha_plantacion(self) -> date:
        """
        Obtiene la fecha de plantacion.
        
        Returns:
            Fecha de plantacion
        """
        return self._fecha_plantacion
    
    def set_fecha_plantacion(self, fecha: date) -> None:
        """
        Establece la fecha de plantacion.
        
        Args:
            fecha: Fecha de plantacion
        """
        self._fecha_plantacion = fecha

# ==============================================================================
# ARCHIVO 7/64: hortaliza.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

"""
Entidad base Hortaliza - base para todas las hortalizas del sistema.
"""
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo):
    """
    Clase base para cultivos horticolas.
    Las hortalizas pueden requerir invernadero.
    """
    
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza.
        
        Args:
            agua: Agua inicial en litros
            superficie: Superficie en m2
            invernadero: Si requiere invernadero
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero
    
    def get_invernadero(self) -> bool:
        """
        Indica si requiere invernadero.
        
        Returns:
            True si requiere invernadero
        """
        return self._invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        """
        Establece si requiere invernadero.
        
        Args:
            invernadero: True si requiere invernadero
        """
        self._invernadero = invernadero

# ==============================================================================
# ARCHIVO 8/64: lechuga.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

"""
Entidad Lechuga - hortaliza tipo Lechuga.
"""
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)


class Lechuga(Hortaliza):
    """
    Cultivo de tipo Lechuga.
    Es una hortaliza de invernadero con variedad configurable.
    """
    
    def __init__(self, variedad: str):
        """
        Inicializa una Lechuga.
        
        Args:
            variedad: Variedad de la lechuga
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        """
        Obtiene la variedad de la lechuga.
        
        Returns:
            Variedad de la lechuga
        """
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad de la lechuga.
        
        Args:
            variedad: Variedad de la lechuga
        """
        self._variedad = variedad

# ==============================================================================
# ARCHIVO 9/64: olivo.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

"""
Entidad Olivo - arbol tipo Olivo.
"""
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO
)


class Olivo(Arbol):
    """
    Cultivo de tipo Olivo.
    Es un arbol con tipo de aceituna.
    """
    
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un Olivo.
        
        Args:
            tipo_aceituna: Tipo de aceituna del olivo
        """
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=0.0
        )
        self._tipo_aceituna = tipo_aceituna
    
    def get_tipo_aceituna(self) -> TipoAceituna:
        """
        Obtiene el tipo de aceituna.
        
        Returns:
            Tipo de aceituna
        """
        return self._tipo_aceituna
    
    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """
        Establece el tipo de aceituna.
        
        Args:
            tipo_aceituna: Tipo de aceituna
        """
        self._tipo_aceituna = tipo_aceituna

# ==============================================================================
# ARCHIVO 10/64: pino.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

"""
Entidad Pino - arbol tipo Pino.
"""
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO
)


class Pino(Arbol):
    """
    Cultivo de tipo Pino.
    Es un arbol con variedad configurable.
    """
    
    def __init__(self, variedad: str):
        """
        Inicializa un Pino.
        
        Args:
            variedad: Variedad del pino (Parana, Elliott, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=0.0
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        """
        Obtiene la variedad del pino.
        
        Returns:
            Variedad del pino
        """
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad del pino.
        
        Args:
            variedad: Variedad del pino
        """
        self._variedad = variedad

# ==============================================================================
# ARCHIVO 11/64: tipo_aceituna.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

"""
Enum para tipos de aceituna.
"""
from enum import Enum


class TipoAceituna(Enum):
    """
    Tipos de aceituna disponibles para olivos.
    """
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

# ==============================================================================
# ARCHIVO 12/64: zanahoria.py
# Directorio: entidades/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

"""
Entidad Zanahoria - hortaliza tipo Zanahoria.
"""
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Hortaliza):
    """
    Cultivo de tipo Zanahoria.
    Es una hortaliza con opcion de baby carrot.
    """
    
    def __init__(self, es_baby: bool):
        """
        Inicializa una Zanahoria.
        
        Args:
            es_baby: Si es baby carrot
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby = es_baby
    
    def get_es_baby(self) -> bool:
        """
        Indica si es baby carrot.
        
        Returns:
            True si es baby carrot
        """
        return self._es_baby
    
    def set_es_baby(self, es_baby: bool) -> None:
        """
        Establece si es baby carrot.
        
        Args:
            es_baby: True si es baby carrot
        """
        self._es_baby = es_baby


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 13/64: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/__init__.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 14/64: apto_medico.py
# Directorio: entidades/personal
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 15/64: herramienta.py
# Directorio: entidades/personal
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 16/64: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 17/64: trabajador.py
# Directorio: entidades/personal
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 18/64: __init__.py
# Directorio: entidades/terrenos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================

"""
Paquete de entidades de terrenos.
"""
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal

__all__ = [
    'Tierra',
    'Plantacion',
    'RegistroForestal'
]

# ==============================================================================
# ARCHIVO 19/64: plantacion.py
# Directorio: entidades/terrenos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

"""
Entidad Plantacion - plantacion agricola.
"""
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """
    Representa una plantacion con cultivos y trabajadores.
    """
    
    def __init__(self, nombre: str, superficie_disponible: float, agua_disponible: int):
        """
        Inicializa una Plantacion.
        
        Args:
            nombre: Nombre de la plantacion
            superficie_disponible: Superficie disponible en m2
            agua_disponible: Agua disponible en litros
        """
        self._nombre = nombre
        self._superficie_disponible = superficie_disponible
        self._agua_disponible = agua_disponible
        self._cultivos = []
        self._trabajadores = []
    
    def get_nombre(self) -> str:
        """
        Obtiene el nombre.
        
        Returns:
            Nombre de la plantacion
        """
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre.
        
        Args:
            nombre: Nombre de la plantacion
        """
        self._nombre = nombre
    
    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie disponible.
        
        Returns:
            Superficie disponible en m2
        """
        return self._superficie_disponible
    
    def set_superficie_disponible(self, superficie: float) -> None:
        """
        Establece la superficie disponible.
        
        Args:
            superficie: Superficie disponible en m2
        """
        self._superficie_disponible = superficie
    
    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.
        
        Returns:
            Agua disponible en litros
        """
        return self._agua_disponible
    
    def set_agua_disponible(self, agua: int) -> None:
        """
        Establece el agua disponible.
        
        Args:
            agua: Agua disponible en litros
        """
        self._agua_disponible = agua
    
    def get_cultivos(self) -> List['Cultivo']:
        """
        Obtiene la lista de cultivos.
        
        Returns:
            Lista de cultivos
        """
        return self._cultivos.copy()
    
    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """
        Agrega un cultivo a la plantacion.
        
        Args:
            cultivo: Cultivo a agregar
        """
        self._cultivos.append(cultivo)
    
    def get_trabajadores(self) -> List['Trabajador']:
        """
        Obtiene la lista de trabajadores.
        
        Returns:
            Lista de trabajadores
        """
        return self._trabajadores.copy()
    
    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        """
        Agrega un trabajador a la plantacion.
        
        Args:
            trabajador: Trabajador a agregar
        """
        self._trabajadores.append(trabajador)

# ==============================================================================
# ARCHIVO 20/64: registro_forestal.py
# Directorio: entidades/terrenos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

"""
Entidad RegistroForestal - registro completo de tierra y plantacion.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """
    Vincula tierra con plantacion y propietario.
    """
    
    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa un RegistroForestal.
        
        Args:
            id_padron: ID del padron catastral
            tierra: Tierra asociada
            plantacion: Plantacion asociada
            propietario: Nombre del propietario
            avaluo: Avaluo fiscal
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo
    
    def get_id_padron(self) -> int:
        """
        Obtiene el ID del padron.
        
        Returns:
            ID del padron
        """
        return self._id_padron
    
    def set_id_padron(self, id_padron: int) -> None:
        """
        Establece el ID del padron.
        
        Args:
            id_padron: ID del padron
        """
        self._id_padron = id_padron
    
    def get_tierra(self) -> 'Tierra':
        """
        Obtiene la tierra.
        
        Returns:
            Tierra asociada
        """
        return self._tierra
    
    def set_tierra(self, tierra: 'Tierra') -> None:
        """
        Establece la tierra.
        
        Args:
            tierra: Tierra a asociar
        """
        self._tierra = tierra
    
    def get_plantacion(self) -> 'Plantacion':
        """
        Obtiene la plantacion.
        
        Returns:
            Plantacion asociada
        """
        return self._plantacion
    
    def set_plantacion(self, plantacion: 'Plantacion') -> None:
        """
        Establece la plantacion.
        
        Args:
            plantacion: Plantacion a asociar
        """
        self._plantacion = plantacion
    
    def get_propietario(self) -> str:
        """
        Obtiene el propietario.
        
        Returns:
            Nombre del propietario
        """
        return self._propietario
    
    def set_propietario(self, propietario: str) -> None:
        """
        Establece el propietario.
        
        Args:
            propietario: Nombre del propietario
        """
        self._propietario = propietario
    
    def get_avaluo(self) -> float:
        """
        Obtiene el avaluo.
        
        Returns:
            Avaluo fiscal
        """
        return self._avaluo
    
    def set_avaluo(self, avaluo: float) -> None:
        """
        Establece el avaluo.
        
        Args:
            avaluo: Avaluo fiscal
        """
        self._avaluo = avaluo

# ==============================================================================
# ARCHIVO 21/64: tierra.py
# Directorio: entidades/terrenos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

"""
Entidad Tierra - terreno catastral.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """
    Representa un terreno catastral.
    """
    
    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        """
        Inicializa una Tierra.
        
        Args:
            id_padron_catastral: Identificador unico del padron
            superficie: Superficie total en m2
            domicilio: Ubicacion del terreno
        """
        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = None
    
    def get_id_padron_catastral(self) -> int:
        """
        Obtiene el padron catastral.
        
        Returns:
            ID del padron catastral
        """
        return self._id_padron_catastral
    
    def set_id_padron_catastral(self, id_padron: int) -> None:
        """
        Establece el padron catastral.
        
        Args:
            id_padron: ID del padron catastral
        """
        self._id_padron_catastral = id_padron
    
    def get_superficie(self) -> float:
        """
        Obtiene la superficie.
        
        Returns:
            Superficie en m2
        """
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie.
        
        Args:
            superficie: Superficie en m2
        """
        self._superficie = superficie
    
    def get_domicilio(self) -> str:
        """
        Obtiene el domicilio.
        
        Returns:
            Domicilio del terreno
        """
        return self._domicilio
    
    def set_domicilio(self, domicilio: str) -> None:
        """
        Establece el domicilio.
        
        Args:
            domicilio: Domicilio del terreno
        """
        self._domicilio = domicilio
    
    def get_finca(self) -> 'Plantacion':
        """
        Obtiene la plantacion asociada.
        
        Returns:
            Plantacion del terreno
        """
        return self._finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        """
        Establece la plantacion asociada.
        
        Args:
            finca: Plantacion a asociar
        """
        self._finca = finca


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 22/64: __init__.py
# Directorio: excepciones
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/excepciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 23/64: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

"""
Excepcion para agua agotada en plantacion.
"""
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class AguaAgotadaException(ForestacionException):
    """
    Se lanza cuando no hay suficiente agua para regar cultivos.
    """
    
    def __init__(self, agua_requerida: int, agua_disponible: int):
        """
        Inicializa la excepcion con datos de agua.
        
        Args:
            agua_requerida: Agua necesaria en litros
            agua_disponible: Agua disponible en litros
        """
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible
        
        user_message = (
            f"Agua agotada. Se requieren {agua_requerida} litros pero solo hay "
            f"{agua_disponible} litros disponibles."
        )
        
        technical_message = (
            f"AguaAgotadaException: "
            f"Requerida={agua_requerida}L, "
            f"Disponible={agua_disponible}L, "
            f"Deficit={agua_requerida - agua_disponible}L"
        )
        
        super().__init__(user_message, technical_message)
    
    def get_agua_requerida(self) -> int:
        """
        Obtiene el agua requerida.
        
        Returns:
            Agua requerida en litros
        """
        return self._agua_requerida
    
    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.
        
        Returns:
            Agua disponible en litros
        """
        return self._agua_disponible

# ==============================================================================
# ARCHIVO 24/64: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

"""
Excepcion base del sistema de gestion forestal.
"""


class ForestacionException(Exception):
    """
    Excepcion base para todas las excepciones del sistema forestal.
    
    Proporciona mensajes separados para usuario y tecnico.
    """
    
    def __init__(self, user_message: str, technical_message: str = None):
        """
        Inicializa la excepcion con mensajes personalizados.
        
        Args:
            user_message: Mensaje amigable para el usuario final
            technical_message: Mensaje tecnico con detalles del error
        """
        self._user_message = user_message
        self._technical_message = technical_message or user_message
        super().__init__(self._user_message)
    
    def get_user_message(self) -> str:
        """
        Obtiene el mensaje para el usuario.
        
        Returns:
            Mensaje amigable para el usuario
        """
        return self._user_message
    
    def get_technical_message(self) -> str:
        """
        Obtiene el mensaje tecnico.
        
        Returns:
            Mensaje con detalles tecnicos
        """
        return self._technical_message
    
    def get_full_message(self) -> str:
        """
        Obtiene ambos mensajes concatenados.
        
        Returns:
            Mensaje completo con informacion de usuario y tecnica
        """
        if self._user_message == self._technical_message:
            return self._user_message
        return f"{self._user_message}\n[Tecnico]: {self._technical_message}"

# ==============================================================================
# ARCHIVO 25/64: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

"""
Mensajes centralizados para excepciones del sistema.
"""


class MensajesException:
    """
    Clase con mensajes de error centralizados.
    """
    
    # Mensajes de superficie
    SUPERFICIE_INSUFICIENTE = "No hay suficiente superficie disponible para plantar"
    
    # Mensajes de agua
    AGUA_AGOTADA = "El agua disponible se ha agotado"
    AGUA_INSUFICIENTE = "No hay suficiente agua para realizar el riego"
    
    # Mensajes de persistencia
    ERROR_GUARDAR = "Error al guardar el archivo"
    ERROR_LEER = "Error al leer el archivo"
    ARCHIVO_NO_EXISTE = "El archivo no existe"
    
    # Mensajes de validacion
    VALOR_NEGATIVO = "El valor no puede ser negativo"
    VALOR_INVALIDO = "El valor proporcionado no es valido"

# ==============================================================================
# ARCHIVO 26/64: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

"""
Excepcion para errores de persistencia.
"""
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class PersistenciaException(ForestacionException):
    """
    Se lanza cuando ocurre un error en operaciones de persistencia.
    """
    
    def __init__(self, operacion: str, ruta: str, causa: Exception = None):
        """
        Inicializa la excepcion con datos de la operacion fallida.
        
        Args:
            operacion: Tipo de operacion (guardar/leer)
            ruta: Ruta del archivo
            causa: Excepcion original que causo el error
        """
        self._operacion = operacion
        self._ruta = ruta
        self._causa = causa
        
        user_message = (
            f"Error al {operacion} el archivo: {ruta}"
        )
        
        technical_message = (
            f"PersistenciaException: Operacion={operacion}, Ruta={ruta}"
        )
        
        if causa:
            technical_message += f", Causa={type(causa).__name__}: {str(causa)}"
        
        super().__init__(user_message, technical_message)
    
    def get_operacion(self) -> str:
        """
        Obtiene el tipo de operacion.
        
        Returns:
            Nombre de la operacion
        """
        return self._operacion
    
    def get_ruta(self) -> str:
        """
        Obtiene la ruta del archivo.
        
        Returns:
            Ruta del archivo
        """
        return self._ruta
    
    def get_causa(self) -> Exception:
        """
        Obtiene la excepcion original.
        
        Returns:
            Excepcion que causo el error
        """
        return self._causa

# ==============================================================================
# ARCHIVO 27/64: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

"""
Excepcion para superficie insuficiente en plantacion.
"""
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class SuperficieInsuficienteException(ForestacionException):
    """
    Se lanza cuando no hay suficiente superficie para plantar cultivos.
    """
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa la excepcion con datos de superficie.
        
        Args:
            superficie_requerida: Superficie necesaria en m2
            superficie_disponible: Superficie disponible en m2
        """
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
        
        user_message = (
            f"No hay suficiente superficie disponible. "
            f"Se requieren {superficie_requerida:.2f} m2 pero solo hay "
            f"{superficie_disponible:.2f} m2 disponibles."
        )
        
        technical_message = (
            f"SuperficieInsuficienteException: "
            f"Requerida={superficie_requerida}, "
            f"Disponible={superficie_disponible}, "
            f"Deficit={superficie_requerida - superficie_disponible}"
        )
        
        super().__init__(user_message, technical_message)
    
    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie requerida.
        
        Returns:
            Superficie requerida en m2
        """
        return self._superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie disponible.
        
        Returns:
            Superficie disponible en m2
        """
        return self._superficie_disponible


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 28/64: __init__.py
# Directorio: patrones
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/__init__.py
# ==============================================================================

"""
Paquete de patrones de diseno.
"""


################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 29/64: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/factory/__init__.py
# ==============================================================================

"""
Paquete del patron Factory Method.
"""
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

__all__ = ['CultivoFactory']

# ==============================================================================
# ARCHIVO 30/64: cultivo_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

"""
Factory Method para creacion de cultivos.
"""
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """
    Factory para crear cultivos sin conocer clases concretas.
    """
    
    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """
        Crea un cultivo segun la especie especificada.
        
        Args:
            especie: Tipo de cultivo (Pino, Olivo, Lechuga, Zanahoria)
            
        Returns:
            Cultivo creado
            
        Raises:
            ValueError: Si la especie es desconocida
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }
        
        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")
        
        return factories[especie]()
    
    @staticmethod
    def _crear_pino() -> Cultivo:
        """
        Crea un Pino con valores por defecto.
        
        Returns:
            Instancia de Pino
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")
    
    @staticmethod
    def _crear_olivo() -> Cultivo:
        """
        Crea un Olivo con valores por defecto.
        
        Returns:
            Instancia de Olivo
        """
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)
    
    @staticmethod
    def _crear_lechuga() -> Cultivo:
        """
        Crea una Lechuga con valores por defecto.
        
        Returns:
            Instancia de Lechuga
        """
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Criolla")
    
    @staticmethod
    def _crear_zanahoria() -> Cultivo:
        """
        Crea una Zanahoria con valores por defecto.
        
        Returns:
            Instancia de Zanahoria
        """
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(es_baby=False)


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 31/64: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/observer/__init__.py
# ==============================================================================

"""
Paquete del patron Observer.
"""
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.observer import Observer

__all__ = ['Observable', 'Observer']

# ==============================================================================
# ARCHIVO 32/64: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/observer/observable.py
# ==============================================================================

"""
Clase Observable del patron Observer.
"""
from abc import ABC
from typing import Generic, TypeVar, List

from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """
    Clase base para objetos observables.
    Notifica a observadores cuando ocurren eventos.
    """
    
    def __init__(self):
        """
        Inicializa el observable con lista vacia de observadores.
        """
        self._observadores: List[Observer[T]] = []
    
    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador a la lista.
        
        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)
    
    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista.
        
        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)
    
    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores de un evento.
        
        Args:
            evento: Evento a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 33/64: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/observer/observer.py
# ==============================================================================

"""
Interfaz Observer del patron Observer.
"""
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz para observadores que reciben notificaciones.
    """
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Se llama cuando el observable notifica un evento.
        
        Args:
            evento: Evento recibido del observable
        """
        pass


################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 34/64: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================

"""
Paquete de eventos para Observer.
"""


################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 35/64: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================

"""
Paquete del patron Singleton.
"""


################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 36/64: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================

"""
Paquete del patron Strategy.
"""
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

__all__ = ['AbsorcionAguaStrategy']

# ==============================================================================
# ARCHIVO 37/64: absorcion_agua_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 38/64: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================

"""
Implementaciones del patron Strategy.
"""
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

__all__ = [
    'AbsorcionSeasonalStrategy',
    'AbsorcionConstanteStrategy'
]

# ==============================================================================
# ARCHIVO 39/64: absorcion_constante_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 40/64: absorcion_seasonal_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 41/64: __init__.py
# Directorio: riego
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/riego/__init__.py
# ==============================================================================

"""
Paquete del sistema de riego automatizado.
"""


################################################################################
# DIRECTORIO: riego/control
################################################################################

# ==============================================================================
# ARCHIVO 42/64: __init__.py
# Directorio: riego/control
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/riego/control/__init__.py
# ==============================================================================

"""
Paquete de control de riego.
"""
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

__all__ = ['ControlRiegoTask']

# ==============================================================================
# ARCHIVO 43/64: control_riego_task.py
# Directorio: riego/control
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

"""
Controlador de riego automatico - Observer pattern.
"""
import threading
import time
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)


class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador que observa sensores y riega automaticamente.
    Implementa Observer pattern.
    """
    
    def __init__(
        self,
        sensor_temperatura: TemperaturaReaderTask,
        sensor_humedad: HumedadReaderTask,
        plantacion: Plantacion,
        plantacion_service: PlantacionService
    ):
        """
        Inicializa el controlador de riego.
        
        Args:
            sensor_temperatura: Sensor de temperatura
            sensor_humedad: Sensor de humedad
            plantacion: Plantacion a regar
            plantacion_service: Servicio de plantacion
        """
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        
        self._ultima_temperatura = None
        self._ultima_humedad = None
        
        self._sensor_temperatura.agregar_observador(self)
        self._sensor_humedad.agregar_observador(self)
    
    def actualizar(self, evento: float) -> None:
        """
        Recibe notificaciones de sensores.
        
        Args:
            evento: Valor del sensor (temperatura o humedad)
        """
        pass
    
    def run(self) -> None:
        """
        Loop principal de control de riego.
        """
        while not self._detenido.is_set():
            self._verificar_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)
    
    def _verificar_y_regar(self) -> None:
        """
        Verifica condiciones y riega si es necesario.
        """
        temperatura = self._sensor_temperatura._leer_temperatura()
        humedad = self._sensor_humedad._leer_humedad()
        
        if (TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO and 
            humedad < HUMEDAD_MAX_RIEGO):
            
            try:
                print(f"[RIEGO] Temp: {temperatura:.1f}C, Humedad: {humedad:.1f}%")
                self._plantacion_service.regar(self._plantacion)
            except Exception as e:
                print(f"[!] Error al regar: {e}")
    
    def detener(self) -> None:
        """
        Detiene el controlador de forma limpia.
        """
        self._detenido.set()


################################################################################
# DIRECTORIO: riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 44/64: __init__.py
# Directorio: riego/sensores
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/riego/sensores/__init__.py
# ==============================================================================

"""
Paquete de sensores ambientales.
"""
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

__all__ = ['TemperaturaReaderTask', 'HumedadReaderTask']

# ==============================================================================
# ARCHIVO 45/64: humedad_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

"""
Sensor de humedad - Observable pattern.
"""
import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    HUMEDAD_MIN_SENSOR,
    HUMEDAD_MAX_SENSOR
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Thread que lee humedad continuamente y notifica observadores.
    Implementa Observable pattern.
    """
    
    def __init__(self):
        """
        Inicializa el sensor de humedad.
        """
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    
    def run(self) -> None:
        """
        Ejecuta el loop de lectura de humedad.
        """
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)
    
    def _leer_humedad(self) -> float:
        """
        Simula lectura de humedad.
        
        Returns:
            Humedad en porcentaje
        """
        return random.uniform(HUMEDAD_MIN_SENSOR, HUMEDAD_MAX_SENSOR)
    
    def detener(self) -> None:
        """
        Detiene el sensor de forma limpia.
        """
        self._detenido.set()

# ==============================================================================
# ARCHIVO 46/64: temperatura_reader_task.py
# Directorio: riego/sensores
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

"""
Sensor de temperatura - Observable pattern.
"""
import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    TEMP_MIN_SENSOR,
    TEMP_MAX_SENSOR
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Thread que lee temperatura continuamente y notifica observadores.
    Implementa Observable pattern.
    """
    
    def __init__(self):
        """
        Inicializa el sensor de temperatura.
        """
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    
    def run(self) -> None:
        """
        Ejecuta el loop de lectura de temperatura.
        """
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)
    
    def _leer_temperatura(self) -> float:
        """
        Simula lectura de temperatura.
        
        Returns:
            Temperatura en grados Celsius
        """
        return random.uniform(TEMP_MIN_SENSOR, TEMP_MAX_SENSOR)
    
    def detener(self) -> None:
        """
        Detiene el sensor de forma limpia.
        """
        self._detenido.set()


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 47/64: __init__.py
# Directorio: servicios
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/__init__.py
# ==============================================================================

"""
Paquete de servicios de logica de negocio.
"""


################################################################################
# DIRECTORIO: servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 48/64: __init__.py
# Directorio: servicios/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================

"""
Paquete de servicios de cultivos.
"""
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

__all__ = ['CultivoServiceRegistry']

# ==============================================================================
# ARCHIVO 49/64: arbol_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

"""
Servicio base para arboles.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """
    Servicio base para arboles.
    Los arboles pueden crecer.
    """
    
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        """
        Inicializa el servicio de arboles.
        
        Args:
            estrategia: Estrategia de absorcion de agua
        """
        super().__init__(estrategia)
    
    def crecer(self, arbol: 'Arbol', incremento: float) -> None:
        """
        Hace crecer el arbol.
        
        Args:
            arbol: Arbol a crecer
            incremento: Incremento de altura en metros
        """
        altura_actual = arbol.get_altura()
        arbol.set_altura(altura_actual + incremento)
    
    def mostrar_datos(self, arbol: 'Arbol') -> None:
        """
        Muestra datos del arbol incluyendo altura.
        
        Args:
            arbol: Arbol a mostrar
        """
        super().mostrar_datos(arbol)
        print(f"Altura: {arbol.get_altura():.2f}m")

# ==============================================================================
# ARCHIVO 50/64: cultivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 51/64: cultivo_service_registry.py
# Directorio: servicios/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

"""
Registry de servicios de cultivos - Implementa Singleton Pattern.
"""
from threading import Lock
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoServiceRegistry:
    """
    Registry centralizado de servicios de cultivos.
    Implementa Singleton Pattern thread-safe.
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        """
        Implementa Singleton con double-checked locking.
        
        Returns:
            Instancia unica del registry
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """
        Inicializa los servicios (solo una vez).
        """
        if not hasattr(self, '_initialized'):
            self._pino_service = PinoService()
            self._olivo_service = OlivoService()
            self._lechuga_service = LechugaService()
            self._zanahoria_service = ZanahoriaService()
            
            from python_forestacion.entidades.cultivos.pino import Pino
            from python_forestacion.entidades.cultivos.olivo import Olivo
            from python_forestacion.entidades.cultivos.lechuga import Lechuga
            from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
            
            self._absorber_agua_handlers = {
                Pino: self._absorber_agua_pino,
                Olivo: self._absorber_agua_olivo,
                Lechuga: self._absorber_agua_lechuga,
                Zanahoria: self._absorber_agua_zanahoria
            }
            
            self._mostrar_datos_handlers = {
                Pino: self._mostrar_datos_pino,
                Olivo: self._mostrar_datos_olivo,
                Lechuga: self._mostrar_datos_lechuga,
                Zanahoria: self._mostrar_datos_zanahoria
            }
            
            self._initialized = True
    
    @classmethod
    def get_instance(cls) -> 'CultivoServiceRegistry':
        """
        Obtiene la instancia unica del registry.
        
        Returns:
            Instancia del registry
        """
        return cls()
    
    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """
        Despacha absorcion de agua al servicio apropiado.
        
        Args:
            cultivo: Cultivo que absorbe agua
            
        Returns:
            Cantidad de agua absorbida
            
        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        
        return self._absorber_agua_handlers[tipo](cultivo)
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Despacha mostracion de datos al servicio apropiado.
        
        Args:
            cultivo: Cultivo a mostrar
            
        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        
        self._mostrar_datos_handlers[tipo](cultivo)
    
    def _absorber_agua_pino(self, pino: 'Pino') -> int:
        cantidad = self._pino_service.absorver_agua(pino)
        self._pino_service.crecer(pino)
        return cantidad
    
    def _absorber_agua_olivo(self, olivo: 'Olivo') -> int:
        cantidad = self._olivo_service.absorver_agua(olivo)
        self._olivo_service.crecer(olivo)
        return cantidad
    
    def _absorber_agua_lechuga(self, lechuga: 'Lechuga') -> int:
        return self._lechuga_service.absorver_agua(lechuga)
    
    def _absorber_agua_zanahoria(self, zanahoria: 'Zanahoria') -> int:
        return self._zanahoria_service.absorver_agua(zanahoria)
    
    def _mostrar_datos_pino(self, pino: 'Pino') -> None:
        self._pino_service.mostrar_datos(pino)
    
    def _mostrar_datos_olivo(self, olivo: 'Olivo') -> None:
        self._olivo_service.mostrar_datos(olivo)
    
    def _mostrar_datos_lechuga(self, lechuga: 'Lechuga') -> None:
        self._lechuga_service.mostrar_datos(lechuga)
    
    def _mostrar_datos_zanahoria(self, zanahoria: 'Zanahoria') -> None:
        self._zanahoria_service.mostrar_datos(zanahoria)

# ==============================================================================
# ARCHIVO 52/64: lechuga_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

"""
Servicio para cultivos Lechuga.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """
    Servicio para operaciones sobre Lechuga.
    Usa estrategia constante para absorcion (1L).
    """
    
    def __init__(self):
        """
        Inicializa el servicio de Lechuga con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(1))
    
    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """
        Muestra datos de la lechuga incluyendo variedad.
        
        Args:
            lechuga: Lechuga a mostrar
        """
        print(f"Tipo: Lechuga")
        print(f"Variedad: {lechuga.get_variedad()}")
        print(f"Invernadero: {lechuga.get_invernadero()}")
        super().mostrar_datos(lechuga)

# ==============================================================================
# ARCHIVO 53/64: olivo_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

"""
Servicio para cultivos Olivo.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """
    Servicio para operaciones sobre Olivo.
    Usa estrategia seasonal para absorcion.
    """
    
    def __init__(self):
        """
        Inicializa el servicio de Olivo con estrategia seasonal.
        """
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, olivo: 'Olivo') -> None:
        """
        Hace crecer el olivo con incremento especifico.
        
        Args:
            olivo: Olivo a crecer
        """
        super().crecer(olivo, CRECIMIENTO_OLIVO)
    
    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """
        Muestra datos del olivo incluyendo tipo de aceituna.
        
        Args:
            olivo: Olivo a mostrar
        """
        print(f"Tipo: Olivo")
        print(f"Tipo aceituna: {olivo.get_tipo_aceituna().value}")
        super().mostrar_datos(olivo)

# ==============================================================================
# ARCHIVO 54/64: pino_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

"""
Servicio para cultivos Pino.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio para operaciones sobre Pino.
    Usa estrategia seasonal para absorcion.
    """
    
    def __init__(self):
        """
        Inicializa el servicio de Pino con estrategia seasonal.
        """
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, pino: 'Pino') -> None:
        """
        Hace crecer el pino con incremento especifico.
        
        Args:
            pino: Pino a crecer
        """
        super().crecer(pino, CRECIMIENTO_PINO)
    
    def mostrar_datos(self, pino: 'Pino') -> None:
        """
        Muestra datos del pino incluyendo variedad.
        
        Args:
            pino: Pino a mostrar
        """
        print(f"Tipo: Pino")
        print(f"Variedad: {pino.get_variedad()}")
        super().mostrar_datos(pino)

# ==============================================================================
# ARCHIVO 55/64: zanahoria_service.py
# Directorio: servicios/cultivos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

"""
Servicio para cultivos Zanahoria.
"""
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio para operaciones sobre Zanahoria.
    Usa estrategia constante para absorcion (2L).
    """
    
    def __init__(self):
        """
        Inicializa el servicio de Zanahoria con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(2))
    
    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """
        Muestra datos de la zanahoria incluyendo tipo.
        
        Args:
            zanahoria: Zanahoria a mostrar
        """
        print(f"Tipo: Zanahoria")
        tipo = "Baby carrot" if zanahoria.get_es_baby() else "Regular"
        print(f"Tipo: {tipo}")
        print(f"Invernadero: {zanahoria.get_invernadero()}")
        super().mostrar_datos(zanahoria)


################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 56/64: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================

"""
Paquete de servicios de negocio de alto nivel.
"""
from python_forestacion.servicios.negocio.paquete import Paquete

__all__ = ['Paquete']

# ==============================================================================
# ARCHIVO 57/64: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

"""
Clase generica Paquete para empaquetado tipado.
"""
from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Paquete generico tipo-seguro para agrupar cultivos cosechados.
    """
    
    def __init__(self, tipo: str):
        """
        Inicializa un paquete vacio.
        
        Args:
            tipo: Descripcion del tipo de contenido
        """
        self._tipo = tipo
        self._contenido: List[T] = []
    
    def agregar(self, item: T) -> None:
        """
        Agrega un item al paquete.
        
        Args:
            item: Item a agregar
        """
        self._contenido.append(item)
    
    def get_contenido(self) -> List[T]:
        """
        Obtiene el contenido del paquete.
        
        Returns:
            Lista de items
        """
        return self._contenido.copy()
    
    def get_tipo(self) -> str:
        """
        Obtiene el tipo del paquete.
        
        Returns:
            Tipo del paquete
        """
        return self._tipo
    
    def cantidad(self) -> int:
        """
        Obtiene la cantidad de items.
        
        Returns:
            Cantidad de items
        """
        return len(self._contenido)
    
    def mostrar(self) -> None:
        """
        Muestra el contenido del paquete.
        """
        print(f"Paquete de {self._tipo}: {self.cantidad()} item(s)")
        for idx, item in enumerate(self._contenido, 1):
            print(f"  {idx}. {type(item).__name__}")


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 58/64: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/personal/__init__.py
# ==============================================================================

"""
Paquete de servicios de personal.
"""
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService

__all__ = ['TrabajadorService']

# ==============================================================================
# ARCHIVO 59/64: trabajador_service.py
# Directorio: servicios/personal
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

"""
Servicio para gestion de trabajadores.
"""
from datetime import date
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta


class TrabajadorService:
    """
    Servicio para operaciones sobre trabajadores.
    """
    
    def trabajar(
        self,
        trabajador: Trabajador,
        fecha: date,
        herramienta: Herramienta
    ) -> bool:
        """
        Hace trabajar al trabajador ejecutando sus tareas.
        
        Args:
            trabajador: Trabajador a ejecutar tareas
            fecha: Fecha de trabajo
            herramienta: Herramienta a usar
            
        Returns:
            True si pudo trabajar, False si no tiene apto medico
        """
        if not trabajador.tiene_apto_medico():
            print(f"[!] {trabajador.get_nombre()} no puede trabajar sin apto medico")
            return False
        
        tareas = trabajador.get_tareas()
        tareas_ordenadas = sorted(tareas, key=lambda t: t.get_id_tarea(), reverse=True)
        
        for tarea in tareas_ordenadas:
            if tarea.get_fecha_programada() <= fecha and not tarea.get_completada():
                print(f"Ejecutando tarea {tarea.get_id_tarea()}: {tarea.get_descripcion()}")
                print(f"  Usando herramienta: {herramienta.get_nombre()}")
                tarea.set_completada(True)
        
        return True
    
    def mostrar_datos(self, trabajador: Trabajador) -> None:
        """
        Muestra datos del trabajador.
        
        Args:
            trabajador: Trabajador a mostrar
        """
        print(f"DNI: {trabajador.get_dni()}")
        print(f"Nombre: {trabajador.get_nombre()}")
        print(f"Tareas asignadas: {len(trabajador.get_tareas())}")
        
        apto = trabajador.get_apto_medico()
        if apto:
            print(f"Apto medico: Si (desde {apto.get_fecha_emision()})")
        else:
            print(f"Apto medico: No")


################################################################################
# DIRECTORIO: servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 60/64: __init__.py
# Directorio: servicios/terrenos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================

"""
Paquete de servicios de terrenos.
"""
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService

__all__ = [
    'TierraService',
    'PlantacionService',
    'RegistroForestalService'
]

# ==============================================================================
# ARCHIVO 61/64: plantacion_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

"""
Servicio para gestion de plantaciones.
"""
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException


class PlantacionService:
    """
    Servicio para operaciones sobre plantaciones.
    """
    
    def __init__(self):
        """
        Inicializa el servicio con el registry de cultivos.
        """
        self._registry = CultivoServiceRegistry.get_instance()
    
    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> None:
        """
        Planta cultivos en la plantacion usando Factory.
        
        Args:
            plantacion: Plantacion donde plantar
            especie: Tipo de cultivo
            cantidad: Cantidad a plantar
            
        Raises:
            SuperficieInsuficienteException: Si no hay superficie suficiente
        """
        cultivo_ejemplo = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_ejemplo.get_superficie() * cantidad
        superficie_disponible = plantacion.get_superficie_disponible()
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                superficie_disponible
            )
        
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)
        
        plantacion.set_superficie_disponible(
            superficie_disponible - superficie_requerida
        )
        
        print(f"Se plantaron {cantidad} {especie}(s)")
    
    def regar(self, plantacion: Plantacion) -> None:
        """
        Riega todos los cultivos de la plantacion.
        
        Args:
            plantacion: Plantacion a regar
            
        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        cultivos = plantacion.get_cultivos()
        agua_disponible = plantacion.get_agua_disponible()
        
        agua_total_necesaria = 0
        for cultivo in cultivos:
            agua_total_necesaria += self._calcular_agua_necesaria(cultivo)
        
        if agua_total_necesaria > agua_disponible:
            raise AguaAgotadaException(agua_total_necesaria, agua_disponible)
        
        for cultivo in cultivos:
            cantidad_absorbida = self._registry.absorber_agua(cultivo)
            agua_disponible -= cantidad_absorbida
        
        plantacion.set_agua_disponible(agua_disponible)
        print(f"Riego completado. Agua restante: {agua_disponible}L")
    
    def _calcular_agua_necesaria(self, cultivo: Cultivo) -> int:
        """
        Calcula agua necesaria para un cultivo.
        
        Args:
            cultivo: Cultivo a calcular
            
        Returns:
            Agua necesaria en litros
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        from python_forestacion.constantes import (
            ABSORCION_SEASONAL_VERANO,
            ABSORCION_SEASONAL_INVIERNO
        )
        from datetime import date
        
        if isinstance(cultivo, (Pino, Olivo)):
            mes = date.today().month
            if 12 <= mes or mes <= 3:
                return ABSORCION_SEASONAL_VERANO
            else:
                return ABSORCION_SEASONAL_INVIERNO
        elif isinstance(cultivo, Lechuga):
            return 1
        elif isinstance(cultivo, Zanahoria):
            return 2
        else:
            return 1
    
    def cosechar(self, plantacion: Plantacion) -> None:
        """
        Cosecha todos los cultivos.
        
        Args:
            plantacion: Plantacion a cosechar
        """
        cultivos = plantacion.get_cultivos()
        print(f"Cosechando {len(cultivos)} cultivo(s)...")
        
        for cultivo in cultivos:
            tipo = type(cultivo).__name__
            print(f"- Cosechado: {tipo}")
    
    def fumigar(self, plantacion: Plantacion, plaguicida: str) -> None:
        """
        Fumiga la plantacion con plaguicida.
        
        Args:
            plantacion: Plantacion a fumigar
            plaguicida: Tipo de plaguicida
        """
        cultivos = plantacion.get_cultivos()
        print(f"Fumigando {len(cultivos)} cultivo(s) con {plaguicida}")
    
    def mostrar_datos(self, plantacion: Plantacion) -> None:
        """
        Muestra datos de la plantacion.
        
        Args:
            plantacion: Plantacion a mostrar
        """
        print(f"Nombre: {plantacion.get_nombre()}")
        print(f"Superficie disponible: {plantacion.get_superficie_disponible()}m2")
        print(f"Agua disponible: {plantacion.get_agua_disponible()}L")
        print(f"Cultivos: {len(plantacion.get_cultivos())}")
        print(f"Trabajadores: {len(plantacion.get_trabajadores())}")

# ==============================================================================
# ARCHIVO 62/64: registro_forestal_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

"""
Servicio para gestion de registros forestales.
"""
import os
import pickle
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATOS, EXTENSION_ARCHIVO


class RegistroForestalService:
    """
    Servicio para operaciones sobre registros forestales.
    Incluye persistencia con pickle.
    """
    
    def persistir(self, registro: RegistroForestal) -> None:
        """
        Persiste un registro en disco.
        
        Args:
            registro: Registro a persistir
            
        Raises:
            PersistenciaException: Si ocurre error al guardar
        """
        if not os.path.exists(DIRECTORIO_DATOS):
            os.makedirs(DIRECTORIO_DATOS)
        
        nombre_archivo = f"{registro.get_propietario()}{EXTENSION_ARCHIVO}"
        ruta_completa = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
        
        try:
            with open(ruta_completa, 'wb') as archivo:
                pickle.dump(registro, archivo)
            print(f"Registro guardado: {ruta_completa}")
        except Exception as e:
            raise PersistenciaException("guardar", ruta_completa, e)
    
    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """
        Lee un registro desde disco.
        
        Args:
            propietario: Nombre del propietario
            
        Returns:
            Registro leido
            
        Raises:
            PersistenciaException: Si ocurre error al leer
        """
        nombre_archivo = f"{propietario}{EXTENSION_ARCHIVO}"
        ruta_completa = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
        
        try:
            with open(ruta_completa, 'rb') as archivo:
                registro = pickle.load(archivo)
            print(f"Registro leido: {ruta_completa}")
            return registro
        except FileNotFoundError as e:
            raise PersistenciaException("leer", ruta_completa, e)
        except Exception as e:
            raise PersistenciaException("leer", ruta_completa, e)
    
    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """
        Muestra datos del registro.
        
        Args:
            registro: Registro a mostrar
        """
        print(f"ID Padron: {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo: ${registro.get_avaluo():.2f}")
        
        tierra = registro.get_tierra()
        if tierra:
            print(f"Superficie: {tierra.get_superficie()}m2")
            print(f"Domicilio: {tierra.get_domicilio()}")
        
        plantacion = registro.get_plantacion()
        if plantacion:
            print(f"Plantacion: {plantacion.get_nombre()}")
            print(f"Cultivos: {len(plantacion.get_cultivos())}")

# ==============================================================================
# ARCHIVO 63/64: tierra_service.py
# Directorio: servicios/terrenos
# Ruta completa: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

"""
Servicio para gestion de tierras.
"""
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """
    Servicio para operaciones sobre tierras.
    """
    
    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una tierra con su plantacion asociada.
        
        Args:
            id_padron_catastral: ID del padron
            superficie: Superficie en m2
            domicilio: Ubicacion
            nombre_plantacion: Nombre de la plantacion
            
        Returns:
            Tierra creada con plantacion
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie_disponible=superficie,
            agua_disponible=AGUA_INICIAL_PLANTACION
        )
        
        tierra.set_finca(plantacion)
        
        return tierra
    
    def mostrar_datos(self, tierra: Tierra) -> None:
        """
        Muestra datos de la tierra.
        
        Args:
            tierra: Tierra a mostrar
        """
        print(f"Padron catastral: {tierra.get_id_padron_catastral()}")
        print(f"Superficie: {tierra.get_superficie()}m2")
        print(f"Domicilio: {tierra.get_domicilio()}")
        
        finca = tierra.get_finca()
        if finca:
            print(f"Plantacion: {finca.get_nombre()}")

# ==============================================================================
# ARCHIVO 64/64: main.py
# Directorio: PythonForestal
# Ruta completa: /home/lzapata/PythonForestal/main.py
# ==============================================================================

"""
Sistema de Gestion Forestal - Demostracion de Patrones de Diseno.
Punto de entrada principal del sistema.
"""
import time
from datetime import date

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.entidades.cultivos.cultivo import Cultivo


def imprimir_separador(mensaje: str = "", ancho: int = 70) -> None:
    """
    Imprime un separador visual.
    
    Args:
        mensaje: Mensaje a mostrar
        ancho: Ancho del separador
    """
    if mensaje:
        print("\n" + "=" * ancho)
        print(f"  {mensaje}")
        print("=" * ancho)
    else:
        print("-" * ancho)


def main():
    """
    Funcion principal que demuestra todos los patrones del sistema.
    """
    print("\n" + "=" * 70)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 70)
    
    # ========================================================================
    # PATRON SINGLETON: Registry de servicios
    # ========================================================================
    imprimir_separador("PATRON SINGLETON: Inicializando servicios")
    
    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry.get_instance()
    
    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
    else:
        print("[!] ERROR: Instancias diferentes del Registry")
    
    # ========================================================================
    # Creacion de terreno con plantacion
    # ========================================================================
    imprimir_separador()
    print("\n1. Creando tierra con plantacion...")
    
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    
    plantacion = terreno.get_finca()
    print(f"[OK] Plantacion creada: {plantacion.get_nombre()}")
    print(f"     Superficie: {plantacion.get_superficie_disponible()}m2")
    print(f"     Agua inicial: {plantacion.get_agua_disponible()}L")
    
    # ========================================================================
    # PATRON FACTORY: Creacion de cultivos
    # ========================================================================
    imprimir_separador("PATRON FACTORY: Plantando cultivos")
    
    plantacion_service = PlantacionService()
    
    print("\nPlantando cultivos usando Factory Method...")
    plantacion_service.plantar(plantacion, "Pino", 5)
    plantacion_service.plantar(plantacion, "Olivo", 3)
    plantacion_service.plantar(plantacion, "Lechuga", 10)
    plantacion_service.plantar(plantacion, "Zanahoria", 15)
    
    print(f"\n[OK] Total de cultivos plantados: {len(plantacion.get_cultivos())}")
    
    # ========================================================================
    # Mostrar datos de cultivos
    # ========================================================================
    imprimir_separador()
    print("\n2. Mostrando datos de algunos cultivos...")
    
    cultivos = plantacion.get_cultivos()
    for i, cultivo in enumerate(cultivos[:3], 1):
        print(f"\nCultivo {i}:")
        registry1.mostrar_datos(cultivo)
    
    # ========================================================================
    # PATRON STRATEGY: Riego con diferentes estrategias
    # ========================================================================
    imprimir_separador("PATRON STRATEGY: Riego de cultivos")
    
    print("\nRegando plantacion (Strategy Pattern)...")
    print("  - Arboles usan AbsorcionSeasonalStrategy")
    print("  - Hortalizas usan AbsorcionConstanteStrategy")
    
    try:
        plantacion_service.regar(plantacion)
    except Exception as e:
        print(f"[!] Error: {e}")
    
    # ========================================================================
    # Gestion de personal
    # ========================================================================
    imprimir_separador()
    print("\n3. Gestionando personal...")
    
    trabajador = Trabajador(
        dni=12345678,
        nombre="Juan Perez",
        tareas=[]
    )
    
    apto_medico = AptoMedico(
        fecha_emision=date.today(),
        observaciones="Apto para tareas agricolas"
    )
    trabajador.set_apto_medico(apto_medico)
    
    tarea1 = Tarea(1, "Cosechar zanahorias", date.today())
    tarea2 = Tarea(2, "Cosechar lechugas", date.today())
    trabajador.agregar_tarea(tarea1)
    trabajador.agregar_tarea(tarea2)
    
    plantacion.agregar_trabajador(trabajador)
    
    herramienta = Herramienta(1, "Pala", True)

    
    trabajador_service = TrabajadorService()
    print(f"\nTrabajador: {trabajador.get_nombre()}")
    trabajador_service.trabajar(trabajador, date.today(), herramienta)
    
    # ========================================================================
    # PATRON OBSERVER: Sistema de riego automatizado
    # ========================================================================
    imprimir_separador("PATRON OBSERVER: Sistema de riego automatizado")
    
    print("\nIniciando sensores y control automatico...")
    print("(Observable Pattern con threads daemon)")
    
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    
    tarea_control = ControlRiegoTask(
        tarea_temp,
        tarea_hum,
        plantacion,
        plantacion_service
    )
    
    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()
    
    print("\n[OK] Sistema de riego funcionando...")
    print("     Dejando funcionar por 10 segundos...")
    
    time.sleep(10)
    
    print("\nDeteniendo sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()
    
    time.sleep(1)
    print("[OK] Sistema de riego detenido correctamente")
    
    # ========================================================================
    # Cosecha y empaquetado
    # ========================================================================
    imprimir_separador()
    print("\n4. Cosechando cultivos...")
    
    plantacion_service.cosechar(plantacion)
    
    print("\nEmpaquetando en Paquete generico (Generic[T])...")
    paquete = Paquete[Cultivo]("Cultivos Cosechados")
    
    for cultivo in cultivos[:5]:
        paquete.agregar(cultivo)
    
    print(f"[OK] Paquete creado con {paquete.cantidad()} cultivos")
    
    # ========================================================================
    # Fumigacion
    # ========================================================================
    imprimir_separador()
    print("\n5. Fumigando plantacion...")
    
    plantacion_service.fumigar(plantacion, "Insecticida organico")
    
    # ========================================================================
    # Persistencia de registro forestal
    # ========================================================================
    imprimir_separador("Persistencia de datos")
    
    print("\nCreando registro forestal...")
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    
    registro_service = RegistroForestalService()
    
    print("Guardando registro en disco (pickle)...")
    try:
        registro_service.persistir(registro)
        print("[OK] Registro guardado exitosamente")
    except Exception as e:
        print(f"[!] Error al guardar: {e}")
    
    print("\nRecuperando registro desde disco...")
    try:
        registro_leido = RegistroForestalService.leer_registro("Juan Perez")
        print("[OK] Registro recuperado exitosamente")
        print("\nDatos del registro recuperado:")
        registro_service.mostrar_datos(registro_leido)
    except Exception as e:
        print(f"[!] Error al leer: {e}")
    
    # ========================================================================
    # Resumen final
    # ========================================================================
    imprimir_separador()
    print("\n6. Resumen del sistema:")
    print(f"   - Tierra: {terreno.get_domicilio()}")
    print(f"   - Superficie total: {terreno.get_superficie()}m2")
    print(f"   - Cultivos plantados: {len(plantacion.get_cultivos())}")
    print(f"   - Agua restante: {plantacion.get_agua_disponible()}L")
    print(f"   - Trabajadores: {len(plantacion.get_trabajadores())}")
    print(f"   - Propietario: {registro.get_propietario()}")
    print(f"   - Avaluo: ${registro.get_avaluo():.2f}")
    
    # ========================================================================
    # Finalizacion
    # ========================================================================
    print("\n" + "=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 63
# Generado: 2025-10-21 22:13:25
################################################################################
