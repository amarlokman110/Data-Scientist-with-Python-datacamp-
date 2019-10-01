# Assign the number of rows in the basetable to the variable 'population_size'.
population_size  = len(basetable)

# Print the population size.
print(population_size)

# Assign the number of targets to the variable 'targets_count'.
targets_count = sum(basetable["target"])

# Print the number of targets.
print(targets_count)

# Print the target incidence.
print(targets_count/population_size)
