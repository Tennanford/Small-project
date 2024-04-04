from yingge2 import par
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
# 设置中文字体
font = FontProperties(fname='/path/to/your/chinese/font.ttf')
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']
# 创建一个矩阵

# print(par)
par=par[:,3:]
# print(par)
# 计算每行中1的总数
row_sums = np.sum(par, axis=1)
# print(row_sums)
# # 统计具有相同1数目的行数
counter = Counter(row_sums)
for i in range(11):
    if i in counter:
        print("存在",i)
    else:
        counter[i]=0
print(counter)
# 提取横坐标和纵坐标
x = list(counter.keys())
y = list(counter.values())

# 绘制图形
plt.bar(x, y)
plt.xlabel('选择鹰策略的概率（×10%）')
plt.ylabel('个体数')
plt.title('yingge2-50000times')
plt.show()
