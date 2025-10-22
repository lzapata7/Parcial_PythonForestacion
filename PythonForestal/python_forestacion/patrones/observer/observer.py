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