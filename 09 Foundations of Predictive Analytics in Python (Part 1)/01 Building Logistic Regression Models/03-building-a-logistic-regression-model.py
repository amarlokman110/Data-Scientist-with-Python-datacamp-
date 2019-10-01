# Import linear_model from sklearn.
from sklearn import linear_model

# Create a dataframe X that only contains the candidate predictors age, gender_F and time_since_last_gift.
X = basetable[["age","gender_F","time_since_last_gift"]]

# Create a dataframe y that contains the target.
y = basetable[["target"]]

# Create a logistic regression model logreg and fit it to the data.
logreg = linear_model.LogisticRegression()
logreg.fit(X,y)
