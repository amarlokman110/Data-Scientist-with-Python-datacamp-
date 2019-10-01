# Variables you want to make predictor insight graph tables for
variables = ["income","gender","disc_mean_gift","disc_time_since_last_gift"]

# Loop through the variables
for variable in variables: 
    
    # Create the predictor insight graph table
    pig_table = create_pig_table(basetable, "target", variable)
    
    # Plot the predictor insight graph
    plot_pig(pig_table, variable)
