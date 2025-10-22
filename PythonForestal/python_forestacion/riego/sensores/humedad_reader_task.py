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