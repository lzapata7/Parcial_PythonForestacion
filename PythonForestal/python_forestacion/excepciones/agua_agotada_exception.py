"""
Excepcion para agua agotada en plantacion.
"""
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class AguaAgotadaException(ForestacionException):
    """
    Se lanza cuando no hay suficiente agua para regar cultivos.
    """
    
    def __init__(self, agua_requerida: int, agua_disponible: int):
        """
        Inicializa la excepcion con datos de agua.
        
        Args:
            agua_requerida: Agua necesaria en litros
            agua_disponible: Agua disponible en litros
        """
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible
        
        user_message = (
            f"Agua agotada. Se requieren {agua_requerida} litros pero solo hay "
            f"{agua_disponible} litros disponibles."
        )
        
        technical_message = (
            f"AguaAgotadaException: "
            f"Requerida={agua_requerida}L, "
            f"Disponible={agua_disponible}L, "
            f"Deficit={agua_requerida - agua_disponible}L"
        )
        
        super().__init__(user_message, technical_message)
    
    def get_agua_requerida(self) -> int:
        """
        Obtiene el agua requerida.
        
        Returns:
            Agua requerida en litros
        """
        return self._agua_requerida
    
    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.
        
        Returns:
            Agua disponible en litros
        """
        return self._agua_disponible