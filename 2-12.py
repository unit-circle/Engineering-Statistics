import numpy as np
import pandas as pd


x_data = [20.1, 20.5, 20.3, 20.5, 20.6, 20.1, 20.2, 20.4]

#将原始数据转换为 numpy 数组 / DataFrame
x = np.array(x_data, dtype=float)  # 将 x_data 转为 numpy 数组，便于数值运算
df = pd.DataFrame({  # 使用 pandas 创建一个 DataFrame
    'x': x,  # 'x' 列保存横坐标数据
})

#计算统计量：均值、标准差、方差
x_mean = df['x'].mean()  # 计算 X 的均值（平均值）
x_std = df['x'].std(ddof=1)  # 计算 X 的样本标准差（ddof=1 表示除以 n-1）
x_var = df['x'].var(ddof=1)  # 计算 X 的样本方差（ddof=1 表示除以 n-1）

#在终端打印统计结果，方便查看
print("===== 统计结果 =====")  # 打印分隔标题
print(f"均值 (mean): {x_mean:.4f}")  # 输出均值，保留 4 位小数
print(f"标准差 (std): {x_std:.4f}")  # 输出标准差，保留 4 位小数
print(f"方差 (var): {x_var:.4f}")  # 输出方差，保留 4 位小数

# 将 x_data 中的数据都除以 2.54
x_data_div = [val / 2.54 for val in x_data]

# 将转换后的数据创建为新的 DataFrame
df_div = pd.DataFrame({'x_div': x_data_div})

# 计算新的统计量
x_mean_div = df_div['x_div'].mean()
x_std_div = df_div['x_div'].std(ddof=1)
x_var_div = df_div['x_div'].var(ddof=1)

# 在终端打印新的统计结果
print("\n===== 除以 2.54 后的统计结果 =====")
print(f"均值 (mean): {x_mean_div:.4f}")
print(f"标准差 (std): {x_std_div:.4f}")
print(f"方差 (var): {x_var_div:.4f}")
