def fuzzify(inputs: dict) -> dict:
    """
    Convert crisp input values into fuzzy membership degrees.

    Intended behavior:
        For each input variable (urgency, impact, effort, risk),
        compute degree of membership across fuzzy sets (low, medium, high)
        using membership functions defined in config/membership_functions.py.

    Args:
        inputs: dict with keys urgency, impact, effort, risk (float 0–10)

    Returns:
        dict of membership degrees per variable per fuzzy set
        e.g. {"urgency": {"low": 0.2, "medium": 0.7, "high": 0.1}, ...}
    """
    # TODO: Replace dummy output with real membership function calls
    memberships = {}
    for var, val in inputs.items():
        memberships[var] = {
            "low":    0.3,  # dummy
            "medium": 0.5,  # dummy
            "high":   0.2,  # dummy
        }
    return memberships