"""
Excepcion para errores de persistencia.
"""
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class PersistenciaException(ForestacionException):
    """
    Se lanza cuando ocurre un error en operaciones de persistencia.
    """
    
    def __init__(self, operacion: str, ruta: str, causa: Exception = None):
        """
        Inicializa la excepcion con datos de la operacion fallida.
        
        Args:
            operacion: Tipo de operacion (guardar/leer)
            ruta: Ruta del archivo
            causa: Excepcion original que causo el error
        """
        self._operacion = operacion
        self._ruta = ruta
        self._causa = causa
        
        user_message = (
            f"Error al {operacion} el archivo: {ruta}"
        )
        
        technical_message = (
            f"PersistenciaException: Operacion={operacion}, Ruta={ruta}"
        )
        
        if causa:
            technical_message += f", Causa={type(causa).__name__}: {str(causa)}"
        
        super().__init__(user_message, technical_message)
    
    def get_operacion(self) -> str:
        """
        Obtiene el tipo de operacion.
        
        Returns:
            Nombre de la operacion
        """
        return self._operacion
    
    def get_ruta(self) -> str:
        """
        Obtiene la ruta del archivo.
        
        Returns:
            Ruta del archivo
        """
        return self._ruta
    
    def get_causa(self) -> Exception:
        """
        Obtiene la excepcion original.
        
        Returns:
            Excepcion que causo el error
        """
        return self._causa