# Plot the cumulative gains
skplt.metrics.plot_cumulative_gain(targets_test, predictions_test)
plt.show()

# Number of targets you want to reach
number_targets_toreach = 30000 / 50
perc_targets_toreach = number_targets_toreach / 1000
cumulative_gains = 0.4
number_donors_toreach = cumulative_gains * 10000
