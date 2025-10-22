"""
Servicio para gestion de trabajadores.
"""
from datetime import date
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta


class TrabajadorService:
    """
    Servicio para operaciones sobre trabajadores.
    """
    
    def trabajar(
        self,
        trabajador: Trabajador,
        fecha: date,
        herramienta: Herramienta
    ) -> bool:
        """
        Hace trabajar al trabajador ejecutando sus tareas.
        
        Args:
            trabajador: Trabajador a ejecutar tareas
            fecha: Fecha de trabajo
            herramienta: Herramienta a usar
            
        Returns:
            True si pudo trabajar, False si no tiene apto medico
        """
        if not trabajador.tiene_apto_medico():
            print(f"[!] {trabajador.get_nombre()} no puede trabajar sin apto medico")
            return False
        
        tareas = trabajador.get_tareas()
        tareas_ordenadas = sorted(tareas, key=lambda t: t.get_id_tarea(), reverse=True)
        
        for tarea in tareas_ordenadas:
            if tarea.get_fecha_programada() <= fecha and not tarea.get_completada():
                print(f"Ejecutando tarea {tarea.get_id_tarea()}: {tarea.get_descripcion()}")
                print(f"  Usando herramienta: {herramienta.get_nombre()}")
                tarea.set_completada(True)
        
        return True
    
    def mostrar_datos(self, trabajador: Trabajador) -> None:
        """
        Muestra datos del trabajador.
        
        Args:
            trabajador: Trabajador a mostrar
        """
        print(f"DNI: {trabajador.get_dni()}")
        print(f"Nombre: {trabajador.get_nombre()}")
        print(f"Tareas asignadas: {len(trabajador.get_tareas())}")
        
        apto = trabajador.get_apto_medico()
        if apto:
            print(f"Apto medico: Si (desde {apto.get_fecha_emision()})")
        else:
            print(f"Apto medico: No")