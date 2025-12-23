from dataclasses import dataclass
from halbzug import Halbzug

@dataclass
class HalbzugToken:
    """Repräsentiert einen Token für einen Halbzug."""
    ebene: int
    halbzug: Halbzug

@dataclass
class VarianteStartToken:
    """Repräsentiert den Anfang einer Variante."""
    ebene: int

@dataclass
class VarianteEndToken:
    """Repräsentiert das Ende einer Variante."""
    ebene: int

@dataclass
class SpielendToken:
    """Repräsentiert das Ende eines Spiels."""
    pass

Token = HalbzugToken | VarianteStartToken | VarianteEndToken | SpielendToken
