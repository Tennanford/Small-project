import numpy as np
import matplotlib.pyplot as plt
#10 100 500 1000 10000 50000
# 数据准备
N = 6
pigeon = (68, 64, 68, 74, 70,70)
hawk = (32, 36, 32, 26, 30,30)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

# 绘制柱形图
fig, ax = plt.subplots()
p1 = ax.bar(ind, pigeon, width)
p2 = ax.bar(ind, hawk, width, bottom=pigeon)

# 设置图表信息
ax.set_ylabel('individual number')
ax.set_title('yingge1')
ax.set_xticks(ind, ('10', '100', '500', '1000', '10000','50000'))
ax.set_yticks(np.arange(0, 101, 10))
ax.legend((p1[0], p2[0]), ('pigeon', 'hawk'))

# 显示图表
plt.show()
