from config.rules_config import RULES


def _parse_rule(rule: str):
    """
    Convert rule string into structured form.
    """
    rule = rule.replace("IF ", "").replace(" THEN ", "|")
    condition_part, output_part = rule.split("|")

    conditions = []
    for cond in condition_part.split(" AND "):
        var, _, val = cond.split()
        conditions.append((var, val))

    _, _, output_set = output_part.split()

    return conditions, output_set

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
    fired_rules = []

    for rule in RULES:
        conditions, output_set = _parse_rule(rule)

        # Evaluate rule strength using AND = min
        strengths = []
        for var, val in conditions:
            strengths.append(memberships[var][val])

        rule_strength = min(strengths)

        fired_rules.append({
            "output_set": output_set,
            "strength": rule_strength
        })

    return fired_rules