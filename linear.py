#LINEAR REGRESSION USING PYTHON



from sklearn import linear_model

x_train=input_variables_values_training_datasets
y_train=target_variables_values_training_datasets
x_test=input_variables_values_test_datasets

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
linear.score(x_train, y_train)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predicted= linear.predict(x_test)