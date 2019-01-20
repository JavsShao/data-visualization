import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# 设置图标标题并给坐标轴定标签
plt.title('Square Nubmers', fontsize=24)
plt.xlabel('xvalue', fontsize=14)
plt.ylabel('yvalue', fontsize=14)

plt.show()