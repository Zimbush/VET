from dataclasses import dataclass
from halbzug import Halbzug

@dataclass
class HalbzugToken:
    ebene: int
    halbzug: Halbzug

@dataclass
class VarianteStartToken:
    ebene: int

@dataclass
class VarianteEndToken:
    ebene: int

@dataclass
class SpielendToken:
    pass

Token = HalbzugToken | VarianteStartToken | VarianteEndToken | SpielendToken
