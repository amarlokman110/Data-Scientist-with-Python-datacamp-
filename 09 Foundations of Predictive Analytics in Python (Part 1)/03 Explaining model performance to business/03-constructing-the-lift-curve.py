# Import the matplotlib.pyplot module 
import matplotlib.pyplot as plt

# Import the scikitplot module
import scikitplot as skplt

# Plot the lift curve
skplt.metrics.plot_lift_curve(targets_test, predictions_test)
plt.show()
