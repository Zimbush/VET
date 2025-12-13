import pytest
from halbzug import Zugnummer
from farbe import Farbe

def test_zugnummer_initialisierung():
    zugnummer = Zugnummer(1, Farbe.W)
    assert zugnummer.zugnummer == 1
    assert zugnummer.farbe == Farbe.W

def test_zugnummer_notation():
    zugnummer_weiss = Zugnummer(1, Farbe.W)
    assert zugnummer_weiss.notation() == "1."

    zugnummer_schwarz = Zugnummer(1, Farbe.S)
    assert zugnummer_schwarz.notation() == "1..."

def test_zugnummer_validation():
    with pytest.raises(ValueError):
        Zugnummer(0, Farbe.W)
    with pytest.raises(ValueError):
        Zugnummer(1, Farbe("invalid_farbe"))

def test_zugnummer_kurznotation():
    # Test für die Kurznotation der weißen Farbe
    zugnummer_weiss = Zugnummer(1, Farbe.W)
    assert zugnummer_weiss.kurz() == "1w"
    
    # Test für die Kurznotation der schwarzen Farbe
    zugnummer_schwarz = Zugnummer(2, Farbe.S)
    assert zugnummer_schwarz.kurz() == "2s"

def test_zugnummer_nachfolger():
    zugnummer = Zugnummer(1, Farbe.W)
    nachfolger = zugnummer.nachfolger()
    assert nachfolger.zugnummer == 1
    assert nachfolger.farbe == Farbe.S

    zugnummer = Zugnummer(2, Farbe.S)
    nachfolger = zugnummer.nachfolger()

    assert nachfolger.zugnummer == 3
    assert nachfolger.farbe == Farbe.W