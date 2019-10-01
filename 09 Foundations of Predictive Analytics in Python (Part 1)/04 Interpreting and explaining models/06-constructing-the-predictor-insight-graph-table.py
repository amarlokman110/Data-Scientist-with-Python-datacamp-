# Function that creates predictor insight graph table
def create_pig_table(basetable, target, variable):

  	# Create groups for each variable
    groups = basetable[[target,variable]].groupby(variable)
    
    # Calculate size and target incidence for each group
    pig_table = groups[target].agg({'Incidence' : np.mean, 'Size' : np.size}).reset_index()

    # Return the predictor insight graph table
    return pig_table

# Calculate the predictor insight graph table for the variable gender
pig_table_gender = create_pig_table(basetable, "target","gender")

# Print the result
print(pig_table_gender)
