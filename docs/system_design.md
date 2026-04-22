# System Design — Fuzzy Priority Allocation System

## 1. Overview
This system implements a fuzzy logic-based decision model to determine task priority.
It evaluates four input factors — urgency, impact, effort, and risk — and produces a priority score and label.

The system uses Mamdani fuzzy inference for interpretability and rule-based reasoning.

---

## 2. Input Variables

| Variable | Description | Range |
|----------|------------|-------|
| Urgency  | How soon the task must be completed | 0–10 |
| Impact   | Importance of the task outcome | 0–10 |
| Effort   | Resources/time required | 0–10 |
| Risk     | Consequences of failure | 0–10 |

---

## 3. Output

- **Priority Score:** 0–100  
- **Priority Label:** Low / Medium / High  

---

## 4. Membership Functions

Triangular membership functions are used for all inputs:

- Low    → (0, 0, 5)  
- Medium → (2.5, 5, 7.5)  
- High   → (5, 10, 10)  

These overlapping functions allow smooth transitions between categories.

---

## 5. Fuzzy Inference Pipeline

The system follows a standard Mamdani fuzzy pipeline:

1. **Fuzzification**  
   Convert crisp inputs into membership degrees.

2. **Rule Evaluation**  
   Apply IF-THEN rules using:
   - AND → min()
   - OR  → max()

3. **Inference**  
   Combine rule outputs using max operator per output set.

4. **Aggregation**  
   Output sets are implicitly aggregated through inference.

5. **Defuzzification**  
   Convert fuzzy output into a crisp score using weighted average.

---

## 6. Defuzzification

Each output set is assigned a representative value:

- Low → 20  
- Medium → 50  
- High → 80  

Final score:

Score = Σ (activation × center) / Σ activation

---

## 7. Threshold Mapping

Priority labels are assigned using:

- Low    → 0–30  
- Medium → 30–65  
- High   → 65–100  

These thresholds were calibrated empirically using output distribution analysis.

---

## 8. Design Decisions

- Mamdani inference chosen for interpretability  
- Triangular membership functions for simplicity  
- Rule-based logic for nonlinear reasoning  
- Override rules added to prevent effort from dominating urgency  
- Simplified aggregation used due to discrete defuzzification  

---

## 9. System Characteristics

- Handles uncertainty and partial truth  
- Produces smooth transitions (no abrupt jumps)  
- Fully explainable (rule-based)  
- Deterministic behavior (no randomness in logic)