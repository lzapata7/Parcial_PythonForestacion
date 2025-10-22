"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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

