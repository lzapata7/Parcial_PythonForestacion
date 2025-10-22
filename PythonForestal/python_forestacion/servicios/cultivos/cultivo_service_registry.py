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