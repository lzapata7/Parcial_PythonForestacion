"""
Excepcion para superficie insuficiente en plantacion.
"""
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class SuperficieInsuficienteException(ForestacionException):
    """
    Se lanza cuando no hay suficiente superficie para plantar cultivos.
    """
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa la excepcion con datos de superficie.
        
        Args:
            superficie_requerida: Superficie necesaria en m2
            superficie_disponible: Superficie disponible en m2
        """
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
        
        user_message = (
            f"No hay suficiente superficie disponible. "
            f"Se requieren {superficie_requerida:.2f} m2 pero solo hay "
            f"{superficie_disponible:.2f} m2 disponibles."
        )
        
        technical_message = (
            f"SuperficieInsuficienteException: "
            f"Requerida={superficie_requerida}, "
            f"Disponible={superficie_disponible}, "
            f"Deficit={superficie_requerida - superficie_disponible}"
        )
        
        super().__init__(user_message, technical_message)
    
    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie requerida.
        
        Returns:
            Superficie requerida en m2
        """
        return self._superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie disponible.
        
        Returns:
            Superficie disponible en m2
        """
        return self._superficie_disponible