"""
Excepcion base del sistema de gestion forestal.
"""


class ForestacionException(Exception):
    """
    Excepcion base para todas las excepciones del sistema forestal.
    
    Proporciona mensajes separados para usuario y tecnico.
    """
    
    def __init__(self, user_message: str, technical_message: str = None):
        """
        Inicializa la excepcion con mensajes personalizados.
        
        Args:
            user_message: Mensaje amigable para el usuario final
            technical_message: Mensaje tecnico con detalles del error
        """
        self._user_message = user_message
        self._technical_message = technical_message or user_message
        super().__init__(self._user_message)
    
    def get_user_message(self) -> str:
        """
        Obtiene el mensaje para el usuario.
        
        Returns:
            Mensaje amigable para el usuario
        """
        return self._user_message
    
    def get_technical_message(self) -> str:
        """
        Obtiene el mensaje tecnico.
        
        Returns:
            Mensaje con detalles tecnicos
        """
        return self._technical_message
    
    def get_full_message(self) -> str:
        """
        Obtiene ambos mensajes concatenados.
        
        Returns:
            Mensaje completo con informacion de usuario y tecnica
        """
        if self._user_message == self._technical_message:
            return self._user_message
        return f"{self._user_message}\n[Tecnico]: {self._technical_message}"