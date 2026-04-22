import random
from main import run_priority_system

scores = []

# Generate 200 random test cases
for _ in range(200):
    urgency = random.uniform(0, 10)
    impact  = random.uniform(0, 10)
    effort  = random.uniform(0, 10)
    risk    = random.uniform(0, 10)

    score, _ = run_priority_system(urgency, impact, effort, risk)
    scores.append(score)

# Sort scores
scores.sort()

# Print key stats
print("Min:", min(scores))
print("Max:", max(scores))

# Percentiles
def percentile(p):
    idx = int(len(scores) * p / 100)
    return scores[idx]

print("25th percentile:", percentile(25))
print("50th percentile (median):", percentile(50))
print("75th percentile:", percentile(75))