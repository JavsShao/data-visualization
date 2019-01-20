import matplotlib.pyplot as plt


plt.scatter(2, 4, s=200)

# 设置图标标题并给坐标加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('xValue', fontsize=14)
plt.ylabel('yValue', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()