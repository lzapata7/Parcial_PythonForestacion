"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/patrones/observer
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/patrones/observer/__init__.py
# ================================================================================

"""
Paquete del patron Observer.
"""
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.patrones.observer.observer import Observer

__all__ = ['Observable', 'Observer']

# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/patrones/observer/observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/patrones/observer/observer.py
# ================================================================================

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

