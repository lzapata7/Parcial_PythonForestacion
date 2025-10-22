"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

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

