"""
Archivo integrador generado automaticamente
Directorio: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos
Fecha: 2025-10-21 22:13:25
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================

"""
Paquete de servicios de terrenos.
"""
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService

__all__ = [
    'TierraService',
    'PlantacionService',
    'RegistroForestalService'
]

# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

"""
Servicio para gestion de plantaciones.
"""
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException


class PlantacionService:
    """
    Servicio para operaciones sobre plantaciones.
    """
    
    def __init__(self):
        """
        Inicializa el servicio con el registry de cultivos.
        """
        self._registry = CultivoServiceRegistry.get_instance()
    
    def plantar(self, plantacion: Plantacion, especie: str, cantidad: int) -> None:
        """
        Planta cultivos en la plantacion usando Factory.
        
        Args:
            plantacion: Plantacion donde plantar
            especie: Tipo de cultivo
            cantidad: Cantidad a plantar
            
        Raises:
            SuperficieInsuficienteException: Si no hay superficie suficiente
        """
        cultivo_ejemplo = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_ejemplo.get_superficie() * cantidad
        superficie_disponible = plantacion.get_superficie_disponible()
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                superficie_disponible
            )
        
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)
        
        plantacion.set_superficie_disponible(
            superficie_disponible - superficie_requerida
        )
        
        print(f"Se plantaron {cantidad} {especie}(s)")
    
    def regar(self, plantacion: Plantacion) -> None:
        """
        Riega todos los cultivos de la plantacion.
        
        Args:
            plantacion: Plantacion a regar
            
        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        cultivos = plantacion.get_cultivos()
        agua_disponible = plantacion.get_agua_disponible()
        
        agua_total_necesaria = 0
        for cultivo in cultivos:
            agua_total_necesaria += self._calcular_agua_necesaria(cultivo)
        
        if agua_total_necesaria > agua_disponible:
            raise AguaAgotadaException(agua_total_necesaria, agua_disponible)
        
        for cultivo in cultivos:
            cantidad_absorbida = self._registry.absorber_agua(cultivo)
            agua_disponible -= cantidad_absorbida
        
        plantacion.set_agua_disponible(agua_disponible)
        print(f"Riego completado. Agua restante: {agua_disponible}L")
    
    def _calcular_agua_necesaria(self, cultivo: Cultivo) -> int:
        """
        Calcula agua necesaria para un cultivo.
        
        Args:
            cultivo: Cultivo a calcular
            
        Returns:
            Agua necesaria en litros
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        from python_forestacion.constantes import (
            ABSORCION_SEASONAL_VERANO,
            ABSORCION_SEASONAL_INVIERNO
        )
        from datetime import date
        
        if isinstance(cultivo, (Pino, Olivo)):
            mes = date.today().month
            if 12 <= mes or mes <= 3:
                return ABSORCION_SEASONAL_VERANO
            else:
                return ABSORCION_SEASONAL_INVIERNO
        elif isinstance(cultivo, Lechuga):
            return 1
        elif isinstance(cultivo, Zanahoria):
            return 2
        else:
            return 1
    
    def cosechar(self, plantacion: Plantacion) -> None:
        """
        Cosecha todos los cultivos.
        
        Args:
            plantacion: Plantacion a cosechar
        """
        cultivos = plantacion.get_cultivos()
        print(f"Cosechando {len(cultivos)} cultivo(s)...")
        
        for cultivo in cultivos:
            tipo = type(cultivo).__name__
            print(f"- Cosechado: {tipo}")
    
    def fumigar(self, plantacion: Plantacion, plaguicida: str) -> None:
        """
        Fumiga la plantacion con plaguicida.
        
        Args:
            plantacion: Plantacion a fumigar
            plaguicida: Tipo de plaguicida
        """
        cultivos = plantacion.get_cultivos()
        print(f"Fumigando {len(cultivos)} cultivo(s) con {plaguicida}")
    
    def mostrar_datos(self, plantacion: Plantacion) -> None:
        """
        Muestra datos de la plantacion.
        
        Args:
            plantacion: Plantacion a mostrar
        """
        print(f"Nombre: {plantacion.get_nombre()}")
        print(f"Superficie disponible: {plantacion.get_superficie_disponible()}m2")
        print(f"Agua disponible: {plantacion.get_agua_disponible()}L")
        print(f"Cultivos: {len(plantacion.get_cultivos())}")
        print(f"Trabajadores: {len(plantacion.get_trabajadores())}")

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

"""
Servicio para gestion de registros forestales.
"""
import os
import pickle
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATOS, EXTENSION_ARCHIVO


class RegistroForestalService:
    """
    Servicio para operaciones sobre registros forestales.
    Incluye persistencia con pickle.
    """
    
    def persistir(self, registro: RegistroForestal) -> None:
        """
        Persiste un registro en disco.
        
        Args:
            registro: Registro a persistir
            
        Raises:
            PersistenciaException: Si ocurre error al guardar
        """
        if not os.path.exists(DIRECTORIO_DATOS):
            os.makedirs(DIRECTORIO_DATOS)
        
        nombre_archivo = f"{registro.get_propietario()}{EXTENSION_ARCHIVO}"
        ruta_completa = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
        
        try:
            with open(ruta_completa, 'wb') as archivo:
                pickle.dump(registro, archivo)
            print(f"Registro guardado: {ruta_completa}")
        except Exception as e:
            raise PersistenciaException("guardar", ruta_completa, e)
    
    @staticmethod
    def leer_registro(propietario: str) -> RegistroForestal:
        """
        Lee un registro desde disco.
        
        Args:
            propietario: Nombre del propietario
            
        Returns:
            Registro leido
            
        Raises:
            PersistenciaException: Si ocurre error al leer
        """
        nombre_archivo = f"{propietario}{EXTENSION_ARCHIVO}"
        ruta_completa = os.path.join(DIRECTORIO_DATOS, nombre_archivo)
        
        try:
            with open(ruta_completa, 'rb') as archivo:
                registro = pickle.load(archivo)
            print(f"Registro leido: {ruta_completa}")
            return registro
        except FileNotFoundError as e:
            raise PersistenciaException("leer", ruta_completa, e)
        except Exception as e:
            raise PersistenciaException("leer", ruta_completa, e)
    
    def mostrar_datos(self, registro: RegistroForestal) -> None:
        """
        Muestra datos del registro.
        
        Args:
            registro: Registro a mostrar
        """
        print(f"ID Padron: {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo: ${registro.get_avaluo():.2f}")
        
        tierra = registro.get_tierra()
        if tierra:
            print(f"Superficie: {tierra.get_superficie()}m2")
            print(f"Domicilio: {tierra.get_domicilio()}")
        
        plantacion = registro.get_plantacion()
        if plantacion:
            print(f"Plantacion: {plantacion.get_nombre()}")
            print(f"Cultivos: {len(plantacion.get_cultivos())}")

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/lzapata/PythonForestal/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

"""
Servicio para gestion de tierras.
"""
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """
    Servicio para operaciones sobre tierras.
    """
    
    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una tierra con su plantacion asociada.
        
        Args:
            id_padron_catastral: ID del padron
            superficie: Superficie en m2
            domicilio: Ubicacion
            nombre_plantacion: Nombre de la plantacion
            
        Returns:
            Tierra creada con plantacion
        """
        tierra = Tierra(id_padron_catastral, superficie, domicilio)
        
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie_disponible=superficie,
            agua_disponible=AGUA_INICIAL_PLANTACION
        )
        
        tierra.set_finca(plantacion)
        
        return tierra
    
    def mostrar_datos(self, tierra: Tierra) -> None:
        """
        Muestra datos de la tierra.
        
        Args:
            tierra: Tierra a mostrar
        """
        print(f"Padron catastral: {tierra.get_id_padron_catastral()}")
        print(f"Superficie: {tierra.get_superficie()}m2")
        print(f"Domicilio: {tierra.get_domicilio()}")
        
        finca = tierra.get_finca()
        if finca:
            print(f"Plantacion: {finca.get_nombre()}")

