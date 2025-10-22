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