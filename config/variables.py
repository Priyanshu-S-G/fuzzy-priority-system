# Input/output range definitions
# Replace with fuzzy membership boundaries when implementing fuzzy logic

INPUT_RANGES = {
    "urgency": (0, 10),
    "impact":  (0, 10),
    "effort":  (0, 10),
    "risk":    (0, 10),
}

OUTPUT_RANGE = (0, 100)

# Labels mapped to output score thresholds
# Replace thresholds with defuzzified crisp value ranges
PRIORITY_LABELS = {
    "Low":    (0,  40),
    "Medium": (40, 70),
    "High":   (70, 100),
}