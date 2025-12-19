from farbe import Farbe

def test_str():
    assert str(Farbe.W) == "weiß"
    assert str(Farbe.S) == "schwarz"

def test_kurz():
    assert Farbe.W.kurz() == "w"
    assert Farbe.S.kurz() == "s"

def test_gegenteil():
    assert Farbe.W.gegenteil() == Farbe.S
    assert Farbe.S.gegenteil() == Farbe.W