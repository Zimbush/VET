from lotto import anzahl_lotto_kombinationen

def test_standard_lotto():
    assert anzahl_lotto_kombinationen() == 13983816

def test_andere_werte():
    assert anzahl_lotto_kombinationen(10, 2) == 45
    assert anzahl_lotto_kombinationen(5, 5) == 1
    assert anzahl_lotto_kombinationen(7, 0) == 1
