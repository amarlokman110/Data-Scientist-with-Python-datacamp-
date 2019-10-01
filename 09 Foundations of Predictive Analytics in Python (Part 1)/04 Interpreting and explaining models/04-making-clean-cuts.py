# Discretize the variable 
basetable["disc_number_gift"] = pd.cut(basetable["number_gift"],[0, 5, 10, 20])

# Count the number of observations per group
print(basetable.groupby("disc_number_gift").size())
