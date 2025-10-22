"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/riego/control
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/riego/control/__init__.py
# ================================================================================

"""
Paquete de control de riego.
"""
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

__all__ = ['ControlRiegoTask']

# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/riego/control/control_riego_task.py
# ================================================================================

"""
Controlador de riego automatico - Observer pattern.
"""
import threading
import time
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)


class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Controlador que observa sensores y riega automaticamente.
    Implementa Observer pattern.
    """
    
    def __init__(
        self,
        sensor_temperatura: TemperaturaReaderTask,
        sensor_humedad: HumedadReaderTask,
        plantacion: Plantacion,
        plantacion_service: PlantacionService
    ):
        """
        Inicializa el controlador de riego.
        
        Args:
            sensor_temperatura: Sensor de temperatura
            sensor_humedad: Sensor de humedad
            plantacion: Plantacion a regar
            plantacion_service: Servicio de plantacion
        """
        threading.Thread.__init__(self, daemon=True)
        self._sensor_temperatura = sensor_temperatura
        self._sensor_humedad = sensor_humedad
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        
        self._ultima_temperatura = None
        self._ultima_humedad = None
        
        self._sensor_temperatura.agregar_observador(self)
        self._sensor_humedad.agregar_observador(self)
    
    def actualizar(self, evento: float) -> None:
        """
        Recibe notificaciones de sensores.
        
        Args:
            evento: Valor del sensor (temperatura o humedad)
        """
        pass
    
    def run(self) -> None:
        """
        Loop principal de control de riego.
        """
        while not self._detenido.is_set():
            self._verificar_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)
    
    def _verificar_y_regar(self) -> None:
        """
        Verifica condiciones y riega si es necesario.
        """
        temperatura = self._sensor_temperatura._leer_temperatura()
        humedad = self._sensor_humedad._leer_humedad()
        
        if (TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO and 
            humedad < HUMEDAD_MAX_RIEGO):
            
            try:
                print(f"[RIEGO] Temp: {temperatura:.1f}C, Humedad: {humedad:.1f}%")
                self._plantacion_service.regar(self._plantacion)
            except Exception as e:
                print(f"[!] Error al regar: {e}")
    
    def detener(self) -> None:
        """
        Detiene el controlador de forma limpia.
        """
        self._detenido.set()

