from dataclasses import dataclass

@dataclass(frozen=True)
class Koordinate:
    """Repräsentiert eine Koordinate auf dem Schachbrett."""
    spalte: int
    reihe: int

    def __post_init__(self):
        """Validiert die Koordinate nach der Initialisierung."""
        if self.spalte not in range(1, 9):
            raise ValueError(f"Ungültige Spalte: {self.spalte}.")
        if self.reihe not in range(1, 9):
            raise ValueError(f"Ungültige Reihe: {self.reihe}.")

    def __str__(self) -> str:
        """Gibt die Zeichenkette der Koordinate zurück."""
        spalten_buchstaben = "abcdefgh"
        return f"{spalten_buchstaben[self.spalte - 1]}{self.reihe}"

    def __repr__(self) -> str:
        """Gibt die detaillierte Zeichenkette der Koordinate zurück."""
        return f"Koordinate(spalte={self.spalte}, reihe={self.reihe})"
