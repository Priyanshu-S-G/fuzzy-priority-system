class InputModel:
    def __init__(self, urgency, impact, effort, risk):
        self.urgency = urgency
        self.impact = impact
        self.effort = effort
        self.risk = risk

    def to_dict(self):
        return {
            "urgency": self.urgency,
            "impact": self.impact,
            "effort": self.effort,
            "risk": self.risk
        }