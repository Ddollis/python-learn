# coding=utf-8
import numpy as np
from sklearn import neighbors

knn = neighbors.KNeighborsClassifier()  # 取得 knn 分类器
# data 对应打斗次数和接吻次数
data = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
labels = np.array([1, 1, 1, 2, 2, 2])  # 对应 Romance 和 Action
knn.fit(data, labels)  # 导入数据进行训练
print knn.predict([[18, 90]])
