import pytest
from src.temperatur_umrechnung import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert pytest.approx(celsius_to_fahrenheit(37), 0.1) == 98.6

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert pytest.approx(fahrenheit_to_celsius(98.6), 0.1) == 37
