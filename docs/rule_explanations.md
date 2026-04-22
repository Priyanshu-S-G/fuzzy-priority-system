# Rule Base Explanation

## 1. Design Philosophy

The rule base is designed to mimic human decision-making:

- Urgency, impact, and risk increase priority  
- Effort reduces priority  
- Critical factors can override weaker ones  
- Decisions are based on combinations, not single variables  

---

## 2. High Priority Rules

These rules represent critical situations:

- IF urgency IS high AND impact IS high → high  
  → urgent and important tasks must be prioritized  

- IF impact IS high AND risk IS high → high  
  → high consequence scenarios demand attention  

- IF urgency IS high AND risk IS high → high  
  → urgent and risky situations require immediate action  

---

## 3. Medium Priority Rules

These handle balanced or uncertain scenarios:

- IF urgency IS medium AND impact IS medium → medium  
- IF impact IS high AND effort IS medium → medium  
- IF urgency IS medium AND risk IS medium → medium  

These represent tasks that are important but not critical.

---

## 4. Low Priority Rules

Low priority is assigned when:

- Task has low impact  
- Requires high effort  
- Has low urgency and risk  

Examples:

- IF urgency IS low AND effort IS high → low  
- IF impact IS low AND risk IS low → low  

---

## 5. Override Rules (Key Improvement)

Override rules were introduced to fix edge cases where effort suppressed urgency.

Example:

- IF urgency IS high AND impact IS low → medium  
- IF urgency IS high AND effort IS high → medium  

These ensure that urgent tasks are not ignored even if other factors are weak.

---

## 6. Multi-Variable Rules

Additional rules consider three variables simultaneously:

- IF urgency IS high AND impact IS low AND effort IS high → medium  
- IF urgency IS medium AND impact IS high AND risk IS high → high  

These improve context awareness and make decisions more realistic.

---

## 7. Rule Behavior Summary

| Factor   | Effect on Priority |
|----------|------------------|
| Urgency  | Increases priority |
| Impact   | Increases priority |
| Risk     | Increases priority |
| Effort   | Decreases priority |

---

## 8. Key Insight

The system does not rely on fixed weights.  
Instead, it uses rule-based reasoning to capture nonlinear relationships between variables.

This allows more flexible and human-like decision-making.