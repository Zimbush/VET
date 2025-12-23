from enum import Enum
from dataclasses import dataclass
from farbe import Farbe

class SpielsteinTyp(Enum):
    """Enumeration für die Typen von Schachfiguren."""
    KOENIG = "König"
    DAME = "Dame"
    TURM = "Turm"
    LAEUFER = "Läufer"
    SPRINGER = "Springer"
    BAUER = "Bauer"

    def __str__(self) -> str:
        """Gibt die Zeichenkette des Figurentyps zurück."""
        return self.value

    def notation(self) -> str:
        """Gibt die PGN-Notation des Figurentyps zurück."""
        if self == SpielsteinTyp.BAUER:
            return ""
        return self.value[0]

@dataclass(frozen=True)
class Spielstein:
    """Repräsentiert eine Schachfigur mit Typ und Farbe."""
    typ: SpielsteinTyp
    farbe: Farbe

    def __str__(self) -> str:
        """Gibt die Zeichenkette der Figur zurück."""
        return f"{self.farbe} {self.typ}"

    def notation(self) -> str:
        """Gibt die PGN-Notation der Figur zurück."""
        return self.typ.notation()
