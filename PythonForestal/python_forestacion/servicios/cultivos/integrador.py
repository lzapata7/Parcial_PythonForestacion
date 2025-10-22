"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================

"""
Paquete de servicios de cultivos.
"""
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

__all__ = ['CultivoServiceRegistry']

# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

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

