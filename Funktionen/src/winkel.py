def addiere_winkel(winkel1: float, winkel2: float) -> float:
    return (winkel1 + winkel2) % 360

def normalisiere_winkel(winkel: float) -> float:
    return winkel % 360

def ist_winkel_normalisiert(winkel: float) -> bool:
    return 0 <= winkel < 360