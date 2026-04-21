from utils.validators   import validate_inputs
from utils.logging_utils import log
from src.fuzzification  import fuzzify
from src.rule_base      import apply_rules
from src.inference      import infer
from src.aggregation    import aggregate
from src.defuzzification import defuzzify
from config.variables    import PRIORITY_LABELS


def _score_to_label(score: float) -> str:
    """Map crisp score to priority label using thresholds in config."""
    for label, (lo, hi) in PRIORITY_LABELS.items():
        if lo <= score < hi:
            return label
    return "High"  # score == 100 edge case


def run_priority_system(urgency: float, impact: float,
                        effort: float, risk: float) -> tuple[float, str]:
    """
    Orchestrate full fuzzy priority pipeline.

    Pipeline (replace each step with real fuzzy logic):
        1. fuzzify      → crisp inputs → fuzzy memberships
        2. apply_rules  → memberships  → fired rule strengths
        3. infer        → fired rules  → output fuzzy sets
        4. aggregate    → output sets  → combined fuzzy set
        5. defuzzify    → fuzzy set    → crisp score

    Returns:
        (score: float [0–100], label: str Low|Medium|High)
    """
    log(f"Input received: urgency={urgency}, impact={impact}, "
        f"effort={effort}, risk={risk}")

    # Validate
    validate_inputs(urgency, impact, effort, risk)

    # Step 1: Fuzzification
    inputs = {"urgency": urgency, "impact": impact,
              "effort": effort, "risk": risk}
    memberships = fuzzify(inputs)
    log(f"Fuzzification done: {memberships}")

    # Step 2: Rule base
    fired_rules = apply_rules(memberships)
    log(f"Rules fired: {fired_rules}")

    # Step 3: Inference
    inferred = infer(fired_rules)
    log(f"Inference done: {inferred}")

    # Step 4: Aggregation
    aggregated = aggregate(inferred)
    log(f"Aggregation done: {aggregated}")

    # Step 5: Defuzzification
    score = defuzzify(aggregated)
    log(f"Defuzzified score: {score}")

    # TODO: Replace score with real defuzzified crisp value
    # Current score is dummy. Real pipeline replaces all steps above.
    label = _score_to_label(score)

    log(f"Final result: score={score}, label={label}")
    return score, label