def validate_inputs(urgency, impact, effort, risk) -> None:
    """
    Validate all inputs are numeric and within [0, 10].

    Raises:
        ValueError if any input out of range or wrong type.
    """
    values = {"urgency": urgency, "impact": impact, "effort": effort, "risk": risk}
    for name, val in values.items():
        if not isinstance(val, (int, float)):
            raise ValueError(f"{name} must be numeric, got {type(val)}")
        if not (0 <= val <= 10):
            raise ValueError(f"{name} must be in [0, 10], got {val}")