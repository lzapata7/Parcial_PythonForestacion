"""
Entidad Herramienta - herramienta de trabajo.
"""


class Herramienta:
    """
    Representa una herramienta de trabajo con certificacion.
    """
    
    def __init__(self, id_herramienta: int, nombre: str, certificacion_hs: bool):
        """
        Inicializa una Herramienta.
        
        Args:
            id_herramienta: ID unico de la herramienta
            nombre: Nombre de la herramienta
            certificacion_hs: Si tiene certificacion de higiene y seguridad
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificacion_hs = certificacion_hs
    
    def get_id_herramienta(self) -> int:
        """
        Obtiene el ID de la herramienta.
        
        Returns:
            ID de la herramienta
        """
        return self._id_herramienta
    
    def set_id_herramienta(self, id_herramienta: int) -> None:
        """
        Establece el ID de la herramienta.
        
        Args:
            id_herramienta: ID de la herramienta
        """
        self._id_herramienta = id_herramienta
    
    def get_nombre(self) -> str:
        """
        Obtiene el nombre de la herramienta.
        
        Returns:
            Nombre de la herramienta
        """
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la herramienta.
        
        Args:
            nombre: Nombre de la herramienta
        """
        self._nombre = nombre
    
    def get_certificacion_hs(self) -> bool:
        """
        Indica si tiene certificacion H&S.
        
        Returns:
            True si tiene certificacion
        """
        return self._certificacion_hs
    
    def set_certificacion_hs(self, certificacion: bool) -> None:
        """
        Establece la certificacion H&S.
        
        Args:
            certificacion: True si tiene certificacion
        """
        self._certificacion_hs = certificacion