from src import length_converter


def test_convert_from_millimeter():
    assert length_converter.convert_from_millimeter("mm_to_cm", 15) == 1.5
    assert length_converter.convert_from_millimeter("mm_to_m", 3) == 0.003
    assert length_converter.convert_from_millimeter("mm_to_km", 4.5) == 0.0000045
    assert length_converter.convert_from_millimeter("mm_to_in", 24) == 0.9448818898
    assert length_converter.convert_from_millimeter("mm_to_ft", 7) == 0.0229658793
    assert length_converter.convert_from_millimeter("mm_to_yd", 1.3) == 0.0014216973
    assert length_converter.convert_from_millimeter("mm_to_mi", 2) == 0.0000012427


def test_convert_from_centimeter():
    assert length_converter.convert_from_centimeter("cm_to_mm", 30) == 300
    assert length_converter.convert_from_centimeter("cm_to_m", 3) == 0.03
    assert length_converter.convert_from_centimeter("cm_to_km", 4.5) == 0.000045
    assert length_converter.convert_from_centimeter("cm_to_in", 27) == 10.6299212598
    assert length_converter.convert_from_centimeter("cm_to_ft", 9) == 0.2952755906
    assert length_converter.convert_from_centimeter("cm_to_yd", 1.2) == 0.0131233596
    assert length_converter.convert_from_centimeter("cm_to_mi", 1.8) == 0.0000111847


def test_convert_from_meter():
    assert length_converter.convert_from_meter("m_to_mm", 180) == 180000
    assert length_converter.convert_from_meter("m_to_cm", 70) == 7000
    assert length_converter.convert_from_meter("m_to_km", 180) == 0.18
    assert length_converter.convert_from_meter("m_to_in", 15.6) == 614.17322772
    assert length_converter.convert_from_meter("m_to_ft", 15) == 49.2125985
    assert length_converter.convert_from_meter("m_to_yd", 40) == 43.744532
    assert length_converter.convert_from_meter("m_to_mi", 70) == 0.0434959834


def test_convert_from_kilometer():
    assert length_converter.convert_from_kilometer("km_to_mm", 700) == 700000000
    assert length_converter.convert_from_kilometer("km_to_cm", 5600) == 560000000
    assert length_converter.convert_from_kilometer("km_to_m", 1400) == 1400000
    assert length_converter.convert_from_kilometer("km_to_in", 100) == 3937007.87
    assert length_converter.convert_from_kilometer("km_to_ft", 40000) == 131233596
    assert length_converter.convert_from_kilometer("km_to_yd", 40) == 43744.532
    assert length_converter.convert_from_kilometer("km_to_mi", 60) == 37.28227152


def test_convert_from_inch():
    assert length_converter.convert_from_inch("in_to_mm", 750) == 19050
    assert length_converter.convert_from_inch("in_to_cm", 150) == 381
    assert length_converter.convert_from_inch("in_to_m", 4) == 0.1016
    assert length_converter.convert_from_inch("in_to_km", 1.45) == 0.0000368300
    assert length_converter.convert_from_inch("in_to_ft", 40) == 3.333333332
    assert length_converter.convert_from_inch("in_to_yd", 5) == 0.138888889
    assert length_converter.convert_from_inch("in_to_mi", 0.75) == 0.0000118371


def test_convert_from_foot():
    assert length_converter.convert_from_foot("ft_to_mm", 750) == 228600
    assert length_converter.convert_from_foot("ft_to_cm", 150) == 4572
    assert length_converter.convert_from_foot("ft_to_m", 4) == 1.2192
    assert length_converter.convert_from_foot("ft_to_km", 1.45) == 0.00044196
    assert length_converter.convert_from_foot("ft_to_in", 40) == 480
    assert length_converter.convert_from_foot("ft_to_yd", 5) == 1.666666665
    assert length_converter.convert_from_foot("ft_to_mi", 0.75) == 0.0001420455


def test_convert_from_yard():
    assert length_converter.convert_from_yard("yd_to_mm", 950) == 868680
    assert length_converter.convert_from_yard("yd_to_cm", 410) == 37490.4
    assert length_converter.convert_from_yard("yd_to_m", 5) == 4.57200
    assert length_converter.convert_from_yard("yd_to_km", 1.5) == 0.0013716
    assert length_converter.convert_from_yard("yd_to_in", 30) == 1080
    assert length_converter.convert_from_yard("yd_to_ft", 7) == 21
    assert length_converter.convert_from_yard("yd_to_mi", 1.5) == 0.0008522727


def test_convert_from_mile():
    assert length_converter.convert_from_mile("mi_to_mm", 950) == 1528876800
    assert length_converter.convert_from_mile("mi_to_cm", 600) == 96560640
    assert length_converter.convert_from_mile("mi_to_m", 5) == 8046.72
    assert length_converter.convert_from_mile("mi_to_km", 90) == 144.84096
    assert length_converter.convert_from_mile("mi_to_in", 120) == 7603200
    assert length_converter.convert_from_mile("mi_to_ft", 400) == 2112000
    assert length_converter.convert_from_mile("mi_to_yd", 500) == 880000
