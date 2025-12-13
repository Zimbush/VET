from enum import Enum
from dataclasses import dataclass
from farbe import Farbe

class SpielsteinTyp(Enum):
    KOENIG = "König"
    DAME = "Dame"
    TURM = "Turm"
    LAEUFER = "Läufer"
    SPRINGER = "Springer"
    BAUER = "Bauer"

    def __str__(self) -> str:
        return self.value

    def notation(self) -> str:
        if self == SpielsteinTyp.BAUER:
            return ""
        return self.value[0]

@dataclass(frozen=True)
class Spielstein:
    typ: SpielsteinTyp
    farbe: Farbe

    def __str__(self) -> str:
        return f"{self.farbe} {self.typ}"

    def notation(self) -> str:
        return self.typ.notation()
