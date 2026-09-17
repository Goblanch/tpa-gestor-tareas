import copy
from tarea import Tarea

class GestorTareas:
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, tarea: Tarea) -> None:
        if not isinstance(tarea, Tarea):
            raise TypeError("[ERROR] Solo se pueden agregar objetos de tipo tarea.")

        if self.buscar_por_nombre(tarea.titulo) is not None:
            raise ValueError(f"[WRN] Ya existe la tarea {tarea.titulo}. No se añade.")

        self._tareas.append(tarea)

    def eliminar_tarea(self, titulo: str) -> Tarea:
        tarea = self.buscar_por_nombre(titulo)
        if tarea is None:
            raise ValueError(f"[ERROR] No existe ninguna tarea con el título {titulo}")

        self._tareas.remove(tarea)
        return tarea

    def buscar_por_nombre(self, titulo: str) -> Tarea:
        for tarea in self._tareas:
            if tarea.titulo == titulo:
                return tarea

        return None

    def a_dict(self):
        return {tarea.titulo: tarea for tarea in self._tareas}

    def mostrar_tarea(self, titulo: str) -> None:
        tarea = self.buscar_por_nombre(titulo)
        if tarea is None:
            print(f"[WRN] No se encontró ninguna tarea con el título {titulo}")
            return

        print(tarea)

    def mostrar_lista_tareas(self):
        if not self._tareas:
            print("[WRN] No hay tareas registradas")
            return

        for tarea in self._tareas:
            print(tarea)

    def copiar_tarea_superficial(self, titulo: str) -> Tarea:
        tarea = self.buscar_por_nombre(titulo)
        if tarea is None:
            raise ValueError(f"[ERROR] No existe ninguna tarea con el título: {titulo}")
        return copy.copy(tarea)

    def copiar_tarea_profunda(self, titulo: str) -> Tarea:
        tarea = self.buscar_por_nombre(titulo)
        if tarea is None:
            raise ValueError(f"[ERROR] No existe ninguna tarea con el título: {titulo}")
        return copy.deepcopy(tarea)

    def __len__(self):
        return len(self._tareas)