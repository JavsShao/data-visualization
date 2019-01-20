import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例, 并将其中包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=125)
    plt.show()

    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break

plt.savefig('给点着色.png', bbox_inches='tight')