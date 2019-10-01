# Inspect the predictor insight graph table of Country
print(pig_table)

# Print the number of UK donors
print(pig_table["Size"][pig_table["Country"]=="UK"])

# Check the target incidence of USA and India donors
print(pig_table["Incidence"][pig_table["Country"]=="USA"])
print(pig_table["Incidence"][pig_table["Country"]=="India"])
