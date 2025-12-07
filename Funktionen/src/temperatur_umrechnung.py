"""
Modul: temperatur_umrechnung.py
Funktionen zur Umrechnung zwischen Celsius und Fahrenheit.
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Wandelt Celsius in Fahrenheit um.
    Formel: F = C * 9/5 + 32
    """
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Wandelt Fahrenheit in Celsius um.
    Formel: C = (F - 32) * 5/9
    """
    return (fahrenheit - 32) * 5 / 9
