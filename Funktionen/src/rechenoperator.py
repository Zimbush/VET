from enum import Enum


class Operator(Enum):
    ADD = ("+", lambda a, b: a + b)
    MULT = ("*", lambda a, b: a * b)
    
    def verknuepfen(self, a: float, b: float) -> float:
        """Verknüpft zwei Gleitkommazahlen mit diesem Operator."""
        return self.value[1](a, b)

    