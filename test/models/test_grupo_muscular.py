import pytest

from models.grupo_muscular import GrupoMuscular


def test_crear_grupo_muscular():
    grupom = GrupoMuscular("Bicep")
    assert grupom.nombre == "Bicep"