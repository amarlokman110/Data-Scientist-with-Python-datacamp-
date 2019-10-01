# Select the income and target columns
basetable_income = basetable[["target","income"]]

# Group basetable_income by income
groups = basetable_income.groupby("income")

# Calculate the target incidence and print the result
incidence = groups["income"].agg({"Incidence" : np.mean()}).reset_index()
print(incidence)
