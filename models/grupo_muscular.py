class GrupoMuscular:
    """Representa un modelo de grupo muscular."""

    def __init__(self, nombre: str):
        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("'nombre' debe ser una cadena no vacia")
        self.__nombre = nombre.strip()