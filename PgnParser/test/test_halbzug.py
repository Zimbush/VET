import pytest
from halbzug import Halbzug
from koordinate import Koordinate
from spielstein import Spielstein, SpielsteinTyp
from farbe import Farbe
from zugnummer import Zugnummer

def test_halbzug_initialisierung():
    zugnummer = Zugnummer(1, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    halbzug = Halbzug(zugnummer, spielstein, Koordinate(5, 2), von=Koordinate(5, 1))
    
    assert halbzug.zugnummer == zugnummer
    assert halbzug.zugnummer.farbe == Farbe.W
    assert halbzug.spielstein == spielstein
    assert halbzug.von == Koordinate(5, 1)
    assert halbzug.zu == Koordinate(5, 2)

def test_halbzug_farben_konsistenz():
    zugnummer = Zugnummer(1, Farbe.S)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    # Schwarzer Zug mit weißem Spielstein sollte fehlschlagen
    with pytest.raises(ValueError):
        Halbzug(zugnummer, spielstein, Koordinate(5, 2), von=Koordinate(5, 1))

def test_halbzug_identische_felder():
    zugnummer = Zugnummer(1, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    with pytest.raises(ValueError):
        Halbzug(zugnummer, spielstein, Koordinate(5, 1), von=Koordinate(5, 1))

def test_halbzug_schach_und_matt():
    zugnummer = Zugnummer(1, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    with pytest.raises(ValueError):
        Halbzug(zugnummer, spielstein, Koordinate(5, 2), von=Koordinate(5, 1), ist_schach=True, ist_matt=True)

def test_halbzug_str_normal():
    zugnummer = Zugnummer(1, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    halbzug = Halbzug(zugnummer, spielstein, Koordinate(5, 2), von=Koordinate(5, 1))
    assert str(halbzug) == "1. Ke2"

def test_halbzug_str_mit_schach():
    zugnummer = Zugnummer(1, Farbe.S)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.S)
    halbzug = Halbzug(zugnummer, spielstein, Koordinate(5, 7), von=Koordinate(5, 8), ist_schach=True)
    assert str(halbzug) == "1... Ke7+"

def test_halbzug_str_mit_matt():
    zugnummer = Zugnummer(10, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.DAME, Farbe.W)
    halbzug = Halbzug(zugnummer, spielstein, Koordinate(4, 8), von=Koordinate(4, 4), ist_matt=True)
    assert str(halbzug) == "10. Dd8#"

def test_halbzug_mit_nag():
    zugnummer = Zugnummer(1, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    halbzug = Halbzug(zugnummer, spielstein, Koordinate(5, 2), von=Koordinate(5, 1), nag=1)
    assert halbzug.nag == 1

def test_halbzug_nag_optional():
    zugnummer = Zugnummer(1, Farbe.W)
    spielstein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    halbzug = Halbzug(zugnummer, spielstein, Koordinate(5, 2), von=Koordinate(5, 1))
    assert halbzug.nag is None
