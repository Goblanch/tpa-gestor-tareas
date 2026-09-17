class Tarea:

    PRIORIDADES_VALIDAS = ("urgente", "alta", "media/alta", "media", "baja")
    ESTADOS_VALIDOS = ("pendiente", "en curso", "finalizada")

    def __init__(self, titulo: str, descripcion : str, prioridad : int, estado : str, dias_restantes: int):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado
        self.dias_restantes = dias_restantes

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("[ERROR] El título no puede estar vacío.")
        self._titulo = valor

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        self._descripcion = valor

    @property
    def prioridad(self):
        return self._prioridad

    @prioridad.setter
    def prioridad(self, valor: int) -> None:
        if valor < 1 or valor > 5:
            raise ValueError("[ERROR] La prioridad debe estár entre 1 y 5.")
        self._prioridad = valor

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str) -> None:
        if valor not in Tarea.ESTADOS_VALIDOS:
            raise ValueError(f"[ERROR] Estado no válido: {valor}")
        self._estado = valor

    @property
    def dias_restantes(self) -> int:
        return self._dias_restantes

    @dias_restantes.setter
    def dias_restantes(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("[ERROR] Los días no pueden ser negativos.")
        self._dias_restantes = valor

    @property
    def clasificacion_dias(self):
        """Propiedad calculada a partir de días restantes (Urgente, Próxima o Sin prisa)"""
        return Tarea._clasificar_por_dias(self._dias_restantes)

    @property
    def clasificacion_prioridad(self):
        return Tarea.PRIORIDADES_VALIDAS[self.prioridad - 1]


    @staticmethod
    def _clasificar_por_dias(dias: int) -> str:
        if dias <= 2:
            return "Urgente"
        elif dias <= 7:
            return "Próxima"
        else:
            return "Sin prisa"