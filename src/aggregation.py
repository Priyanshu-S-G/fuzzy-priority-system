def aggregate(inferred: dict) -> dict:
    """
    Aggregate all fuzzy output sets into single output fuzzy set.

    Intended behavior:
        Clip each output membership function at its activation strength,
        then union (max) all clipped sets across the output universe (0–100).
        Result is a combined fuzzy set ready for defuzzification.

    Args:
        inferred: dict from infer()

    Returns:
        dict representing aggregated fuzzy set
        (real impl: array over output universe; here: pass-through dummy)
    """
    # TODO: Replace with real aggregation over output universe [0, 100]
    aggregated = {
        "low":    inferred.get("low",    0.2),
        "medium": inferred.get("medium", 0.5),
        "high":   inferred.get("high",   0.3),
    }
    return aggregated  # dummy pass-through