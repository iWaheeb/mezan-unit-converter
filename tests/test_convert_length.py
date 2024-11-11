from src.length_converter import convert_to_millimeter


def test_convert_to_millimeter():
    assert convert_to_millimeter(15, "cm") == 150
    assert convert_to_millimeter(3, "m") == 3000
    assert convert_to_millimeter(4.5, "km") == 4500000
    assert convert_to_millimeter(24, "in") == 609.6
    assert convert_to_millimeter(7, "ft") == 2133.6
    assert convert_to_millimeter(1.3, "yd") == 1188.72
    assert convert_to_millimeter(2, "mi") == 3218688