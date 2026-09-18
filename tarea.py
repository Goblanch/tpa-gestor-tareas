from datetime import datetime

class Tarea:

    PRIORIDADES_VALIDAS = ("urgente", "alta", "media/alta", "media", "baja")
    ESTADOS_VALIDOS = ("pendiente", "en curso", "finalizada")

    def __init__(self, titulo: str, descripcion : str, prioridad : int, estado : str, dias_restantes: int, tag: str = ""):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
        self.dias_restantes = dias_restantes
        self.tag = tag

        self._ultima_modificacion = datetime.now()

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("[ERROR] El título no puede estar vacío.")
        self._titulo = valor
        self._marcar_modificada()

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        self._descripcion = valor
        self._marcar_modificada()

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, valor: int) -> None:
        if valor < 1 or valor > 5:
            raise ValueError("[ERROR] La prioridad debe estár entre 1 y 5.")
        self._prioridad = valor
        self._marcar_modificada()

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str) -> None:
        if valor not in Tarea.ESTADOS_VALIDOS:
            raise ValueError(f"[ERROR] Estado no válido: {valor}")
        self._estado = valor
        self._marcar_modificada()

    @property
    def dias_restantes(self) -> int:
        return self._dias_restantes

    @dias_restantes.setter
    def dias_restantes(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("[ERROR] Los días no pueden ser negativos.")
        self._dias_restantes = valor
        self._marcar_modificada()

    @property
    def tag(self) -> str:
        return self._tag

    tag.setter
    def tag(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise ValueError(f"[ERROR] El tag deve ser una cadena de texto: {valor}")
        self._tag = valor.strip()
        self._marcar_modificada()

    @property
    def clasificacion_dias(self):
        """Propiedad calculada a partir de días restantes (Urgente, Próxima o Sin prisa)"""
        return Tarea._clasificar_por_dias(self._dias_restantes)

    @property
    def clasificacion_prioridad(self):
        return Tarea.PRIORIDADES_VALIDAS[self.prioridad - 1]

    @property
    def ultima_modificacion(self):
        return self._ultima_modificacion

    def esta_finalizada(self) -> bool:
        return self._estado == "finalizada"

    def completar(self) -> None:
        if self.esta_finalizada():
            raise ValueError("[ERROR] La tarea ya está finalizada")

        self._estado = "finalizada"

    def _marcar_modificada(self):
        self._ultima_modificacion = datetime.now()

    @staticmethod
    def _clasificar_por_dias(dias: int) -> str:
        if dias <= 2:
            return "Urgente"
        elif dias <= 7:
            return "Próxima"
        else:
            return "Sin prisa"

    @classmethod
    def desde_dict(cls, datos: dict) -> "Tarea":
        return cls(
            titulo=datos["titulo"],
            descripcion=datos["descripcion"],
            prioridad=datos["prioridad"],
            estado=datos["estado"],
            dias_restantes=datos["dias_restantes"],
            tag=datos.get("tag", ""),
        )

    def __str__(self):
        fecha = self._ultima_modificacion.strftime("%d/%m/%Y %H:%M:%S")
        etiqueta = f" #{self.tag}" if self.tag else ""
        return (f"[{self.clasificacion_dias}] {self.titulo}{etiqueta} "
                f"(prioridad: {self.clasificacion_prioridad}, estado: {self.estado}, "
                f"faltan {self.dias_restantes} días, "
                f"modificada: {fecha})")