# Load the partitioning module
from sklearn.cross_validation import train_test_split

# Create dataframes with variables and target
X = basetable.drop('target', 1)
y = basetable["target"]

# Carry out 70-30 partititioning with stratification
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, stratify = y)

# Create the final train and test basetables
train = pd.concat([X_train, y_train], axis=1)
test = pd.concat([X_test, y_test], axis=1)

 # Apply the auc_train_test function
auc_train, auc_test = auc_train_test(["age", "gender_F"], ["target"], train, test)
print(round(auc_train,2))
print(round(auc_test,2))
