from sklearn.naive_bayes import GaussianNB



gnb = GaussianNB()
 gnb.fit(iris.data, iris.target)
y_pred =.predict(iris.data)