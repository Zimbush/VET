from dataclasses import dataclass
from farbe import Farbe

@dataclass(frozen=True)
class Zugnummer:
    zugnummer: int
    farbe: Farbe

    def __post_init__(self):
        if self.zugnummer < 1:
            raise ValueError(f"Unmögliche Zugnummer: {self.zugnummer}.")
        if not isinstance(self.farbe, Farbe):
            raise ValueError(f"Unbekannte Farbe: {self.farbe}.")

    def kurz(self) -> str:
        return f"{self.zugnummer}{self.farbe.kurz()}"
    
    def notation(self) -> str:
        return f"{self.zugnummer}." if self.farbe == Farbe.W else f"{self.zugnummer}..."    

    def nachfolger(self) -> Zugnummer:
        return Zugnummer(self.zugnummer + (1 if self.farbe == Farbe.S else 0), self.farbe.gegenteil())