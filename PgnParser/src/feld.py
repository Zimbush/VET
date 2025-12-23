from dataclasses import dataclass
from koordinate import Koordinate
from spielstein import Spielstein

@dataclass
class Feld:
    """Repräsentiert ein Schachfeld mit einer Koordinate und einer optionalen Figur."""

    __koordinate: Koordinate
    __spielstein: Spielstein | None = None

    def __init__(self, koordinate: Koordinate, spielstein: Spielstein | None = None):
        """Initialisiert ein Feld mit einer Koordinate und einer optionalen Figur."""
        self.__koordinate = koordinate
        self.__spielstein = spielstein

    @property
    def koordinate(self) -> Koordinate:
        """Gibt die Koordinate des Feldes zurück."""
        return self.__koordinate

    @property
    def spielstein(self) -> Spielstein | None:
        """Gibt die Figur auf dem Feld zurück, falls vorhanden."""
        return self.__spielstein
    
    def ist_leer(self) -> bool:
        """Prüft, ob das Feld leer ist."""
        return self.__spielstein is None

    def setze_spielstein(self, spielstein: Spielstein) -> None:
        """Setzt eine Figur auf das Feld."""
        self.__spielstein = spielstein

    def entferne_spielstein(self) -> Spielstein | None:
        """Entfernt und gibt die Figur vom Feld zurück."""
        temp = self.__spielstein
        self.__spielstein = None    
        return temp

    def __str__(self) -> str:
        """Gibt eine Zeichenkette des Feldes zurück."""
        if self.ist_leer():
            return str(self.__koordinate)
        return f"{self.__koordinate}: {self.__spielstein}"