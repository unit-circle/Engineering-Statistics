import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 或者其他支持中文的字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 原始数据
temperatures = np.array([84, 49, 61, 40, 83, 67, 45, 66, 70, 69, 80, 58,
                         68, 60, 67, 72, 73, 70, 57, 63, 70, 78, 52, 67,
                         53, 67, 75, 61, 70, 81, 76, 79, 75, 76, 58, 31])

# (a) 计算样本均值和样本标准差
mean_temp = np.mean(temperatures)
std_temp = np.std(temperatures, ddof=1)  # ddof=1 表示计算样本标准差

# (b) 找出温度的上四分位数和下四分位数
q1_temp = np.percentile(temperatures, 25)
q3_temp = np.percentile(temperatures, 75)

# (c) 找出中位数
median_temp = np.median(temperatures)

print("--- 原始数据分析 ---")
print(f"(a) 样本均值: {mean_temp:.2f}°F")
print(f"(a) 样本标准差: {std_temp:.2f}°F")
print(f"(b) 下四分位数 (Q1): {q1_temp}°F")
print(f"(b) 上四分位数 (Q3): {q3_temp}°F")
print(f"(c) 中位数: {median_temp}°F")
print("-" * 20)

# 新增：输出从小到大排列的数据
sorted_temperatures = np.sort(temperatures)
print("\n--- 从小到大排列的温度数据 ---")
print(sorted_temperatures)
print("-" * 20)

# (d) 剔除最小的观测值（31°F），重新计算
temperatures_removed = temperatures[temperatures != 31]

mean_temp_removed = np.mean(temperatures_removed)
std_temp_removed = np.std(temperatures_removed, ddof=1)
q1_temp_removed = np.percentile(temperatures_removed, 25)
q3_temp_removed = np.percentile(temperatures_removed, 75)
median_temp_removed = np.median(temperatures_removed)

print("\n--- 剔除最小值 (31°F) 后的数据分析 ---")
print(f"(d) 重新计算的样本均值: {mean_temp_removed:.2f}°F")
print(f"(d) 重新计算的样本标准差: {std_temp_removed:.2f}°F")
print(f"(d) 重新计算的下四分位数 (Q1): {q1_temp_removed}°F")
print(f"(d) 重新计算的上四分位数 (Q3): {q3_temp_removed}°F")
print(f"(d) 重新计算的中位数: {median_temp_removed}°F")
print("-" * 20)

# 计算并输出IQR和上下边缘
iqr = q3_temp - q1_temp
lower_edge = q1_temp - 1.5 * iqr
upper_edge = q3_temp + 1.5 * iqr

# 找到实际的晶须位置（在计算边缘内的最远数据点）
actual_lower_whisker = temperatures[temperatures >= lower_edge].min()
actual_upper_whisker = temperatures[temperatures <= upper_edge].max()

print("\n--- IQR 和边缘计算 ---")
print(f"四分位距 (IQR): {iqr:.2f}")
print(f"理论下边缘 (Q1 - 1.5 * IQR): {lower_edge:.2f}")
print(f"理论上边缘 (Q3 + 1.5 * IQR): {upper_edge:.2f}")
print(f"实际下晶须位置 (数据点): {actual_lower_whisker}")
print(f"实际上晶须位置 (数据点): {actual_upper_whisker}")
print("-" * 20)

# (e) 构建数据的箱线图
plt.figure(figsize=(6, 8))
# 先正常绘制箱线图，并捕获其返回的绘图元素
bp = plt.boxplot(temperatures, vert=True, patch_artist=True,
                 boxprops=dict(facecolor='lightblue'),
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='red', linewidth=2),
                 flierprops=dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none'))

# 手动修改晶须位置 ---
# bp['whiskers'] 是一个包含上下两条晶须线的列表
# bp['whiskers'][0] 是下晶须, bp['whiskers'][1] 是上晶须
# 我们用计算出的理论边缘来更新它们的位置
bp['whiskers'][0].set_ydata([lower_edge, q1_temp])
bp['whiskers'][1].set_ydata([q3_temp, upper_edge])

# 同样地，更新晶须末端“帽子”的位置
bp['caps'][0].set_ydata([lower_edge, lower_edge])
bp['caps'][1].set_ydata([upper_edge, upper_edge])
# --- 修改结束 ---

plt.title('航天飞机O型环结合温度箱线图')
plt.ylabel('温度 (°F)')
plt.xticks([1], ['温度数据'])
plt.grid(True, linestyle='--', alpha=0.7)
current_ylim = plt.ylim()
plt.ylim(current_ylim[0], upper_edge + 5)
# 在图上标注四分位数、中位数和上下边缘
plt.text(1.1, q1_temp, f'Q1', va='center', ha='left', color='blue')
plt.text(1.1, median_temp, f'中位数', va='center', ha='left', color='red')
plt.text(1.1, q3_temp, f'Q3', va='center', ha='left', color='green')
plt.text(0.9, lower_edge, f'下边缘', va='center', ha='right', color='purple')
plt.text(0.9, upper_edge, f'上边缘', va='center', ha='right', color='purple')
plt.savefig(
    '2-33.png',  # 保存为新文件名以作区分
    dpi=2000,
    bbox_inches='tight'
)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


