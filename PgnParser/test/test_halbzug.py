import pytest
import dataclasses
from halbzug import Halbzug
from farbe import Farbe

def test_halbzug_initialisierung():
    halbzug = Halbzug(1, Farbe.W)
    assert halbzug.zugnummer == 1
    assert halbzug.farbe == Farbe.W

def test_halbzug_str():
    halbzug_weiss = Halbzug(1, Farbe.W)
    assert str(halbzug_weiss) == "1."

    halbzug_schwarz = Halbzug(1, Farbe.S)
    assert str(halbzug_schwarz) == "1..."

def test_halbzug_validation():
    with pytest.raises(ValueError):
        Halbzug(0, Farbe.W)
    with pytest.raises(ValueError):
        Halbzug(1, Farbe("invalid_farbe"))

def test_halbzug_kurznotation():
    # Test für die Kurznotation der weißen Farbe
    halbzug_weiss = Halbzug(1, Farbe.W)
    assert halbzug_weiss.kurz() == "1w"
    
    # Test für die Kurznotation der schwarzen Farbe
    halbzug_schwarz = Halbzug(2, Farbe.S)
    assert halbzug_schwarz.kurz() == "2s"

def test_halbzug_nachfolger():
    halbzug = Halbzug(1, Farbe.W)
    nachfolger = halbzug.nachfolger()

    assert nachfolger.zugnummer == 1
    assert nachfolger.farbe == Farbe.S

    halbzug = Halbzug(2, Farbe.S)
    nachfolger = halbzug.nachfolger()

    assert nachfolger.zugnummer == 3
    assert nachfolger.farbe == Farbe.W