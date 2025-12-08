from math import comb

def anzahl_lotto_kombinationen(n: int = 49, k: int = 6) -> int:
    """
    Berechnet die Anzahl der möglichen Kombinationen für das deutsche Lotto 6 aus 49.
    Formel: n! / (k! * (n-k)!)
    """
    return comb(n, k)
