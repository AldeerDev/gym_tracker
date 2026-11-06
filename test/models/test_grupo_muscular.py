import pytest

from models.grupo_muscular import GrupoMuscular


def test_crear_grupo_muscular():
    g = GrupoMuscular("Bicep")
    assert g.nombre == "Bicep"

def test_asignar_nombre_valido():
    g = GrupoMuscular("Bicep")
    g.nombre = "Tricep"
    assert g.nombre == "Tricep"