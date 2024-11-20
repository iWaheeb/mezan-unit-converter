def convert_from_milligram(operation: str, mg: float):
    mg_formulas = {
        "mg_to_g": mg * 0.001,
        "mg_to_kg": mg * 0.000001,
        "mg_to_oz": mg * 0.0000352739619,
        "mg_to_lb": mg * 0.00000220462262,
    }
    return round(mg_formulas[operation], 10)


def convert_from_gram(operation: str, g: float):
    g_formulas = {
        "g_to_mg": g * 1000,
        "g_to_kg": g * 0.001,
        "g_to_oz": g * 0.0352739619,
        "g_to_lb": g * 0.00220462262,
    }
    return round(g_formulas[operation], 10)


def convert_from_kilogram(operation: str, kg: float):
    kg_formulas = {
        "kg_to_mg": kg * 1000000,
        "kg_to_g": kg * 1000,
        "kg_to_oz": kg * 35.2739619,
        "kg_to_lb": kg * 2.20462262,
    }
    return round(kg_formulas[operation], 10)


def convert_from_ounce(operation: str, oz: float):
    oz_formulas = {
        "oz_to_mg": oz * 28349.5231,
        "oz_to_g": oz * 28.349523,
        "oz_to_kg": oz * 0.0283495231,
        "oz_to_lb": oz * 0.0625,
    }
    return round(oz_formulas[operation], 10)


def convert_from_pound(operation: str, lb: float):
    lb_formulas = {
        "lb_to_mg": lb * 453592.37,
        "lb_to_g": lb * 453.59237,
        "lb_to_kg": lb * 0.45359237,
        "lb_to_oz": lb * 16,
    }
    return round(lb_formulas[operation], 10)
