import matplotlib.pyplot as plt
from collections import defaultdict

# 原始数据
data = [42.4,65.7,29.8,58.7,52.1,55.8,57.0,68.7,67.3,67.3,
        54.3,54.0,73.1,81.3,59.9,56.9,62.2,69.9,66.9,59.0,
        56.3,43.3,57.4,45.3,80.1,49.7,42.8,42.4,59.6,65.8,
        61.4,64.0,64.2,72.6,72.5,46.1,53.1,56.1,67.2,70.7,
        42.6,77.4,54.7,57.1,77.3,39.3,76.4,59.3,51.1,73.8,
        61.4,73.1,77.3,48.5,89.8,50.7,52.0,59.6,66.1,31.6
]

# 对数据进行排序，这是构建茎叶图的第一步
data.sort()

# 创建一个默认值为列表的字典来存储茎和叶
# 茎是数据的百位及以上的数字，叶是十位数字
stem_leaf = defaultdict(list)

# 遍历排序后的数据，填充茎叶字典
for x in data:
    # 茎是十位数
    stem = int(x // 10)
    # 叶是整数部分的个位数和小数部分
    leaf = round(x % 10, 1)
    # 将叶附加到对应的茎上
    stem_leaf[stem].append(leaf)

# 打印茎叶图的标题
print("茎叶图 (茎单位: 10, 叶单位: 1)")
print("------------------------------------")

# 获取所有茎并排序
stems = sorted(stem_leaf.keys())

# 遍历排序后的茎，打印每一行
for stem in stems:
    # 将叶列表中的数字转换为字符串，并按升序排序
    leaves = ' '.join(map(str, sorted(stem_leaf[stem])))
    # 格式化打印茎和叶，使茎右对齐
    print(f"{stem:2d} | {leaves}")

# --- 绘图部分  ---
# 创建一个图形来呈现这段文字
fig, ax = plt.subplots(figsize=(12, 14))
ax.axis('off') # Hide the axes

# --- Title and Key ---
fig.text(0.5, 0.95, "Stem-and-Leaf Plot of Suspended Solids", ha='center', fontsize=20, weight='bold')
fig.text(0.5, 0.90, "Stem unit: 10, Leaf unit: 1", ha='center', fontsize=12, style='italic')

# --- 列标题 ---
fig.text(0.1, 0.85, "Frequency", ha='center', fontsize=12, weight='bold')
fig.text(0.2, 0.85, "Stem", ha='center', fontsize=12, weight='bold')
fig.text(0.55, 0.85, "Leaves", ha='center', fontsize=12, weight='bold')


# --- 生成绘图线 ---
lines_for_plot = []
for stem in stems:
    count = len(stem_leaf[stem])
    # Format leaves to show decimal part
    leaves = ' '.join(map(lambda l: f"{l:<3.1f}", sorted(stem_leaf[stem])))
    lines_for_plot.append((f"{count}", f"{stem}", leaves))


# --- 绘制情节内容 ---
y_pos = 0.80
for freq, stem, leaves in lines_for_plot:
    fig.text(0.1, y_pos, freq, ha='center', fontfamily='monospace', fontsize=12)
    fig.text(0.2, y_pos, stem, ha='center', fontfamily='monospace', fontsize=12)
    fig.text(0.25, y_pos, "|", ha='center', fontfamily='monospace', fontsize=12)
    fig.text(0.27, y_pos, leaves, ha='left', va='center', fontfamily='monospace', fontsize=10)
    y_pos -= 0.04

# 调整布��
plt.tight_layout(rect=[0, 0, 1, 0.9]) # Adjust rect to make space for title

# 保存该图形
plt.savefig(
    '2-16.png',                            # 指定输出的 PNG 文件名
    dpi=2000,                                     # 设置分辨率为 300 dpi
    bbox_inches='tight'                          # 紧缩边界以减少多余空白
)
plt.show()

