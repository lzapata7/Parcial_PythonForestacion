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