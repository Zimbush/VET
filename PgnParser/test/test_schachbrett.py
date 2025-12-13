import pytest
from schachbrett import Schachbrett
from koordinate import Koordinate
from spielstein import Spielstein, SpielsteinTyp
from farbe import Farbe

def test_schachbrett_initialisierung():
    brett = Schachbrett()
    for spalte in range(1, 9):
        for reihe in range(1, 9):
            koord = Koordinate(spalte, reihe)
            assert brett.feld(koord).ist_leer()

def test_schachbrett_feld_zugriff():
    brett = Schachbrett()
    koord = Koordinate(5, 4)
    feld = brett.feld(koord)
    assert feld.koordinate == koord

def test_schachbrett_feld_setzen():
    brett = Schachbrett()
    koord = Koordinate(5, 4)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    
    brett.feld(koord).setze_spielstein(spielstein)
    assert not brett.feld(koord).ist_leer()
    assert brett.feld(koord).spielstein == spielstein
