from abc import ABC, abstractmethod
from typing import overload
from functools import singledispatchmethod


class BaumKnoten(ABC):
    """Abstrakte Basisklasse für Baumknoten"""
    
    @abstractmethod
    def wert(self) -> int:
        """Gibt den Wert des Blattes zurück"""
        pass


class Blatt(BaumKnoten):
    """Blatt eines binären Baumes mit einem Ganzzahlwert"""
    
    _wert: int
    
    def __init__(self, wert: int) -> None:
        self._wert = wert
    
    def wert(self) -> int:
        return self._wert
    
    def __str__(self) -> str:
        return f"Blatt({self._wert})"
    
    def __repr__(self) -> str:
        return f"Blatt({self._wert})"


class Knoten(BaumKnoten):
    """Innerer Knoten eines binären Baumes mit zwei Kindknoten"""
    
    _links: BaumKnoten
    _rechts: BaumKnoten
    
    def __init__(self, links: BaumKnoten, rechts: BaumKnoten) -> None:
        self._links = links
        self._rechts = rechts
    
    @property
    def links(self) -> BaumKnoten:
        return self._links
    
    @property
    def rechts(self) -> BaumKnoten:
        return self._rechts
    
    def wert(self) -> int:
        """Gibt die Summe der Werte aller Blätter zurück"""
        return self._links.wert() + self._rechts.wert()
    
    def __str__(self) -> str:
        return f"Knoten({self._links}, {self._rechts})"
    
    def __repr__(self) -> str:
        return f"Knoten({self._links!r}, {self._rechts!r})"


class BaumAuswertung:
    """Visitor zum Auswerten eines Baumes mit @overload für bessere Typ-Hinweise"""
    
    @overload
    def auswerten(self, knoten: Blatt) -> int:  ...
    
    @overload
    def auswerten(self, knoten: Knoten) -> int: ...
    
    @overload
    def auswerten(self, knoten: BaumKnoten) -> int: ...
    
    def auswerten(self, knoten: BaumKnoten) -> int:
        """Auswertung eines Baumknotens"""
        if isinstance(knoten, Blatt):
            return knoten.wert()
        elif isinstance(knoten, Knoten):
            links_wert = self.auswerten(knoten.links)
            rechts_wert = self.auswerten(knoten.rechts)
            return links_wert + rechts_wert
        else:
            raise NotImplementedError(f"Auswertung für {type(knoten)} nicht implementiert")


class BaumAuswertungSingleDispatch:
    """Visitor zum Auswerten eines Baumes mit @singledispatchmethod"""
    
    @singledispatchmethod
    def auswerten(self, knoten: BaumKnoten) -> int:
        """Allgemeine Auswertung (wird nicht direkt aufgerufen)"""
        raise NotImplementedError(f"Auswertung für {type(knoten)} nicht implementiert")
    
    @auswerten.register
    def _(self, blatt: Blatt) -> int:
        """Auswertung eines Blattes: Gibt einfach den Wert zurück"""
        return blatt.wert()
    
    @auswerten.register
    def _(self, knoten: Knoten) -> int:
        """Auswertung eines Knotens: Addiert die Werte beider Kinder"""
        links_wert = self.auswerten(knoten.links)
        rechts_wert = self.auswerten(knoten.rechts)
        return links_wert + rechts_wert
