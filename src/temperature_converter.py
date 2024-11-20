def convert_from_celsius(operation: str, c: float):
    c_formulas = {"c_to_f": c * 1.8 + 32, "c_to_k": c + 273.15}
    return round(c_formulas[operation], 6)


def convert_from_fahrenheit(operation: str, f: float):
    f_formulas = {"f_to_c": (f - 32) / 1.8, "f_to_k": (f - 32) / 1.8 + 273.15}
    return round(f_formulas[operation], 6)


def convert_from_kelvin(operation: str, k: float):
    k_formulas = {"k_to_c": k - 273.15, "k_to_f": 1.8 * (k - 273.15) + 32}
    return round(k_formulas[operation], 6)
