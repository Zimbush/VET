import pytest
from koordinate import Koordinate

def test_koordinate_initialisierung():
    koord = Koordinate(5, 4)
    assert koord.spalte == 5
    assert koord.reihe == 4

def test_koordinate_str():
    koord = Koordinate(5, 4)
    assert str(koord) == "e4"

    koord = Koordinate(1, 1)
    assert str(koord) == "a1"

def test_koordinate_repr():
    koord = Koordinate(5, 4)
    assert repr(koord) == "Koordinate(spalte=5, reihe=4)"

def test_koordinate_spalte_validation():
    with pytest.raises(ValueError):
        Koordinate(9, 4)
    
    with pytest.raises(ValueError):
        Koordinate(0, 4)

def test_koordinate_reihe_validation():
    with pytest.raises(ValueError):
        Koordinate(5, 0)
    
    with pytest.raises(ValueError):
        Koordinate(5, 9)
