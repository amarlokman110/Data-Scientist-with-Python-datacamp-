# Import the modules
import random
import matplotlib.pyplot as plt
import scikitplot as skplt

# Generate random predictions
random_predictions = [random.uniform(0,1) for _ in range(len(targets_test))]

# Adjust random_predictions
random_predictions = [(r,1-r) for r in random_predictions]

# Plot the cumulative gains graph
skplt.metrics.plot_cumulative_gain(targets_test, random_predictions)
plt.show()
