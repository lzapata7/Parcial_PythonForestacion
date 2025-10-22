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