import pytest
from src.versandkosten import berechne_versandkosten




def test_bestellsumme():
    assert berechne_versandkosten(37.75) == 5.00
    assert berechne_versandkosten(65.83) == 0.00


# @pytest.mark.parametrize("summe,erwartet", [
#     (10.00, 5.00),
#     (25.50, 5.00),
#     (50.00, 5.00),
#     (50.01, 0.00),
#     (75.25, 0.00),
#     (200.00, 0.00),
# ])
# def test_verschiedene_bestellsummen(summe: float, erwartet: float):
#     """Test mit verschiedenen Bestellsummen"""
#     assert berechne_versandkosten(summe) == erwartet
