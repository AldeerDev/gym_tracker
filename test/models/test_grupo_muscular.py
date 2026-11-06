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


@pytest.mark.parametrize(
    "valor",
    [
        pytest.param(None, id="none"),
        pytest.param(123, id="entero"),
        pytest.param(5.5, id="float"),
        pytest.param([], id="lista_vacia"),
        pytest.param(["bicep"], id="lista_con_string")
    ]
)
def test_crear_con_tipo_invalido_lanza_error(valor):
    with pytest.raises(ValueError):
        GrupoMuscular(valor)


@pytest.mark.parametrize(
    "valor",
    [
        pytest.param("", id="cadena_vacia"),
        pytest.param(" ", id="solo_espacios"),
        pytest.param("\n\t", id="solo_tabulacion_y_salto")
    ]
)
def test_asignar_nombre_invalido_lanza_error(valor):
    g = GrupoMuscular("bicep")
    with pytest.raises(ValueError):
        g.nombre = valor


@pytest.mark.parametrize(
    "valor",
    [
        pytest.param(None, id="none"),
        pytest.param(123, id="entero"),
        pytest.param(5.5, id="float"),
        pytest.param([], id="lista_vacia"),
        pytest.param(["bicep"], id="lista_con_string")
    ]
)
def test_asignar_nombre_invalido_no_modifica_el_anterior(valor):
    g = GrupoMuscular("bicep")
    with pytest.raises(ValueError):
        g.nombre = valor
    assert g.nombre == "bicep"