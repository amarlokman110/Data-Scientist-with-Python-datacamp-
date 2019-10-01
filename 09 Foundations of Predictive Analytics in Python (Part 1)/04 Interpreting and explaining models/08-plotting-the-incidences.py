import matplotlib.pyplot as plt
import numpy as np

# The function to plot a predictor insight graph.
def plot_incidence(pig_table,variable):
    
    # Plot the incidence line
    pig_table["Incidence"].plot()
    
    # Formatting the predictor insight graph
    plt.xticks(np.arange(len(pig_table)), pig_table[variable])
    plt.xlim([-0.5, len(pig_table) - 0.5])
    plt.ylim([0, max(pig_table["Incidence"] * 2)])
    plt.ylabel("Incidence", rotation=0, rotation_mode="anchor", ha="right")
    plt.xlabel(variable)
    
    # Show the graph
    plt.show()

# Apply the function for the variable "country".
plot_incidence(pig_table, "country")
