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