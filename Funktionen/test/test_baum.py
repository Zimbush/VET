import pytest
from baum import Blatt, Knoten, BaumKnoten, BaumAuswertung, BaumAuswertungSingleDispatch


class TestBlatt:
    def test_blatt_erstellung(self) -> None:
        blatt = Blatt(5)
        assert blatt.wert() == 5
    
    def test_blatt_string(self) -> None:
        blatt = Blatt(3)
        assert str(blatt) == "Blatt(3)"
    
    def test_blatt_repr(self) -> None:
        blatt = Blatt(3)
        assert repr(blatt) == "Blatt(3)"


class TestKnoten:
    def test_knoten_mit_zwei_blaettern(self) -> None:
        blatt_links = Blatt(3)
        blatt_rechts = Blatt(4)
        knoten = Knoten(blatt_links, blatt_rechts)
        assert knoten.wert() == 7
    
    def test_knoten_mit_verschachtelten_knoten(self) -> None:
        blatt1 = Blatt(1)
        blatt2 = Blatt(2)
        blatt3 = Blatt(3)
        blatt4 = Blatt(4)
        
        knoten_links = Knoten(blatt1, blatt2)
        knoten_rechts = Knoten(blatt3, blatt4)
        knoten_oben = Knoten(knoten_links, knoten_rechts)
        
        assert knoten_oben.wert() == 10
    
    def test_knoten_links_eigenschaft(self) -> None:
        blatt_links = Blatt(1)
        blatt_rechts = Blatt(2)
        knoten = Knoten(blatt_links, blatt_rechts)
        assert knoten.links == blatt_links
    
    def test_knoten_rechts_eigenschaft(self) -> None:
        blatt_links = Blatt(1)
        blatt_rechts = Blatt(2)
        knoten = Knoten(blatt_links, blatt_rechts)
        assert knoten.rechts == blatt_rechts


class TestBaumAuswertung:
    def test_auswerten_einzelnes_blatt(self) -> None:
        blatt = Blatt(5)
        visitor = BaumAuswertung()
        assert visitor.auswerten(blatt) == 5
    
    def test_auswerten_knoten_mit_zwei_blaettern(self) -> None:
        blatt_links = Blatt(3)
        blatt_rechts = Blatt(4)
        knoten = Knoten(blatt_links, blatt_rechts)
        visitor = BaumAuswertung()
        assert visitor.auswerten(knoten) == 7
    
    def test_auswerten_verschachtelter_baum(self) -> None:
        blatt1 = Blatt(1)
        blatt2 = Blatt(2)
        blatt3 = Blatt(3)
        blatt4 = Blatt(4)
        
        knoten_links = Knoten(blatt1, blatt2)
        knoten_rechts = Knoten(blatt3, blatt4)
        knoten_oben = Knoten(knoten_links, knoten_rechts)
        
        visitor = BaumAuswertung()
        assert visitor.auswerten(knoten_oben) == 10


class TestBaumAuswertungSingleDispatch:
    def test_auswerten_einzelnes_blatt(self) -> None:
        blatt = Blatt(5)
        visitor = BaumAuswertungSingleDispatch()
        assert visitor.auswerten(blatt) == 5
    
    def test_auswerten_knoten_mit_zwei_blaettern(self) -> None:
        blatt_links = Blatt(3)
        blatt_rechts = Blatt(4)
        knoten = Knoten(blatt_links, blatt_rechts)
        visitor = BaumAuswertungSingleDispatch()
        assert visitor.auswerten(knoten) == 7
    
    def test_auswerten_verschachtelter_baum(self) -> None:
        blatt1 = Blatt(1)
        blatt2 = Blatt(2)
        blatt3 = Blatt(3)
        blatt4 = Blatt(4)
        
        knoten_links = Knoten(blatt1, blatt2)
        knoten_rechts = Knoten(blatt3, blatt4)
        knoten_oben = Knoten(knoten_links, knoten_rechts)
        
        visitor = BaumAuswertungSingleDispatch()
        assert visitor.auswerten(knoten_oben) == 10

