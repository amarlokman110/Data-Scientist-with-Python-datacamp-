# Fit a logistic regression model
from sklearn import linear_model
X = basetable[["age","gender_F","time_since_last_gift"]]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)

# Create a dataframe new_data from current_data that has only the relevant predictors 
new_data = current_data[["age","gender_F","time_since_last_gift"]]

# Make a prediction for each observation in new_data and assign it to predictions
predictions = logreg.predict_proba(new_data)
print(predictions[0:5])
