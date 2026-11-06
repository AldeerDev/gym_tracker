class Ejercicio:

    def __init__(
        self,
        nombre: str,
        descripcion: str = None,
        grupo_muscular_id: int = None,
        id: int = None
    ):
        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter()
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Cadena vacia.")
        self.__nombre = nombre.strip()

    @property
    def descripcion(self) -> str | None:
        return self.__descripcion
    