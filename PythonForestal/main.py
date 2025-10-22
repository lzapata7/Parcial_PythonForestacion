"""
Sistema de Gestion Forestal - Demostracion de Patrones de Diseno.
Punto de entrada principal del sistema.
"""
import time
from datetime import date

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.entidades.cultivos.cultivo import Cultivo


def imprimir_separador(mensaje: str = "", ancho: int = 70) -> None:
    """
    Imprime un separador visual.
    
    Args:
        mensaje: Mensaje a mostrar
        ancho: Ancho del separador
    """
    if mensaje:
        print("\n" + "=" * ancho)
        print(f"  {mensaje}")
        print("=" * ancho)
    else:
        print("-" * ancho)


def main():
    """
    Funcion principal que demuestra todos los patrones del sistema.
    """
    print("\n" + "=" * 70)
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    print("=" * 70)
    
    # ========================================================================
    # PATRON SINGLETON: Registry de servicios
    # ========================================================================
    imprimir_separador("PATRON SINGLETON: Inicializando servicios")
    
    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry.get_instance()
    
    if registry1 is registry2:
        print("[OK] Todos los servicios comparten la misma instancia del Registry")
    else:
        print("[!] ERROR: Instancias diferentes del Registry")
    
    # ========================================================================
    # Creacion de terreno con plantacion
    # ========================================================================
    imprimir_separador()
    print("\n1. Creando tierra con plantacion...")
    
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Agrelo, Mendoza",
        nombre_plantacion="Finca del Madero"
    )
    
    plantacion = terreno.get_finca()
    print(f"[OK] Plantacion creada: {plantacion.get_nombre()}")
    print(f"     Superficie: {plantacion.get_superficie_disponible()}m2")
    print(f"     Agua inicial: {plantacion.get_agua_disponible()}L")
    
    # ========================================================================
    # PATRON FACTORY: Creacion de cultivos
    # ========================================================================
    imprimir_separador("PATRON FACTORY: Plantando cultivos")
    
    plantacion_service = PlantacionService()
    
    print("\nPlantando cultivos usando Factory Method...")
    plantacion_service.plantar(plantacion, "Pino", 5)
    plantacion_service.plantar(plantacion, "Olivo", 3)
    plantacion_service.plantar(plantacion, "Lechuga", 10)
    plantacion_service.plantar(plantacion, "Zanahoria", 15)
    
    print(f"\n[OK] Total de cultivos plantados: {len(plantacion.get_cultivos())}")
    
    # ========================================================================
    # Mostrar datos de cultivos
    # ========================================================================
    imprimir_separador()
    print("\n2. Mostrando datos de algunos cultivos...")
    
    cultivos = plantacion.get_cultivos()
    for i, cultivo in enumerate(cultivos[:3], 1):
        print(f"\nCultivo {i}:")
        registry1.mostrar_datos(cultivo)
    
    # ========================================================================
    # PATRON STRATEGY: Riego con diferentes estrategias
    # ========================================================================
    imprimir_separador("PATRON STRATEGY: Riego de cultivos")
    
    print("\nRegando plantacion (Strategy Pattern)...")
    print("  - Arboles usan AbsorcionSeasonalStrategy")
    print("  - Hortalizas usan AbsorcionConstanteStrategy")
    
    try:
        plantacion_service.regar(plantacion)
    except Exception as e:
        print(f"[!] Error: {e}")
    
    # ========================================================================
    # Gestion de personal
    # ========================================================================
    imprimir_separador()
    print("\n3. Gestionando personal...")
    
    trabajador = Trabajador(
        dni=12345678,
        nombre="Juan Perez",
        tareas=[]
    )
    
    apto_medico = AptoMedico(
        fecha_emision=date.today(),
        observaciones="Apto para tareas agricolas"
    )
    trabajador.set_apto_medico(apto_medico)
    
    tarea1 = Tarea(1, "Cosechar zanahorias", date.today())
    tarea2 = Tarea(2, "Cosechar lechugas", date.today())
    trabajador.agregar_tarea(tarea1)
    trabajador.agregar_tarea(tarea2)
    
    plantacion.agregar_trabajador(trabajador)
    
    herramienta = Herramienta(1, "Pala", True)

    
    trabajador_service = TrabajadorService()
    print(f"\nTrabajador: {trabajador.get_nombre()}")
    trabajador_service.trabajar(trabajador, date.today(), herramienta)
    
    # ========================================================================
    # PATRON OBSERVER: Sistema de riego automatizado
    # ========================================================================
    imprimir_separador("PATRON OBSERVER: Sistema de riego automatizado")
    
    print("\nIniciando sensores y control automatico...")
    print("(Observable Pattern con threads daemon)")
    
    tarea_temp = TemperaturaReaderTask()
    tarea_hum = HumedadReaderTask()
    
    tarea_control = ControlRiegoTask(
        tarea_temp,
        tarea_hum,
        plantacion,
        plantacion_service
    )
    
    tarea_temp.start()
    tarea_hum.start()
    tarea_control.start()
    
    print("\n[OK] Sistema de riego funcionando...")
    print("     Dejando funcionar por 10 segundos...")
    
    time.sleep(10)
    
    print("\nDeteniendo sistema de riego...")
    tarea_temp.detener()
    tarea_hum.detener()
    tarea_control.detener()
    
    time.sleep(1)
    print("[OK] Sistema de riego detenido correctamente")
    
    # ========================================================================
    # Cosecha y empaquetado
    # ========================================================================
    imprimir_separador()
    print("\n4. Cosechando cultivos...")
    
    plantacion_service.cosechar(plantacion)
    
    print("\nEmpaquetando en Paquete generico (Generic[T])...")
    paquete = Paquete[Cultivo]("Cultivos Cosechados")
    
    for cultivo in cultivos[:5]:
        paquete.agregar(cultivo)
    
    print(f"[OK] Paquete creado con {paquete.cantidad()} cultivos")
    
    # ========================================================================
    # Fumigacion
    # ========================================================================
    imprimir_separador()
    print("\n5. Fumigando plantacion...")
    
    plantacion_service.fumigar(plantacion, "Insecticida organico")
    
    # ========================================================================
    # Persistencia de registro forestal
    # ========================================================================
    imprimir_separador("Persistencia de datos")
    
    print("\nCreando registro forestal...")
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Juan Perez",
        avaluo=50309233.55
    )
    
    registro_service = RegistroForestalService()
    
    print("Guardando registro en disco (pickle)...")
    try:
        registro_service.persistir(registro)
        print("[OK] Registro guardado exitosamente")
    except Exception as e:
        print(f"[!] Error al guardar: {e}")
    
    print("\nRecuperando registro desde disco...")
    try:
        registro_leido = RegistroForestalService.leer_registro("Juan Perez")
        print("[OK] Registro recuperado exitosamente")
        print("\nDatos del registro recuperado:")
        registro_service.mostrar_datos(registro_leido)
    except Exception as e:
        print(f"[!] Error al leer: {e}")
    
    # ========================================================================
    # Resumen final
    # ========================================================================
    imprimir_separador()
    print("\n6. Resumen del sistema:")
    print(f"   - Tierra: {terreno.get_domicilio()}")
    print(f"   - Superficie total: {terreno.get_superficie()}m2")
    print(f"   - Cultivos plantados: {len(plantacion.get_cultivos())}")
    print(f"   - Agua restante: {plantacion.get_agua_disponible()}L")
    print(f"   - Trabajadores: {len(plantacion.get_trabajadores())}")
    print(f"   - Propietario: {registro.get_propietario()}")
    print(f"   - Avaluo: ${registro.get_avaluo():.2f}")
    
    # ========================================================================
    # Finalizacion
    # ========================================================================
    print("\n" + "=" * 70)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y eventos")
    print("  [OK] STRATEGY    - Algoritmos de absorcion de agua")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()