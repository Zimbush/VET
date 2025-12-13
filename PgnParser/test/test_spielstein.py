from spielstein import Spielstein, SpielsteinTyp
from farbe import Farbe

def test_spielstein_initialisierung():
    stein = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    assert stein.typ == SpielsteinTyp.KOENIG
    assert stein.farbe == Farbe.W

def test_spielstein_typ():
    assert str(SpielsteinTyp.KOENIG) == "König"
    assert str(SpielsteinTyp.DAME) == "Dame"
    assert str(SpielsteinTyp.TURM) == "Turm"
    assert str(SpielsteinTyp.LAEUFER) == "Läufer"
    assert str(SpielsteinTyp.SPRINGER) == "Springer"
    assert str(SpielsteinTyp.BAUER) == "Bauer"

def test_spielstein_str():
    stein_weiss = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    assert str(stein_weiss) == "weiß König"
    
    stein_schwarz = Spielstein(SpielsteinTyp.BAUER, Farbe.S)
    assert str(stein_schwarz) == "schwarz Bauer"

def test_spielstein_pgn_notation():
    assert SpielsteinTyp.KOENIG.notation() == "K"
    assert SpielsteinTyp.DAME.notation() == "D"
    assert SpielsteinTyp.TURM.notation() == "T"
    assert SpielsteinTyp.LAEUFER.notation() == "L"
    assert SpielsteinTyp.SPRINGER.notation() == "S"
    assert SpielsteinTyp.BAUER.notation() == ""

def test_spielstein_pgn_notation_mit_farbe():
    stein_weiss_koenig = Spielstein(SpielsteinTyp.KOENIG, Farbe.W)
    assert stein_weiss_koenig.notation() == "K"
    
    stein_schwarz_koenig = Spielstein(SpielsteinTyp.KOENIG, Farbe.S)
    assert stein_schwarz_koenig.notation() == "K"
    
    stein_weiss_bauer = Spielstein(SpielsteinTyp.BAUER, Farbe.W)
    assert stein_weiss_bauer.notation() == ""
    
    stein_schwarz_bauer = Spielstein(SpielsteinTyp.BAUER, Farbe.S)
    assert stein_schwarz_bauer.notation() == ""