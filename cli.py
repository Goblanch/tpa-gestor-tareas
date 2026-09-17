from tarea import Tarea
from gestor_tareas import GestorTareas

class GestorTareasCLI:
    def __init__(self):
        pass

    @staticmethod
    def mostrar_menu() -> None:
        print("\n" + "=" * 50)
        print("     # GESTOR DE TAREAS #")
        print("=" * 50)
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Buscar tarea (lista)")
        print("4. Buscar tarea (dict)")
        print("5. Mostrar tarea")
        print("6. Mostrar lista de tareas")
        print("7. Marcar tarea como completada")
        print("8. Copiar tarea (superficial)")
        print("9. Copiar tarea (profunda)")
        print("0. Salir")
        print("-" * 50)

    @staticmethod
    def pedir_entero(mensaje: str) -> int:
        """Pide un entero hasta que el usuario introduzca uno válido"""
        while True:
            valor = input(mensaje)
            try:
                return int(valor)
            except ValueError:
                print("    -> [ERROR] Introduce un número válido")

    @staticmethod
    def opcion_agregar(gestor: GestorTareas) -> None:
        print("\n-- Añadir nueva tarea --")
        titulo = str(input("Título: "))
        descripcion = str(input("Descripción: "))

        print("Prioridades válidas de mayor a menor: 1 / 2 / 3 / 4 / 5")
        prioridad = GestorTareasCLI.pedir_entero("Prioridad: ")

        print(f"Estados válidos: {Tarea.ESTADOS_VALIDOS}")
        estado = str(input("Estado: "))

        dias = GestorTareasCLI.pedir_entero("Días restantes: ")
        tag = str(input("Tag (opcional, Enter para omitir): "))

        try:
            tarea = Tarea(titulo, descripcion, prioridad, estado, dias, tag)
            gestor.agregar_tarea(tarea)
            print(f"    -> [SUCCESS] Tarea '{titulo}' añadida correctamente")
        except (ValueError, TypeError) as e:
            print(f"    -> [ERROR] Error al crear la tarea: {e}")

    @staticmethod
    def opcion_eliminar(gestor: GestorTareas) -> None:
        titulo = str(input("\nTítulo de la tarea a eliminar: "))
        try:
            gestor.eliminar_tarea(titulo)
            print(f"    -> [SUCCESS] Tarea '{titulo}' eliminada")
        except ValueError as e:
            print(f"    -> [ERROR] No se puedo eliminar la tarea: {e}")

    @staticmethod
    def opcion_buscar_lista(gestor: GestorTareas) -> None:
        titulo = str(input("\nTítulo a buscar: "))
        tarea = gestor.buscar_por_nombre(titulo)
        print(tarea if tarea else "    -> No encontrada")

    @staticmethod
    def opcion_buscar_dict(gestor: GestorTareas) -> None:
        titulo = str(input("\nTítulo a buscar: "))
        tareas_dict = gestor.a_dict()
        tarea = tareas_dict.get(titulo)
        print(tarea if tarea else "    -> No encontrada")

    @staticmethod
    def opcion_mostrar_tarea(gestor: GestorTareas) -> None:
        titulo = str(input("\nTítulo de la tarea a mostrar: "))
        gestor.mostrar_tarea(titulo)

    @staticmethod
    def opcion_mostrar_lista_tareas(gestor: GestorTareas) -> None:
        print(f"\n-- Lista de tareas ({len(gestor)}) --")
        gestor.mostrar_lista_tareas()

    @staticmethod
    def opcion_completar(gestor: GestorTareas) -> None:
        titulo = str(input("\nTítulo de la tarea a completar: "))
        tarea = gestor.buscar_por_nombre(titulo)
        if tarea is None:
            print("    -> [ERROR] Tarea no encontrada")
            return

        try:
            tarea.completar()
            print(f"    -> [SUCCESS] Tarea '{titulo}' marcada como completada")
        except ValueError as e:
            print(f"    -> [ERROR] No se pudo completar la tarea: {e}")

    @staticmethod
    def opcion_copiar(gestor: GestorTareas, profunda: bool) -> None:
        titulo = str(input("\nTítulo de la tarea a copiar: "))
        try:
            if profunda:
                copia = gestor.copiar_tarea_profunda(titulo)
            else:
                copia = gestor.copiar_tarea_superficial(titulo)
        except ValueError as e:
            print(f"    -> [ERROR] No se puedo copiar: {e}")
            return

        nuevo_titulo = input(f"Título para la copia (Enter = '{titulo} (copia)'): ")
        copia.titulo = nuevo_titulo if nuevo_titulo.strip() else f"{titulo} (copia)"

        gestor.agregar_tarea(copia)
        print(f"    -> [SUCCESS] Copia {'profunda' if profunda else 'superficual'} añadida como '{copia.titulo}'")

    @staticmethod
    def mainloop():
        gestor = GestorTareas()
        acciones = {
            "1": GestorTareasCLI.opcion_agregar,
            "2": GestorTareasCLI.opcion_eliminar,
            "3": GestorTareasCLI.opcion_buscar_lista,
            "4": GestorTareasCLI.opcion_buscar_dict,
            "5": GestorTareasCLI.opcion_mostrar_tarea,
            "6": GestorTareasCLI.opcion_mostrar_lista_tareas,
            "7": GestorTareasCLI.opcion_completar,
        }

        while True:
            GestorTareasCLI.mostrar_menu()
            opcion = input("Elige una opción: ").strip()

            if opcion == "0":
                print("Saliendo...")
                break
            elif opcion in acciones:
                acciones[opcion](gestor)
            elif opcion == "8":
                GestorTareasCLI.opcion_copiar(gestor, profunda=False)
            elif opcion == "9":
                GestorTareasCLI.opcion_copiar(gestor, profunda=True)
            else:
                print("    -> [ERROR] Opción no válida, prueba de nuevo")

            input("\nPulsa Enter para continuar...")

        