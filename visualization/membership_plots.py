import numpy as np
import matplotlib.pyplot as plt
from config.membership_functions import low, medium, high

x = np.linspace(0, 10, 100)

low_vals = [low(v, 0, 5) for v in x]
med_vals = [medium(v, 2.5, 5, 7.5) for v in x]
high_vals = [high(v, 5, 10) for v in x]

plt.plot(x, low_vals, label="Low")
plt.plot(x, med_vals, label="Medium")
plt.plot(x, high_vals, label="High")

plt.legend()
plt.title("Membership Functions")
plt.show()