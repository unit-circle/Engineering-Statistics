#coding=utf-8
# 导入必要的第三方库
import matplotlib.pyplot as plt
import numpy as np  # 导入 numpy，用于数值计算（均值、标准差、方差等）
import pandas as pd  # 导入 pandas，用于表格数据处理和统计计算
import seaborn as sns  # 导入 seaborn，用于绘制更美观的统计图

sns.set_theme(style="whitegrid")          # 使用 seaborn 的白色网格主题，使图形更加美观
# --- 更可靠的中文显示方案 ---
# 在设置 seaborn 主题后，再设置字体，防止被覆盖
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题
# 2. 在这里输入数据
# ---------- 重要说明 ----------
# 1）请将你的“横坐标数据”填入 x_data 列表中
# 2）请将你的“纵坐标数据”填入 y_data 列表中
# 3）x_data 和 y_data 的长度必须一致（即一一对应）
# 4）如果你只有一组 y 数据，但没有明确的 x，可以用序号 [1, 2, 3, ...] 作为 x
# ------------------------------
# 用你的数据替换下面两行中的数字（可以是整数或小数）
x_data = list(range(1,19))           # 在这里输入你的 x 数据（横坐标）
y_data = [96,96,102,102,102,104,104,108,126,126,128,128,140,156,160,160,164,170] # 在这里输入你的 y 数据（纵坐标）
# 3. 将原始数据转换为 numpy 数组 / DataFrame
x = np.array(x_data, dtype=float)         # 将 x_data 转为 numpy 数组，便于数值运算和绘图
y = np.array(y_data, dtype=float)         # 将 y_data 转为 numpy 数组，便于数值运算和绘图
df = pd.DataFrame({                       # 使用 pandas 创建一个 DataFrame
    'x': x,                               # 'x' 列保存横坐标数据
    'y': y                                # 'y' 列保存纵坐标数据
})
# 4. 计算统计量：均值、标准差、方差
y_mean = df['y'].mean()                  # 计算 y 的均值（平均值）
y_std = df['y'].std(ddof=1)              # 计算 y 的样本标准差（ddof=1 表示除以 n-1）
y_var = df['y'].var(ddof=1)              # 计算 y 的样本方差（ddof=1 表示除以 n-1）
# 在终端打印统计结果，方便查看
print("===== 统计结果 =====")             # 打印分隔标题
print(f"均值 (mean): {y_mean:.4f}")      # 输出均值，保留 4 位小数
print(f"标准差 (std): {y_std:.4f}")      # 输出标准差，保留 4 位小数
print(f"方差 (var): {y_var:.4f}")        # 输出方差，保留 4 位小数
# 5. 创建画布与坐标轴
fig, ax = plt.subplots(figsize=(8, 4))   # 创建一个 8x4 英寸的图像和一个坐标轴对象 ax
# 6. 绘制点线图（折线 + 散点）
# 使用 seaborn 绘制折线图
'''
sns.lineplot(
    x='x',                               # 指定 DataFrame 中作为 x 轴的数据列名
    y='y',                               # 指定 DataFrame 中作为 y 轴的数据列名
    data=df,                             # 指定数据源为 df
    ax=ax,                               # 绘制到 ax 这个坐标轴对象上
    color='steelblue',                   # 设置折线颜色为钢蓝色
    linewidth=2,                         # 设置折线宽度
    marker=None,                         # 折线本身不画点（点单独用散点图绘制）
    label='数据折线'                      # 图例名称：表示这是一条数据折线
)
'''
# 使用 seaborn 绘制散点图
sns.scatterplot(
    x='x',                               # 指定 DataFrame 中作为 x 轴的数据列名
    y='y',                               # 指定 DataFrame 中作为 y 轴的数据列名
    data=df,                             # 指定数据源为 df
    ax=ax,                               # 绘制到同一个坐标轴 ax 上
    color='crimson',                     # 设置散点颜色为深红色
    s=40,                                # 设置散点大小
    alpha=0.9,                           # 设置散点透明度
    edgecolor='white',                   # 设置散点边缘颜色为白色
    linewidth=0.6,                       # 设置散点边缘线宽
    label='数据点'                        # 图例名称：表示这些是具体数据点
)
# 7. 在图中绘制均值参考线
ax.axhline(
    y=y_mean,                            # 水平线位置设置为 y 的均值
    color='green',                       # 均值线颜色为绿色
    linestyle='--',                      # 均值线使用虚线样式
    linewidth=1.5,                       # 均值线宽度
    label=f'均值: {y_mean:.2f}'          # 图例中显示“均值: 数值”，保留两位小数
)
# 8. 设置标题、坐标轴标签和图例
ax.set_title('Dot Diagram', fontsize=16)  # 设置图形标题，使用中文说明
ax.set_xlabel('X（Serial Number）', fontsize=12)        # 设置 x 轴标签，说明横坐标含义
ax.set_ylabel('Y（Yield Strength）', fontsize=12)        # 设置 y 轴标签，说明纵坐标含义
ax.tick_params(axis='both', labelsize=10)        # 设置坐标轴刻度字体大小
ax.set_xticks(np.arange(1, 19, 1)) # 设置x轴刻度为从1到18，间隔为1
ax.set_yticks(np.arange(90, 180, 10))
ax.legend(
    loc='best',                                  # 自动选择最合适的图例位置
    fontsize=9,                                  # 设置图例字体大小
    frameon=True,                                # 显示图例边框
    framealpha=0.9                               # 设置图例边框透明度
)
# 9. 布局优化与保存为 PNG 图片
plt.tight_layout()                           # 自动调整布局，防止标签重叠
plt.savefig(
    '2-4.png',                            # 指定输出的 PNG 文件名
    dpi=2000,                                     # 设置分辨率为 2000 dpi
    bbox_inches='tight'                          # 紧缩边界以减少多余空白
)
# 10. 显示图像
plt.show()                                       # 在屏幕上显示绘制好的图像窗口