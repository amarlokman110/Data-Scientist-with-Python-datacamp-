# Create the list of variables for our predictor insight graph tables
variables = ["income","gender","disc_mean_gift","disc_time_since_last_gift"]

# Create an empty dictionary
pig_tables = {}

# Loop through the variables
for variable in variables:
  
    # Create a predictor insight graph table
    pig_table = create_pig_table(basetable, "target", variable)
    
    # Add the table to the dictionary
    pig_tables[variable] = pig_table

# Print the predictor insight graph table of the variable "disc_time_since_last_gift"
print(pig_tables["disc_time_since_last_gift"])
