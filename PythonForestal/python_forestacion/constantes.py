"""
Constantes centralizadas del sistema de gestion forestal.
Todas las constantes magicas del proyecto se definen aqui.
"""

# ============================================================================
# CONSTANTES DE AGUA
# ============================================================================
AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# ============================================================================
# CONSTANTES DE RIEGO
# ============================================================================
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50

# ============================================================================
# CONSTANTES DE CULTIVOS - PINO
# ============================================================================
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
CRECIMIENTO_PINO = 0.10

# ============================================================================
# CONSTANTES DE CULTIVOS - OLIVO
# ============================================================================
SUPERFICIE_OLIVO = 1.5
AGUA_INICIAL_OLIVO = 2
CRECIMIENTO_OLIVO = 0.01

# ============================================================================
# CONSTANTES DE CULTIVOS - LECHUGA
# ============================================================================
SUPERFICIE_LECHUGA = 0.5
AGUA_INICIAL_LECHUGA = 1

# ============================================================================
# CONSTANTES DE CULTIVOS - ZANAHORIA
# ============================================================================
SUPERFICIE_ZANAHORIA = 0.3
AGUA_INICIAL_ZANAHORIA = 2

# ============================================================================
# CONSTANTES DE ABSORCION DE AGUA
# ============================================================================
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
MES_INICIO_VERANO = 12
MES_FIN_VERANO = 3

# ============================================================================
# CONSTANTES DE SENSORES
# ============================================================================
INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0
INTERVALO_CONTROL_RIEGO = 2.5

TEMP_MIN_SENSOR = -25
TEMP_MAX_SENSOR = 50
HUMEDAD_MIN_SENSOR = 0
HUMEDAD_MAX_SENSOR = 100

# ============================================================================
# CONSTANTES DE PERSISTENCIA
# ============================================================================
DIRECTORIO_DATOS = "data"
EXTENSION_ARCHIVO = ".dat"

# ============================================================================
# CONSTANTES DE SISTEMA
# ============================================================================
TIMEOUT_THREAD = 1.0