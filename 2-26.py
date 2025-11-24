import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置支持中文的字体
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

# 焊接强度数据
data = np.array([
    5408, 5431, 5475, 5442, 5376, 5388, 5459, 5422, 5416, 5435,
    5420, 5429, 5401, 5446, 5487, 5416, 5382, 5357, 5388, 5457,
    5407, 5469, 5416, 5377, 5454, 5375, 5409, 5459, 5445, 5429,
    5463, 5408, 5481, 5453, 5422, 5354, 5421, 5406, 5444, 5466,
    5399, 5391, 5477, 5447, 5329, 5473, 5423, 5441, 5412, 5384,
    5445, 5436, 5454, 5453, 5428, 5418, 5465, 5427, 5421, 5396,
    5381, 5425, 5388, 5388, 5378, 5481, 5387, 5440, 5482, 5406,
    5401, 5411, 5399, 5431, 5440, 5413, 5406, 5342, 5452, 5420,
    5458, 5485, 5431, 5416, 5431, 5390, 5399, 5435, 5387, 5462,
    5383, 5401, 5407, 5385, 5440, 5422, 5448, 5366, 5430, 5418
])

# (a) 使用 8 个区间
plt.figure(figsize=(12, 10))

# 绘制直方图 (8 bins)
plt.subplot(2, 2, 1)
plt.hist(data, bins=8, color='skyblue', edgecolor='black')
plt.title('焊接强度直方图 (8个区间)', fontproperties=font)
plt.xlabel('焊接强度', fontproperties=font)
plt.ylabel('频率', fontproperties=font)

# 绘制累积频率图 (8 bins)
plt.subplot(2, 2, 2)
plt.hist(data, bins=8, cumulative=True, color='lightgreen', edgecolor='black')
plt.title('焊接强度累积频率图 (8个区间)', fontproperties=font)
plt.xlabel('焊接强度', fontproperties=font)
plt.ylabel('累积频率', fontproperties=font)

# (b) 使用 16 个区间
# 绘制直方图 (16 bins)
plt.subplot(2, 2, 3)
plt.hist(data, bins=16, color='salmon', edgecolor='black')
plt.title('焊接强度直方图 (16个区间)', fontproperties=font)
plt.xlabel('焊接强度', fontproperties=font)
plt.ylabel('频率', fontproperties=font)

# 绘制累积频率图 (16 bins)
plt.subplot(2, 2, 4)
plt.hist(data, bins=16, cumulative=True, color='gold', edgecolor='black')
plt.title('焊接强度累积频率图 (16个区间)', fontproperties=font)
plt.xlabel('焊接强度', fontproperties=font)
plt.ylabel('累积频率', fontproperties=font)

plt.savefig(
    '2-26.png',                            # 指定输出的 PNG 文件名
    dpi=2000,                                     # 设置分辨率为 300 dpi
    bbox_inches='tight'                          # 紧缩边界以减少多余空白
)
plt.tight_layout()
plt.show()


