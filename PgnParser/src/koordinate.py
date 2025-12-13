from dataclasses import dataclass

@dataclass(frozen=True)
class Koordinate:
    spalte: int
    reihe: int

    def __post_init__(self):
        if self.spalte not in range(1, 9):
            raise ValueError(f"Ungültige Spalte: {self.spalte}.")
        if self.reihe not in range(1, 9):
            raise ValueError(f"Ungültige Reihe: {self.reihe}.")

    def __str__(self) -> str:
        spalten_buchstaben = "abcdefgh"
        return f"{spalten_buchstaben[self.spalte - 1]}{self.reihe}"

    def __repr__(self) -> str:
        return f"Koordinate(spalte={self.spalte}, reihe={self.reihe})"
