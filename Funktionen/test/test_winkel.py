from winkel import addiere_winkel, ist_winkel_normalisiert

def test_einfache_addition():
    assert addiere_winkel(10, 20) == 30

def test_ueberlauf():
    assert addiere_winkel(350, 20) == 10

def test_null():
    assert addiere_winkel(0, 0) == 0

def test_genau_360():
    assert addiere_winkel(180, 180) == 0

def test_negative_winkel():
    assert addiere_winkel(-10, 20) == 10
    assert addiere_winkel(10, -20) == 350

def test_ist_winkel_normalisiert():
    assert ist_winkel_normalisiert(0) is True
    assert ist_winkel_normalisiert(359.9999) is True
    assert ist_winkel_normalisiert(360) is False
    assert ist_winkel_normalisiert(-0.0001) is False
    assert ist_winkel_normalisiert(720) is False
