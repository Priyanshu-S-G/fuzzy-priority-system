# Rule definitions as human-readable strings
# Replace with structured rule objects when building inference engine

RULES = [
    "IF urgency IS high AND impact IS high THEN priority IS high",
    "IF urgency IS low AND effort IS high THEN priority IS low",
    "IF risk IS high AND impact IS medium THEN priority IS high",
    "IF urgency IS medium AND impact IS medium THEN priority IS medium",
    "IF effort IS low AND impact IS high THEN priority IS high",
    "IF risk IS low AND urgency IS low THEN priority IS low",
    # TODO: expand rule base to cover all input combinations
]