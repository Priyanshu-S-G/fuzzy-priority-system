class OutputModel:
    def __init__(self, score, label):
        self.score = score
        self.label = label

    def explain(self):
        return f"Priority is {self.label} with score {self.score}"