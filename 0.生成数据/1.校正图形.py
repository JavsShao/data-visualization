import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5,]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图标标题, 并给坐标轴加上标签
plt.title("Squares values")
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.show()