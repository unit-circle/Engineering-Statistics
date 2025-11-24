import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 心脏起搏器激活率数据
data = np.array([0.670, 0.697, 0.699, 0.707, 0.732, 0.733, 0.737,
                   0.747, 0.751, 0.774, 0.777, 0.804, 0.819, 0.827])

# (a) 计算样本均值和样本方差
sample_mean = np.mean(data)
# ddof=1 表示计算样本方差 (除以 n-1)
sample_variance = np.var(data, ddof=1)

# (b) 找出样本的上四分位数和下四分位数
lower_quartile = np.percentile(data, 25)
upper_quartile = np.percentile(data, 75)

# 计算IQR（四分位距）
iqr = upper_quartile - lower_quartile

# (c) 找出样本中位数
median = np.median(data)

# (e) 找出内径的第5百分位数和第95百分位数
percentile_5 = np.percentile(data, 5)
percentile_95 = np.percentile(data, 95)

# 计算理论上的上下边缘（内限）
lower_whisker_theory = lower_quartile - 1.5 * iqr
upper_whisker_theory = upper_quartile + 1.5 * iqr

# 找到数据中实际的上下边缘
# 箱线图的须延伸到不超过 Q1 - 1.5*IQR 和 Q3 + 1.5*IQR 的最远数据点
actual_lower_edge = np.min(data[data >= lower_whisker_theory])
actual_upper_edge = np.max(data[data <= upper_whisker_theory])


# 打印计算结果
print("--- 统计分析结果 ---")
print(f"(a) 样本均值: {sample_mean:.4f}")
print(f"(a) 样本方差: {sample_variance:.6f}")
print(f"IQR (四分位距): {iqr:.4f}")
print(f"(b) 样本下四分位数 (Q1): {lower_quartile:.4f}")
print(f"(b) 样本上四分位数 (Q3): {upper_quartile:.4f}")
print(f"(c) 样本中位数: {median:.4f}")
print(f"计算出的下边缘: {lower_whisker_theory:.4f}")
print(f"计算出的上边缘: {upper_whisker_theory:.4f}")
print(f"图表的实际下边缘: {actual_lower_edge:.4f}")
print(f"图表的实际上边缘: {actual_upper_edge:.4f}")
print(f"(e) 第5百分位数: {percentile_5:.4f}")
print(f"(e) 第95百分位数: {percentile_95:.4f}")
print("--------------------")

# (d) 绘制数据的箱线图
plt.figure(figsize=(6, 10))
plt.boxplot(data, vert=True, patch_artist=True)
plt.title('心脏起搏器激活率', fontsize=16)
plt.ylabel('激活率 (秒)', fontsize=12)
plt.xticks([1], ['设备'], fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 在图上标注四分位数、中位数和上下边缘
plt.text(1.1, lower_quartile, f'Q1', va='center', ha='left', color='blue')
plt.text(1.1, median, f'中位数', va='center', ha='left', color='red')
plt.text(1.1, upper_quartile, f'Q3', va='center', ha='left', color='green')
plt.text(0.9, actual_lower_edge, f'下边缘', va='center', ha='right', color='purple')
plt.text(0.9, actual_upper_edge, f'上边缘', va='center', ha='right', color='purple')

# 保存图像
plot_filename = 'd:/Jetbrains/PythonProject/Statistics/2-41_boxplot_vertical.png'
plt.savefig(
    '2-41.png',  # 保存为新文件名以作区分
    dpi=2000,
    bbox_inches='tight'
)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


