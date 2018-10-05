#SUPPORT VECTOR MACHINE



from sklearn import svm

model = svm.svc() 

model.fit(X, y)
model.score(X, y)

predicted= model.predict(x_test)