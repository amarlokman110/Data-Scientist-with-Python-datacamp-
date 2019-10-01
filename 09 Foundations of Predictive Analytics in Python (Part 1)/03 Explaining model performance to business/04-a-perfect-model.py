# Generate perfect predictions
perfect_predictions = [(1-target , target) for target in targets_test["target"]]

# Plot the lift curve
skplt.metrics.plot_lift_curve(targets_test, perfect_predictions)
plt.show()
