# Print the columns in the original basetable
print(basetable.columns)

# Get all the variable names except "target"
variables = list(basetable.columns)
variables.remove("target")

# Loop through all the variables and discretize in 10 bins if there are more than 5 different values
for variable in variables:
    if len(basetable.groupby(variable))>5:
        new_variable = "disc_" + variable
        basetable[new_variable] = pd.qcut(basetable[variable], 10)
        
# Print the columns in the new basetable
print(basetable.columns)
