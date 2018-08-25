import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import matplotlib as mpl


iris = load_iris()
print(type(iris.data))
data = pd.DataFrame(iris.data)

data.columns = iris.feature_names
print(type(iris.feature_names))

data['Species'] = iris.target

x = data.iloc[:, :2]
y = data.iloc[:, -1]
#print(x)
print(y)


x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75, random_state=42)
print(type(x_train))


#criterion：计算纯度的方法,这里使用的ID3.0算法
tree_clf = DecisionTreeClassifier(max_depth=4, criterion='entropy')
tree_clf.fit(x_train, y_train)
y_test_hat = tree_clf.predict(x_test)
print("acc score:", accuracy_score(y_test, y_test_hat))




depth = np.arange(1, 15)
err_list = []
for d in depth:
    tree_clf = DecisionTreeClassifier(max_depth=d, criterion='entropy')
    tree_clf.fit(x_train, y_train)
    y_test_hat = tree_clf.predict(x_test)
    result = (y_test_hat == y_test)
    if d == 1:
        print(result)
    err = 1 - np.mean(result)
    print(100 * err)
    err_list.append(err)
    print(d, '错误率： %.2f' % (100 * err))



plt.figure(facecolor='w')
plt.plot(depth, err_list, 'ro-', lw=2)
plt.xlabel("决策树的深度", fontsize=15)
plt.ylabel("错误率", fontsize=15)
plt.grid(True)

plt.show()






