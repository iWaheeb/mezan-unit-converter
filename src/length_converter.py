def convert_from_millimeter(operation: str, mm: float):
    mm_formulas = {
        "mm_to_cm": mm * (1 / 10),
        "mm_to_m": mm * (1 / 1000),
        "mm_to_km": mm * (1 / 1000000),
        "mm_to_in": mm * (1 / 25.4),
        "mm_to_ft": mm * (1 / 304.8),
        "mm_to_yd": mm * (1 / 914.4),
        "mm_to_mi": mm * (1 / 1609344),
    }

    return round(mm_formulas[operation], 10)


def convert_from_centimeter(operation: str, cm: float):
    cm_formulas = {
        "cm_to_mm": cm * 10,
        "cm_to_m": cm * (1 / 100),
        "cm_to_km": cm * (1 / 100000),
        "cm_to_in": cm * (1 / 2.54),
        "cm_to_ft": cm * (1 / 30.48),
        "cm_to_yd": cm * (1 / 91.44),
        "cm_to_mi": cm * (1 / 160934.4),
    }

    return round(cm_formulas[operation], 10)


def convert_from_meter(operation: str, m: float):
    m_formulas = {
        "m_to_mm": m * 1000,
        "m_to_cm": m * 100,
        "m_to_km": m * 0.001,
        "m_to_in": m * 39.3700787,
        "m_to_ft": m * 3.2808399,
        "m_to_yd": m * 1.0936133,
        "m_to_mi": m * 0.000621371192,
    }

    return round(m_formulas[operation], 10)


def convert_from_kilometer(operation: str, km: float):
    km_formulas = {
        "km_to_mm": km * 1000000,
        "km_to_cm": km * 100000,
        "km_to_m": km * 1000,
        "km_to_in": km * 39370.0787,
        "km_to_ft": km * 3280.8399,
        "km_to_yd": km * 1093.6133,
        "km_to_mi": km * 0.621371192,
    }

    return round(km_formulas[operation], 9)


def convert_from_inch(operation: str, inch: float):
    in_formulas = {
        "in_to_mm": inch * 25.4,
        "in_to_cm": inch * 2.54,
        "in_to_m": inch * 0.0254,
        "in_to_km": inch * 0.0000254,
        "in_to_ft": inch * 0.0833333333,
        "in_to_yd": inch * 0.0277777778,
        "in_to_mi": inch * 0.0000157828283,
    }

    return round(in_formulas[operation], 10)


def convert_from_foot(operation: str, ft: float):
    ft_formulas = {
        "ft_to_mm": ft * 304.8,
        "ft_to_cm": ft * 30.48,
        "ft_to_m": ft * 0.3048,
        "ft_to_km": ft * 0.0003048,
        "ft_to_in": ft * 12,
        "ft_to_yd": ft * 0.333333333,
        "ft_to_mi": ft * 0.000189393939,
    }

    return round(ft_formulas[operation], 10)


def convert_from_yard(operation: str, yd: float):
    yd_formulas = {
        "yd_to_mm": yd * 914.4,
        "yd_to_cm": yd * 91.44,
        "yd_to_m": yd * 0.9144,
        "yd_to_km": yd * 0.0009144,
        "yd_to_in": yd * 36,
        "yd_to_ft": yd * 3,
        "yd_to_mi": yd * 0.000568181818,
    }

    return round(yd_formulas[operation], 10)


def convert_from_mile(operation: str, mi: float):
    mi_formulas = {
        "mi_to_mm": mi * 1609344,
        "mi_to_cm": mi * 160934.4,
        "mi_to_m": mi * 1609.344,
        "mi_to_km": mi * 1.609344,
        "mi_to_in": mi * 63360,
        "mi_to_ft": mi * 5280,
        "mi_to_yd": mi * 1760,
    }

    return round(mi_formulas[operation], 10)
