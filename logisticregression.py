#LOGISTIC REGRESSION


from sklearn.linear_model import LogisticRegression


model = LogisticRegression()

model.fit(X, y)
model.score(X, y)

print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)

predicted= model.predict(x_test)