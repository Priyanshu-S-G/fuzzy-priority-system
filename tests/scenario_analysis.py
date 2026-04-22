from main import run_priority_system

scenarios = {
    "Critical bug": (9, 9, 3, 7),
    "Minor feature": (3, 4, 6, 2),
    "Security risk": (7, 8, 5, 9),
}

for name, vals in scenarios.items():
    score, label = run_priority_system(*vals)
    print(f"{name}: {score} → {label}")