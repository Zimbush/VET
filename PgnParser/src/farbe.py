from enum import Enum

class Farbe(Enum):
    """Enumeration für die Farben der Schachfiguren."""
    W = "weiß"
    S = "schwarz"

    def __str__(self) -> str:
        """Gibt die Zeichenkette der Farbe zurück."""
        return self.value

    def kurz(self) -> str:
        """Gibt die Kurzform der Farbe zurück."""
        return self.name.lower()

    def gegenteil(self) -> "Farbe":
        """Gibt die entgegengesetzte Farbe zurück."""
        return Farbe.S if self == Farbe.W else Farbe.W