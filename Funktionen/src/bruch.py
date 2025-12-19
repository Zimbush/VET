class Bruch_LY:
    
    def __init__(self, zaehler: int, nenner: int) -> None:
        if nenner == 0:
            raise ValueError("Nenner darf nicht 0 sein")
        self.zaehler: int = zaehler
        self.nenner: int = nenner
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bruch_LY):
            return False
        return self.zaehler == other.zaehler and self.nenner == other.nenner
    
    def __str__(self) -> str:
        return f"({self.zaehler},{self.nenner})"


class Bruch_PY:
    
    def __init__(self, zaehler: int, nenner: int) -> None:
        if nenner == 0:
            raise ValueError("Nenner darf nicht 0 sein")
        self.__zaehler: int = zaehler
        self.__nenner: int = nenner
    
    @property
    def zaehler(self) -> int:
        return self.__zaehler
    
    @zaehler.setter
    def zaehler(self, value: int) -> None:
        self.__zaehler = value
    
    @property
    def nenner(self) -> int:
        return self.__nenner
    
    @nenner.setter
    def nenner(self, value: int) -> None:
        if value == 0:
            raise ValueError("Nenner darf nicht 0 sein")
        self.__nenner = value
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bruch_PY):
            return False
        return self.zaehler == other.zaehler and self.nenner == other.nenner
    
    def __str__(self) -> str:
        return f"({self.zaehler},{self.nenner})"


from dataclasses import dataclass


@dataclass
class Bruch_DC:
    zaehler: int
    nenner: int
    
    def __post_init__(self) -> None:
        if self.nenner == 0:
            raise ValueError("Nenner darf nicht 0 sein")
    
    def __str__(self) -> str:
        return f"({self.zaehler},{self.nenner})"


@dataclass(frozen=True)
class Bruch_IM:
    zaehler: int
    nenner: int
    
    def __init__(self, zaehler: int, nenner: int) -> None:
        if nenner == 0:
            raise ValueError("Nenner darf nicht 0 sein")
        object.__setattr__(self, 'zaehler', zaehler)
        object.__setattr__(self, 'nenner', nenner)
    
    def __str__(self) -> str:
        return f"({self.zaehler},{self.nenner})"
    
    def __hash__(self) -> int:
        return hash((self.zaehler, self.nenner))
