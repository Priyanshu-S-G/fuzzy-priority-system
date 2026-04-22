from main import run_priority_system

TEST_CASES = [
    (9, 9, 2, 8),  # High
    (2, 3, 8, 2),  # Low
    (5, 5, 5, 5),  # Medium
]

for case in TEST_CASES:
    score, label = run_priority_system(*case)
    print(case, "→", score, label)