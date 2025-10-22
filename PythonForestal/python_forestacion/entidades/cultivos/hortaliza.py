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