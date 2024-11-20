from src import weight_converter


def test_convert_from_milligram():
    assert weight_converter.convert_from_milligram("mg_to_g", 7.5) == 0.0075
    assert weight_converter.convert_from_milligram("mg_to_kg", 0.5) == 0.0000005
    assert weight_converter.convert_from_milligram("mg_to_oz", 0.7) == 0.0000246918
    assert weight_converter.convert_from_milligram("mg_to_lb", 3) == 0.0000066139


def test_convert_from_gram():
    assert weight_converter.convert_from_gram("g_to_mg", 1200) == 1200000
    assert weight_converter.convert_from_gram("g_to_kg", 11.5) == 0.0115
    assert weight_converter.convert_from_gram("g_to_oz", 15) == 0.5291094285
    assert weight_converter.convert_from_gram("g_to_lb", 40) == 0.0881849048


def test_convert_from_kilogram():
    assert weight_converter.convert_from_kilogram("kg_to_mg", 17000) == 17000000000
    assert weight_converter.convert_from_kilogram("kg_to_g", 1200) == 1200000
    assert weight_converter.convert_from_kilogram("kg_to_oz", 50) == 1763.698095
    assert weight_converter.convert_from_kilogram("kg_to_lb", 140) == 308.6471668


def test_convert_from_ounce():
    assert weight_converter.convert_from_ounce("oz_to_mg", 750) == 21262142.325
    assert weight_converter.convert_from_ounce("oz_to_g", 140) == 3968.93322
    assert weight_converter.convert_from_ounce("oz_to_kg", 17) == 0.4819418927
    assert weight_converter.convert_from_ounce("oz_to_lb", 200) == 12.5


def test_convert_from_pound():
    assert weight_converter.convert_from_pound("lb_to_mg", 1600) == 725747792
    assert weight_converter.convert_from_pound("lb_to_g", 860) == 390089.4382
    assert weight_converter.convert_from_pound("lb_to_kg", 45) == 20.41165665
    assert weight_converter.convert_from_pound("lb_to_oz", 500) == 8000
