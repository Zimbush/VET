import pytest
from feld import Feld
from koordinate import Koordinate
from spielstein import Spielstein, SpielsteinTyp
from farbe import Farbe

def test_feld_leer():
    feld = Feld(Koordinate(1, 1))
    assert feld.ist_leer()
    assert feld.spielstein is None

def test_feld_mit_spielstein():
    koord = Koordinate(5, 4)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    feld = Feld(koord, spielstein)
    
    assert not feld.ist_leer()
    assert feld.spielstein == spielstein
    assert feld.koordinate == koord

def test_feld_str_leer():
    feld = Feld(Koordinate(1, 1))
    assert str(feld) == "a1"

def test_feld_str_mit_spielstein():
    koord = Koordinate(5, 4)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    feld = Feld(koord, spielstein)
    assert str(feld) == "e4: weiß König"

def test_feld_setze_spielstein():
    feld = Feld(Koordinate(1, 1))
    assert feld.ist_leer()
    
    spielstein = Spielstein(SpielsteinTyp.BAUER, Farbe.W)
    feld.setze_spielstein(spielstein)
    
    assert not feld.ist_leer()
    assert feld.spielstein == spielstein

def test_feld_entferne_spielstein():
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.S)
    feld = Feld(Koordinate(5, 4), spielstein)
    
    entfernter = feld.entferne_spielstein()
    assert entfernter == spielstein
    assert feld.ist_leer()
