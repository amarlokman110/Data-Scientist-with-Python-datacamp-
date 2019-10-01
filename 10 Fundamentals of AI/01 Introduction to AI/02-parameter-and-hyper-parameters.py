# Define the model
model = LogisticRegression(C=0.000001)
model = LogisticRegression(C=0.0001)
model = LogisticRegression(C=0.01)
model = LogisticRegression(C=100)

# Lower values of C make the model more conservative and resilient to noise,
# while higher values give it more flexibility and capacity to capture the
# nuances. If you increase it too much, you risk overfitting.

# Fit the model
model.fit(training_inputs, training_labels)

# Check model performance
check_performance(model, testing_inputs, testing_labels)
