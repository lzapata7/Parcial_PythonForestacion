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