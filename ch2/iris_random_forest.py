import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import  DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data[:, :2]
y = iris.target

x_trains, x_tests, y_trains, y_tests = train_test_split(X, y, train_size=0.67, random_state=42)

#这里n_jobs 就是并行的线程数，-1代表不限制。
forest_clf = RandomForestClassifier(n_estimators=150, criterion="entropy", max_depth=8, n_jobs=-1)
forest_clf.fit(x_trains, y_trains)

y_tests_hat = forest_clf.predict(x_tests)
print(accuracy_score(y_tests, y_tests_hat))

forestAccList = []
treeAccList = []

xList = range(1, 40)

for forestScale in xList:
    forest_clf = RandomForestClassifier(n_estimators=forestScale, criterion="entropy", max_depth=8)
    forest_clf.fit(x_trains, y_trains)
    y_tests_hat = forest_clf.predict(x_tests)
    forestAccList.append(accuracy_score(y_tests, y_tests_hat))


for forestScale in xList:
    dt_clf = DecisionTreeClassifier(max_depth=8, criterion="entropy")
    dt_clf.fit(x_trains, y_trains)
    y_tests_hat = dt_clf.predict(x_tests)
    treeAccList.append(accuracy_score(y_tests, y_tests_hat))


plt.figure()
plt.plot(xList, forestAccList, 'ro-', lw=2)
plt.plot(xList, treeAccList, 'go-', lw=2)
plt.show()




