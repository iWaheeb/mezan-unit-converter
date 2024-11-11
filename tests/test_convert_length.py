from src.length_converter import (
    convert_to_millimeter,
    convert_to_centimeter,
    convert_to_meter,
    convert_to_kilometer
)


def test_convert_to_millimeter():
    assert convert_to_millimeter("cm", 15) == 150
    assert convert_to_millimeter("m", 3) == 3000
    assert convert_to_millimeter("km", 4.5) == 4500000
    assert convert_to_millimeter("in", 24) == 609.6
    assert convert_to_millimeter("ft", 7) == 2133.6
    assert convert_to_millimeter("yd", 1.3) == 1188.72
    assert convert_to_millimeter("mi", 2) == 3218688

def test_convert_to_centimeter():
    assert convert_to_centimeter("mm", 30) == 3
    assert convert_to_centimeter("m", 3) == 300
    assert convert_to_centimeter("km", 4.5) == 450000
    assert convert_to_centimeter("in", 27) == 68.58
    assert convert_to_centimeter("ft", 9) == 274.32
    assert convert_to_centimeter("yd", 1.2) == 109.728
    assert convert_to_centimeter("mi", 1.8) == 289681.92


def test_convert_to_meter():
    assert convert_to_meter("mm", 180) == 0.18
    assert convert_to_meter("cm", 70) == 0.7
    assert convert_to_meter("km", 180) == 180000
    assert convert_to_meter("in", 15.6) == 0.39624
    assert convert_to_meter("ft", 15) == 4.572
    assert convert_to_meter("yd", 40) == 36.576
    assert convert_to_meter("mi", 70) == 112,654.08

def test_convert_to_kilometer():
    assert convert_to_kilometer("mm", 700) == 0.0007
    assert convert_to_kilometer("cm", 5600) == 0.056
    assert convert_to_kilometer("m", 1400) == 1.4
    assert convert_to_kilometer("in", 100) == 0.00254
    assert convert_to_kilometer("ft", 40000) == 12.19200
    assert convert_to_kilometer("yd", 40) == 0.03658
    assert convert_to_kilometer("mi", 60) == 96.56064