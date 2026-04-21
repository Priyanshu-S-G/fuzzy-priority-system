def apply_rules(memberships: dict) -> list:
    """
    Apply fuzzy IF-THEN rules to fuzzified inputs.

    Intended behavior:
        Evaluate each rule from config/rules_config.py against membership
        degrees. Use AND = min(), OR = max() for rule antecedents.
        Return list of (output_set, activation_strength) tuples.

    Args:
        memberships: dict from fuzzify()

    Returns:
        list of dicts: [{"output_set": "high", "strength": 0.7}, ...]
    """
    # TODO: Replace with real rule evaluation logic
    dummy_fired_rules = [
        {"output_set": "low",    "strength": 0.2},
        {"output_set": "medium", "strength": 0.5},
        {"output_set": "high",   "strength": 0.3},
    ]
    return dummy_fired_rules