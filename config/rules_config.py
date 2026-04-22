# Rule definitions as human-readable strings

RULES = [
    # HIGH priority
    "IF urgency IS high AND impact IS high THEN priority IS high",
    "IF impact IS high AND effort IS low THEN priority IS high",
    "IF urgency IS high AND risk IS high THEN priority IS high",
    "IF impact IS high AND risk IS high THEN priority IS high",

    # MEDIUM priority
    "IF urgency IS medium AND impact IS medium THEN priority IS medium",
    "IF impact IS high AND effort IS medium THEN priority IS medium",
    "IF urgency IS medium AND risk IS medium THEN priority IS medium",

    # OVERRIDE rules
    "IF urgency IS high AND impact IS low THEN priority IS medium",
    "IF urgency IS high AND effort IS high THEN priority IS medium",
    "IF urgency IS high AND risk IS medium THEN priority IS medium",

    # LOW priority
    "IF urgency IS low AND effort IS high THEN priority IS low",
    "IF impact IS low AND effort IS high THEN priority IS low",
    "IF urgency IS low AND risk IS low THEN priority IS low",
    "IF impact IS low AND risk IS low THEN priority IS low",

    # CONTEXT-AWARE rules (3-variable)
    "IF urgency IS high AND impact IS low AND effort IS high THEN priority IS medium",
    "IF urgency IS medium AND impact IS high AND risk IS high THEN priority IS high",
    "IF impact IS low AND effort IS high AND urgency IS medium THEN priority IS medium",
    "IF urgency IS high AND impact IS medium AND risk IS medium THEN priority IS high",
    "IF urgency IS low AND impact IS medium AND effort IS high THEN priority IS low",
]