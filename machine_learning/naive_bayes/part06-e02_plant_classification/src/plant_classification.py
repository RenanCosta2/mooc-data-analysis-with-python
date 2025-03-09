#!/usr/bin/env python3

# Exercise 6.2 (plant classification)
# Write function plant_classification that does the following:

# loads the iris dataset using sklearn (sklearn.datasets.load_iris)
# splits the data into training and testing part using the train_test_split function so that the training set size is 80% of the whole data (give the call also the random_state=0argument to make the result deterministic)
# use Gaussian naive Bayes to fit the training data
# predict labels of the test data
# the function should return the accuracy score of the prediction performance (sklearn.metrics.accuracy_score)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():

    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

    nb = naive_bayes.GaussianNB()
    nb.fit(X_train, y_train)

    nb_predict = nb.predict(X_test)

    nb_acc = metrics.accuracy_score(y_test, nb_predict)

    return nb_acc

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
