from datetime import datetime
from tarea import Tarea
from gestor_tareas import GestorTareas

class GestorArchivo:
    SEPARADOR = '|'

    @staticmethod
    def guardar_tareas(gestor: GestorTareas, ruta: str) -> None:
        with open(ruta, "w", encoding="utf-8") as archivo:
            for tarea in gestor._tareas:
                linea = GestorArchivo.SEPARADOR.join([
                    tarea.titulo,
                    tarea.descripcion,
                    tarea.prioridad,
                    tarea.estado,
                    str(tarea.dias_restantes),
                    tarea.tag,
                    tarea.ultima_modificacion.isoformat()
                ])

                archivo.write(linea + "\n")

    @staticmethod
    def cargar_tareas(ruta: str) -> GestorTareas:
        gestor = GestorTareas()

        with open(ruta, "r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea:
                    continue

                campos = linea.split(GestorArchivo.SEPARADOR)

                if len(campos) != 7:
                    print(f"    -> [WRN] Linea {numero_linea} corrupta, se omite")
                    continue

                titulo, descripcion, prioridad, estado, dias_restantes, tag, ultima_mod = campos

                try:
                    tarea = Tarea(
                        titulo=titulo,
                        descripcion=descripcion,
                        prioridad=prioridad,
                        estado=estado,
                        dias_restantes=dias_restantes,
                        tag=tag,
                    )
                    tarea._ultima_modificacion = datetime.fromisoformat(ultima_mod)
                    gestor.agregar_tarea(tarea)
                except (ValueError, TypeError) as e:
                    print(f"    [ERROR] Línea {numero_linea} inválida. ({e}), se omite.")

        return gestor