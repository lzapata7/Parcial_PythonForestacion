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