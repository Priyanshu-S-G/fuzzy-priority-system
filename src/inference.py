def infer(fired_rules: list) -> dict:
    """
    Combine fired rules into aggregated fuzzy output sets.

    Intended behavior:
        For each output fuzzy set, take max activation strength
        across all rules that fired for that set (Mamdani inference).

    Args:
        fired_rules: list of dicts from apply_rules()

    Returns:
        dict of output set → peak activation strength
        e.g. {"low": 0.2, "medium": 0.5, "high": 0.3}
    """
    inferred = {}
    for rule in fired_rules:
        s = rule["output_set"]
        inferred[s] = max(inferred.get(s, 0), rule["strength"])
    return inferred  # structure correct; values are dummy