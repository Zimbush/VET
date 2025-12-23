from dataclasses import dataclass
from farbe import Farbe

@dataclass(frozen=True)
class Zugnummer:
    """Repräsentiert eine Zugnummer in einem Schachspiel."""
    zugnummer: int
    farbe: Farbe

    def __post_init__(self):
        """Validiert die Zugnummer nach der Initialisierung."""
        if self.zugnummer < 1:
            raise ValueError(f"Unmögliche Zugnummer: {self.zugnummer}.")
        if not isinstance(self.farbe, Farbe):
            raise ValueError(f"Unbekannte Farbe: {self.farbe}.")

    def kurz(self) -> str:
        """Gibt die Kurzform der Zugnummer zurück."""
        return f"{self.zugnummer}{self.farbe.kurz()}"
    
    def notation(self) -> str:
        """Gibt die Standard-Notation der Zugnummer zurück."""
        return f"{self.zugnummer}." if self.farbe == Farbe.W else f"{self.zugnummer}..."    

    def nachfolger(self) -> Zugnummer:
        """Gibt die nächste Zugnummer zurück."""
        return Zugnummer(self.zugnummer + (1 if self.farbe == Farbe.S else 0), self.farbe.gegenteil())