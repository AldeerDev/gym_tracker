import pytest

from models.grupo_muscular import GrupoMuscular


def test_crear_grupo_muscular():
    g = GrupoMuscular("Bicep")
    assert g.nombre == "Bicep"


def test_asignar_nombre_valido():
    g = GrupoMuscular("Bicep")
    g.nombre = "Tricep"
    assert g.nombre == "Tricep"

@pytest.mark.parametrize(
    "valor",
    [
        pytest.param("", id="cadena_vacia"),
        pytest.param(" ", id="solo_espacios"),
        pytest.param("\n\t", id="solo_tabulacion_y_sato")
    ]
)
def test_crear_con_cadena_vacia_lanza_error(valor):
    with pytest.raises(ValueError):
        g = GrupoMuscular(valor)