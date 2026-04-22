# Fuzzy Priority Allocation System

A fuzzy logic-based decision system that determines task priority using four key factors: urgency, impact, effort, and risk.

---

## 🚀 Features

* Mamdani fuzzy inference system
* Triangular membership functions
* Rule-based decision logic (interpretable)
* Interactive Gradio web interface
* Color-coded and explainable outputs
* Data-driven threshold calibration

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

Dependencies:

* gradio
* numpy
* matplotlib

---

## ▶️ Running the App

```bash
python app.py
```

Then open the local URL shown in the terminal.

---

## 🧪 Example

**Input:**

```
Urgency = 9
Impact  = 8
Effort  = 3
Risk    = 7
```

**Output:**

```
Score ≈ 75
Label = High
```

---

## 🧠 How It Works

1. **Fuzzification**

   * Converts crisp inputs into fuzzy membership values (low, medium, high)

2. **Rule Evaluation**

   * Applies IF-THEN rules using logical operators (AND = min, OR = max)

3. **Inference**

   * Combines rule outputs using Mamdani max aggregation

4. **Defuzzification**

   * Converts fuzzy result into a crisp score using weighted average

5. **Label Mapping**

   * Maps score to priority levels:

     * Low (0–30)
     * Medium (30–65)
     * High (65–100)

---

## 🏗️ Project Structure

```
config/      → rules, variables, membership functions
src/         → fuzzy logic pipeline (core system)
utils/       → validation and logging
main.py      → orchestrates fuzzy pipeline
app.py       → Gradio UI
tests/       → test cases and scenario analysis
```

---

## 🎯 Key Idea

Instead of rigid thresholds, this system uses fuzzy logic to model real-world uncertainty and make smooth, human-like decisions.

---

## 🔮 Future Improvements

* Full centroid defuzzification
* Rule weighting and tuning
* Automatic rule generation
* Visualization of rule activation

---

## 📌 Notes

This project demonstrates how soft computing techniques like fuzzy logic can be applied to real-world decision systems where inputs are uncertain and not strictly binary.
