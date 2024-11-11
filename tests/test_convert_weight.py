from src.weight_converter import (
    convert_to_milligram,
    convert_to_gram,
    convert_to_kilogram,
    convert_to_ounce,
    convert_to_pound
)


def test_convert_to_milligram():
    assert convert_to_milligram("g", 7.5) == 7500
    assert convert_to_milligram("kg", 0.5) == 500000
    assert convert_to_milligram("oz", 0.7) == 19844.66619
    assert convert_to_milligram("lb", 3) == 1360777.11

def test_convert_to_gram():
    assert convert_to_gram("mg", 1200) == 1.2
    assert convert_to_gram("kg", 11.5) == 11500
    assert convert_to_gram("oz", 15) == 425.2428
    assert convert_to_gram("lb", 40) == 18143.6948
    
def test_convert_to_kilogram():
    assert convert_to_kilogram("mg", 17000) == 0.017
    assert convert_to_kilogram("g", 1200) == 1.2
    assert convert_to_kilogram("oz", 50) == 1.417
    assert convert_to_kilogram("lb", 140) == 63.50293

def test_convert_to_ounce():
    assert convert_to_ounce("mg", 750) == 0.02645
    assert convert_to_ounce("g", 140) == 4.93835
    assert convert_to_ounce("kg", 17) == 599.657
    assert convert_to_ounce("lb", 200) == 3200

def test_convert_to_pound():
    assert convert_to_pound("mg", 1600) == 0.00353
    assert convert_to_pound("g", 860) == 1.89598
    assert convert_to_pound("kg", 45) == 99.208
    assert convert_to_pound("oz", 500) == 31.25
