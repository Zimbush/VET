from dataclasses import dataclass
from koordinate import Koordinate
from spielstein import Spielstein
from zugnummer import Zugnummer

@dataclass
class Halbzug:
    """Repräsentiert einen Halbzug in einem Schachspiel."""
    zugnummer: Zugnummer
    spielstein: Spielstein
    zu: Koordinate
    von: Koordinate | None = None
    ist_schach: bool = False
    ist_matt: bool = False
    nag: int | None = None

    def __post_init__(self):
        """Validiert den Halbzug nach der Initialisierung."""
        if self.spielstein.farbe != self.zugnummer.farbe:
            raise ValueError(f"Spielstein-Farbe stimmt nicht mit Zug-Farbe überein.")
        if self.von is not None and self.von == self.zu:
            raise ValueError("Von- und Zu-Feld können nicht identisch sein.")
        if self.ist_schach and self.ist_matt:
            raise ValueError("Ein Zug kann nicht gleichzeitig Schach und Matt sein.")

    def __str__(self) -> str:
        """Gibt die Zeichenkette des Halbzugs zurück."""
        notation = self.zugnummer.notation()
        notation += f" {self.spielstein.typ.notation()}{self.zu}"
        if self.ist_matt:
            notation += "#"
        elif self.ist_schach:
            notation += "+"
        return notation
