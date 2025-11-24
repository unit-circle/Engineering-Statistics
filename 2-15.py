import matplotlib.pyplot as plt
from collections import defaultdict

# 原始数据
data = [
    1115, 1567, 1223, 1782, 1055, 1310, 1883, 375, 1522, 1764,
    1540, 1203, 2265, 1792, 1330, 1502, 1270, 1910, 1000, 1608,
    1258, 1015, 1018, 1820, 1535, 1315, 845, 1452, 1940, 1781,
    1085, 1674, 1890, 1120, 1750, 798, 1016, 2100, 910, 1501,
    1020, 1102, 1594, 1730, 1238, 865, 1605, 2023, 1102, 990,
    2130, 706, 1315, 1578, 1468, 1421, 2215, 1269, 758, 1512,
    1109, 785, 1260, 1416, 1750, 1481, 885, 1888, 1560, 1642
]

# 对数据进行排序，这是构建茎叶图的第一步
data.sort()

# 创建一个默认值为列表的字典来存储茎和叶
# 茎是数据的百位及以上的数字，叶是十位和个位数字（表示为小数）
stem_leaf = defaultdict(list)

# 遍历排序后的数据，填充茎叶字典
for x in data:
    stem = x // 100
    leaf_part = x % 100
    leaf = leaf_part / 10.0
    stem_leaf[stem].append(leaf)

# 打印茎叶图的标题
print("茎叶图 (茎单位: 100, 叶单位: 10)")
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
fig, ax = plt.subplots(figsize=(10, 12))
ax.axis('off') # Hide the axes

# --- Title and Key ---
fig.text(0.5, 0.95, "Stem-and-Leaf Plot of Failure Cycles", ha='center', fontsize=20, weight='bold')
fig.text(0.5, 0.90, "Stem unit: 100, Leaf unit: 10", ha='center', fontsize=12, style='italic')

# --- 列标题 ---
fig.text(0.15, 0.85, "Frequency", ha='center', fontsize=12, weight='bold')
fig.text(0.35, 0.85, "Stem", ha='center', fontsize=12, weight='bold')
fig.text(0.65, 0.85, "Leaves", ha='center', fontsize=12, weight='bold')

# ---找到中位数茎并准备线条---
total_count = len(data)
median_pos = (total_count + 1) / 2
cumulative_count = 0
median_stem_index = -1

for i, stem in enumerate(stems):
    count = len(stem_leaf[stem])
    if (cumulative_count + count) >= median_pos:
        median_stem_index = i
        break
    cumulative_count += count

# --- 生成绘图线 ---
lines_for_plot = []
for stem in stems:
    count = len(stem_leaf[stem])
    leaves = ' '.join(map(str, sorted(stem_leaf[stem])))
    lines_for_plot.append((f"{count}", f"{stem}", leaves))


# --- 绘制情节内容 ---
y_pos = 0.80
for freq, stem, leaves in lines_for_plot:
    fig.text(0.15, y_pos, freq, ha='center', fontfamily='monospace', fontsize=12)
    fig.text(0.35, y_pos, stem, ha='center', fontfamily='monospace', fontsize=12)
    fig.text(0.40, y_pos, "|", ha='center', fontfamily='monospace', fontsize=12)
    fig.text(0.42, y_pos, leaves, ha='left', va='center', fontfamily='monospace', fontsize=10) # Reduced fontsize for leaves
    y_pos -= 0.04

# 调整布局
plt.tight_layout(rect=[0, 0, 1, 0.9]) # Adjust rect to make space for title

# 保存该图形
plt.savefig(
    '2-15.png',                            # 指定输出的 PNG 文件名
    dpi=2000,                                     # 设置分辨率为 300 dpi（清晰）
    bbox_inches='tight'                          # 紧缩边界以减少多余空白
)
plt.show()

