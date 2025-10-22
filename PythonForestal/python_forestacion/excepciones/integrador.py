"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/excepciones
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

"""
Mensajes centralizados para excepciones del sistema.
"""


class MensajesException:
    """
    Clase con mensajes de error centralizados.
    """
    
    # Mensajes de superficie
    SUPERFICIE_INSUFICIENTE = "No hay suficiente superficie disponible para plantar"
    
    # Mensajes de agua
    AGUA_AGOTADA = "El agua disponible se ha agotado"
    AGUA_INSUFICIENTE = "No hay suficiente agua para realizar el riego"
    
    # Mensajes de persistencia
    ERROR_GUARDAR = "Error al guardar el archivo"
    ERROR_LEER = "Error al leer el archivo"
    ARCHIVO_NO_EXISTE = "El archivo no existe"
    
    # Mensajes de validacion
    VALOR_NEGATIVO = "El valor no puede ser negativo"
    VALOR_INVALIDO = "El valor proporcionado no es valido"

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

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

