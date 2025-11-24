import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置绘图样式
sns.set_style("whitegrid")

# High Dose 和 Control 组的基因表达数据
high_dose_data = [16.1, 134.9, 52.7, 14.4, 124.3, 99.0, 24.3, 16.3, 15.2, 47.7, 12.9, 72.7, 126.7, 46.4, 60.3, 23.5, 43.6, 79.4, 38.0, 58.2, 26.5, 25.1]
control_data = [297.1, 491.8, 1332.9, 1172.0, 1482.7, 335.4, 528.9, 24.1, 545.2, 92.9, 337.1, 102.3, 255.1, 100.5, 159.9, 168.0, 95.2, 132.5, 442.6, 15.8, 175.6, 131.1]

# 将列表转换为numpy数组，方便后续计算
group1_data = np.array(high_dose_data)
group2_data = np.array(control_data)

# --- 绘制直方图 ---
plt.figure(figsize=(14, 12))
plt.suptitle('Gene Expression Data Analysis', fontsize=16)

# High Dose 组直方图
plt.subplot(2, 2, 1)
high_dose_bins = np.arange(0, 150, 20)
sns.histplot(group1_data, bins=high_dose_bins, kde=False, color='blue')
plt.title('Histogram - High Dose')
plt.xlabel('Gene Expression Level')
plt.ylabel('Frequency')

# Control 组直方图
plt.subplot(2, 2, 2)
control_bins = np.arange(0, 1600, 150)
sns.histplot(group2_data, bins=control_bins, kde=False, color='red')
plt.title('Histogram - Control')
plt.xlabel('Gene Expression Level')
plt.ylabel('Frequency')

# --- 绘制累积频率图 (ECDF) ---
# High Dose 组累积频率图
plt.subplot(2, 2, 3)
sns.ecdfplot(group1_data, color='blue')
plt.title('Cumulative Frequency (ECDF) - High Dose')
plt.xlabel('Gene Expression Level')
plt.ylabel('Cumulative Frequency')

# Control 组累积频率图
plt.subplot(2, 2, 4)
sns.ecdfplot(group2_data, color='red')
plt.title('Cumulative Frequency (ECDF) - Control')
plt.xlabel('Gene Expression Level')
plt.ylabel('Cumulative Frequency')


plt.savefig(
    '2-30.png',                            # 指定输出的 PNG 文件名
    dpi=2000,                                     # 设置分辨率为 2000 dpi
    bbox_inches='tight'                          # 紧缩边界以减少多余空白
)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()



