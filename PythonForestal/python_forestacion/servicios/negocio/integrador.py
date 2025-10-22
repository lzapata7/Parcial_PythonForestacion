"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/servicios/negocio
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/negocio/__init__.py
# ================================================================================

"""
Paquete de servicios de negocio de alto nivel.
"""
from python_forestacion.servicios.negocio.paquete import Paquete

__all__ = ['Paquete']

# ================================================================================
# ARCHIVO 2/2: paquete.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

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

