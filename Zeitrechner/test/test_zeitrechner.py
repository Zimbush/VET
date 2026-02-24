"""Tests für Zeitrechner-Funktionen."""

from zeitrechner import (
    stunden_zu_minuten,
    minuten_zu_stunden,
    minuten_rest,
    uhrzeit_differenz,
)


class TestStundenZuMinuten:
    """Tests für die Umrechnung von Stunden in Minuten."""
    
    def test_null_stunden(self):
        assert stunden_zu_minuten(0) == 0
    
    def test_eine_stunde(self):
        assert stunden_zu_minuten(1) == 60
    
    def test_mehrere_stunden(self):
        assert stunden_zu_minuten(5) == 300
        assert stunden_zu_minuten(24) == 1440


class TestMinutenZuStunden:
    """Tests für die Umrechnung von Minuten in Stunden (Ganzzahlanteil)."""
    
    def test_null_minuten(self):
        assert minuten_zu_stunden(0) == 0
    
    def test_weniger_als_eine_stunde(self):
        assert minuten_zu_stunden(30) == 0
        assert minuten_zu_stunden(59) == 0
    
    def test_genau_eine_stunde(self):
        assert minuten_zu_stunden(60) == 1
    
    def test_mehrere_stunden(self):
        assert minuten_zu_stunden(120) == 2
        assert minuten_zu_stunden(150) == 2
        assert minuten_zu_stunden(180) == 3


class TestMinutenRest:
    """Tests für die Berechnung der restlichen Minuten."""
    
    def test_null_minuten(self):
        assert minuten_rest(0) == 0
    
    def test_weniger_als_eine_stunde(self):
        assert minuten_rest(30) == 30
        assert minuten_rest(45) == 45
    
    def test_genau_eine_stunde(self):
        assert minuten_rest(60) == 0
    
    def test_mit_rest(self):
        assert minuten_rest(90) == 30
        assert minuten_rest(125) == 5
        assert minuten_rest(185) == 5


class TestUhrzeitDifferenz:
    """Tests für die Berechnung der Differenz zwischen zwei Uhrzeiten."""
    
    def test_gleiche_uhrzeiten(self):
        assert uhrzeit_differenz((12, 30), (12, 30)) == (0, 0)
    
    def test_differenz_nur_minuten(self):
        assert uhrzeit_differenz((12, 30), (12, 45)) == (0, 15)
    
    def test_differenz_nur_stunden(self):
        assert uhrzeit_differenz((12, 0), (14, 0)) == (2, 0)
    
    def test_differenz_stunden_und_minuten(self):
        assert uhrzeit_differenz((12, 15), (14, 30)) == (2, 15)
        assert uhrzeit_differenz((14, 20), (16, 45)) == (2, 25)
    
    def test_uebertrag_bei_minuten(self):
        # 12:30 bis 14:15 = 1:45
        assert uhrzeit_differenz((12, 30), (14, 15)) == (1, 45)
    
    def test_reihenfolge_egal(self):
        # Wenn zeit1 nach zeit2 liegt, wird ein Tag vorher angenommen
        assert uhrzeit_differenz((14, 45), (12, 30)) == (21, 45)
        assert uhrzeit_differenz((12, 30), (14, 45)) == (2, 15)
    
    def test_mitternacht_grenze(self):
        # 23:45 bis 0:15 = 0:30 (über Mitternacht)
        assert uhrzeit_differenz((23, 45), (0, 15)) == (0, 30)
