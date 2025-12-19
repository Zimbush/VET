from dataclasses import dataclass
from koordinate import Koordinate
from spielstein import Spielstein

@dataclass
class Feld:

    __koordinate: Koordinate
    __spielstein: Spielstein | None = None

    def __init__(self, koordinate: Koordinate, spielstein: Spielstein | None = None):
        self.__koordinate = koordinate
        self.__spielstein = spielstein

    @property
    def koordinate(self) -> Koordinate:
        return self.__koordinate

    @property
    def spielstein(self) -> Spielstein | None:
        return self.__spielstein
    
    def ist_leer(self) -> bool:
        return self.__spielstein is None

    def setze_spielstein(self, spielstein: Spielstein) -> None:
        self.__spielstein = spielstein

    def entferne_spielstein(self) -> Spielstein | None:
        temp = self.__spielstein
        self.__spielstein = None    
        return temp

    def __str__(self) -> str:
        if self.ist_leer():
            return str(self.__koordinate)
        return f"{self.__koordinate}: {self.__spielstein}"