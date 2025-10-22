"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/riego/sensores
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/riego/sensores/__init__.py
# ================================================================================

"""
Paquete de sensores ambientales.
"""
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

__all__ = ['TemperaturaReaderTask', 'HumedadReaderTask']

# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================

"""
Sensor de humedad - Observable pattern.
"""
import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    HUMEDAD_MIN_SENSOR,
    HUMEDAD_MAX_SENSOR
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Thread que lee humedad continuamente y notifica observadores.
    Implementa Observable pattern.
    """
    
    def __init__(self):
        """
        Inicializa el sensor de humedad.
        """
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    
    def run(self) -> None:
        """
        Ejecuta el loop de lectura de humedad.
        """
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)
    
    def _leer_humedad(self) -> float:
        """
        Simula lectura de humedad.
        
        Returns:
            Humedad en porcentaje
        """
        return random.uniform(HUMEDAD_MIN_SENSOR, HUMEDAD_MAX_SENSOR)
    
    def detener(self) -> None:
        """
        Detiene el sensor de forma limpia.
        """
        self._detenido.set()

# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

"""
Sensor de temperatura - Observable pattern.
"""
import threading
import time
import random
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    TEMP_MIN_SENSOR,
    TEMP_MAX_SENSOR
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Thread que lee temperatura continuamente y notifica observadores.
    Implementa Observable pattern.
    """
    
    def __init__(self):
        """
        Inicializa el sensor de temperatura.
        """
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    
    def run(self) -> None:
        """
        Ejecuta el loop de lectura de temperatura.
        """
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)
    
    def _leer_temperatura(self) -> float:
        """
        Simula lectura de temperatura.
        
        Returns:
            Temperatura en grados Celsius
        """
        return random.uniform(TEMP_MIN_SENSOR, TEMP_MAX_SENSOR)
    
    def detener(self) -> None:
        """
        Detiene el sensor de forma limpia.
        """
        self._detenido.set()

