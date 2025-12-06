def stunden_zu_minuten(stunden: int) -> int:
    return stunden * 60


def minuten_zu_stunden(minuten: int) -> int:
    return minuten // 60


def minuten_rest(minuten: int) -> int:
    return minuten % 60


def uhrzeit_differenz(zeit1: tuple[int, int], zeit2: tuple[int, int]) -> tuple[int, int]:
    minuten1 = zeit1[0] * 60 + zeit1[1]
    minuten2 = zeit2[0] * 60 + zeit2[1]
    differenz_minuten = abs(minuten1 - minuten2)
    stunden = minuten_zu_stunden(differenz_minuten)
    minuten = minuten_rest(differenz_minuten)
    return (stunden, minuten)
