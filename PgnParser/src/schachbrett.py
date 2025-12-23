from koordinate import Koordinate
from feld import Feld

class Schachbrett:
    """Repräsentiert ein Schachbrett mit 8x8 Feldern."""
    
    def __init__(self):
        """Initialisiert das Schachbrett mit leeren Feldern."""
        self.__felder: dict[Koordinate, Feld] = {}
        for spalte in range(1, 9):
            for reihe in range(1, 9):
                koord = Koordinate(spalte, reihe)
                self.__felder[koord] = Feld(koord)

    def feld(self, koordinate: Koordinate) -> Feld:
        """Gibt das Feld für eine Koordinate zurück."""
        if koordinate not in self.__felder:
            raise ValueError(f"Ungültige Koordinate: {koordinate}")
        return self.__felder[koordinate]

    def __str__(self) -> str:
        """Gibt eine Zeichenkette des Schachbretts zurück."""
        result = []
        for reihe in range(8, 0, -1):
            reihe_str = f"{reihe} "
            for spalte in range(1, 9):
                koord = Koordinate(spalte, reihe)
                feld = self.__felder[koord]
                if feld.spielstein is None:
                    reihe_str += ". "
                else:
                    reihe_str += f"{feld.spielstein.notation()} "
            result.append(reihe_str)
        result.append("  a b c d e f g h")
        return "\n".join(result)
