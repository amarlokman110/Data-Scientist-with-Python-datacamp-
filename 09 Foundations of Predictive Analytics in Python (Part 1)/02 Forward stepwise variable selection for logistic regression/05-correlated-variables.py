import numpy as np
# Calculate the AUC of the model using min_gift only
auc_min_gift = auc(["min_gift"],["target"],basetable)
print(round(auc_min_gift,2))

# Calculate the AUC of the model using income_high only
auc_income_high = auc(["income_high"],["target"],basetable)
print(round(auc_income_high,2))

# Calculate the correlation between min_gift and mean_gift
correlation = np.corrcoef(basetable["min_gift"], basetable["mean_gift"])[0,1]
print(round(correlation,2))
