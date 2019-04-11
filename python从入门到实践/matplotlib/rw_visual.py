# coding=utf-8
import matplotlib.pyplot as plt

from random_walk import RandomWork

while True:
    rw = RandomWork(5000)
    rw.fill_walk()
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    plt.scatter(0, 0, s=100, edgecolors='none', c='green')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = raw_input("Make another wakl?(y/n):")
    if keep_running == 'n':
        break
