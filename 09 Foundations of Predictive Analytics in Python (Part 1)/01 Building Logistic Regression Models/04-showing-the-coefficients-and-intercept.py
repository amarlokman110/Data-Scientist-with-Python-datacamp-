# Construct a logistic regression model that predicts the target using age, gender_F and time_since_last gift
predictors = ["age","gender_F","time_since_last_gift"]
X = basetable[predictors]
y = basetable[["target"]]
logreg = linear_model.LogisticRegression()
logreg.fit(X, y)

# Assign the coefficients to a list coef
coef = logreg.coef_
for p,c in zip(predictors,list(coef[0])):
    print(p + '\t' + str(c))
    
# Assign the intercept to the variable intercept
intercept = logreg.intercept_
print(intercept)
