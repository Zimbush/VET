from enum import Enum

class Farbe(Enum):
    W = "weiß"
    S = "schwarz"

    def __str__(self):
        return self.value

    def kurz(self):
        return self.name.lower()

    def gegenteil(self):
        return Farbe.S if self == Farbe.W else Farbe.W