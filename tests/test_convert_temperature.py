from src.temperature_converter import (
    convert_to_celsius,
    convert_to_fahrenheit,
    convert_to_kelvin
)


def test_convert_to_celsius():
    assert convert_to_celsius("f", 50) == 10
    assert convert_to_celsius("k", 120) == -153.15
    
def test_convert_to_fahrenheit():
    assert convert_to_fahrenheit("c", 50) == 86
    assert convert_to_fahrenheit("k", 150) == -189.67

def test_convert_to_kelvin():
    assert convert_to_kelvin("c", 100) == 373.15
    assert convert_to_kelvin("f", 70) == 294.26111
