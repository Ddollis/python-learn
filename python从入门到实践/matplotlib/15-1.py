# coding=utf-8
import matplotlib.pyplot as plt

x_values = list(range(5001))
y_values = [x ** 3 for x in x_values]
plt.scatter(x_values, y_values, s=30, c='blue', edgecolors='none')
plt.title('lifangtu', fontsize=24)
plt.xlabel('x de zuo biao', fontsize=14)
plt.ylabel('y de zuo biao', fontsize=14)

plt.show()
