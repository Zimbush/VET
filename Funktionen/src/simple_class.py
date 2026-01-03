from typing import overload


class SimpleClass:
    
    wert: str       

    def __init__(self, wert: str) -> None:
        self.wert = wert

    def __str__(self) -> str:
        return self.wert
    
    @overload
    def append(self, suffix: int) -> None: ...

    @overload
    def append(self, suffix: str) -> None: ...

    def append(self, suffix: int | str) -> None:
        if isinstance(suffix, int):
            self.wert += str(suffix)
        else:    
            self.wert += suffix

sc = SimpleClass("Test")
print(sc)
sc.append(123)
print(sc)
sc.append("_ende")
print(sc)
        