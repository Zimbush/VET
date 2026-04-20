import pytest
from src.versandkosten import berechne_versandkosten


class TestBerechneVersandkosten:
    """Tests für die Funktion berechne_versandkosten"""

    def test_bestellsumme_unter_50_euro(self):
        """Bestellsumme unter 50 Euro sollte 5 Euro Versandkosten kosten"""
        assert berechne_versandkosten(37.75) == 5.00
        assert berechne_versandkosten(1.00) == 5.00
        assert berechne_versandkosten(49.99) == 5.00

    def test_bestellsumme_genau_50_euro(self):
        """Bestellsumme genau 50 Euro sollte 5 Euro Versandkosten kosten"""
        assert berechne_versandkosten(50.00) == 5.00

    def test_bestellsumme_ueber_50_euro(self):
        """Bestellsumme über 50 Euro sollte kostenlos versendet werden"""
        assert berechne_versandkosten(50.01) == 0.00
        assert berechne_versandkosten(65.83) == 0.00
        assert berechne_versandkosten(100.00) == 0.00
        assert berechne_versandkosten(1000.00) == 0.00

    def test_bestellsumme_null(self):
        """Bestellsumme von 0 Euro sollte 5 Euro Versandkosten kosten"""
        assert berechne_versandkosten(0.00) == 5.00

    def test_bestellsumme_negativ(self):
        """Negative Bestellsummen sollten 5 Euro Versandkosten kosten"""
        assert berechne_versandkosten(-10.00) == 5.00

    def test_return_type(self):
        """Rückgabewert sollte float sein"""
        result = berechne_versandkosten(25.00)
        assert isinstance(result, float)

    @pytest.mark.parametrize("summe,erwartet", [
        (10.00, 5.00),
        (25.50, 5.00),
        (50.00, 5.00),
        (50.01, 0.00),
        (75.25, 0.00),
        (200.00, 0.00),
    ])
    def test_verschiedene_bestellsummen(self, summe, erwartet):
        """Test mit verschiedenen Bestellsummen"""
        assert berechne_versandkosten(summe) == erwartet
