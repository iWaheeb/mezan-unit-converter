from src import temperature_converter


def test_convert_from_celsius():
    assert temperature_converter.convert_from_celsius("c_to_f", 50) == 122
    assert temperature_converter.convert_from_celsius("c_to_k", 120) == 393.15


def test_convert_from_fahrenheit():
    assert temperature_converter.convert_from_fahrenheit("f_to_c", 50) == 10
    assert temperature_converter.convert_from_fahrenheit("f_to_k", 150) == 338.705556


def test_convert_from_kelvin():
    assert temperature_converter.convert_from_kelvin("k_to_c", 100) == -173.15
    assert temperature_converter.convert_from_kelvin("k_to_f", 70) == -333.67
