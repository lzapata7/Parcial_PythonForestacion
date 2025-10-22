"""
Factory Method para creacion de cultivos.
"""
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """
    Factory para crear cultivos sin conocer clases concretas.
    """
    
    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        """
        Crea un cultivo segun la especie especificada.
        
        Args:
            especie: Tipo de cultivo (Pino, Olivo, Lechuga, Zanahoria)
            
        Returns:
            Cultivo creado
            
        Raises:
            ValueError: Si la especie es desconocida
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }
        
        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")
        
        return factories[especie]()
    
    @staticmethod
    def _crear_pino() -> Cultivo:
        """
        Crea un Pino con valores por defecto.
        
        Returns:
            Instancia de Pino
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")
    
    @staticmethod
    def _crear_olivo() -> Cultivo:
        """
        Crea un Olivo con valores por defecto.
        
        Returns:
            Instancia de Olivo
        """
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)
    
    @staticmethod
    def _crear_lechuga() -> Cultivo:
        """
        Crea una Lechuga con valores por defecto.
        
        Returns:
            Instancia de Lechuga
        """
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Criolla")
    
    @staticmethod
    def _crear_zanahoria() -> Cultivo:
        """
        Crea una Zanahoria con valores por defecto.
        
        Returns:
            Instancia de Zanahoria
        """
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(es_baby=False)