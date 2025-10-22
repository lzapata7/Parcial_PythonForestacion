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