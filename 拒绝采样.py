import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # 更改后端
import matplotlib.pyplot as plt


def complex_function(r, A, p, o, a, b):
    # 计算函数值
    term1 = (r + p) / (o + p)
    term2 = np.exp((r - o) / (o + p) * (-b))
    return A * (term1 ** a) * term2


# 参数值
o = 8.3
A = 20.14
p = 3.76
a = 9.03
b = 13.99

# 误差范围
A_err = 0.31
p_err = 0.42
b_err = 1.36
a_err = 1.08

# 设置样本数量
num_samples = 130000

# 拒绝采样
samples = []
while len(samples) < num_samples:
    r_sample = np.random.uniform(0, 20)  # 选择 r 的范围
    y_sample = np.random.uniform(0, complex_function(r_sample, A, p, o, a, b) * 1.2)  # 设定 y 的上限为函数值的 1.2 倍

    if y_sample < complex_function(r_sample, A, p, o, a, b):
        samples.append(r_sample)

samples = np.array(samples)

# 绘制函数曲线
r_values = np.linspace(0, 20, 100)
function_values = complex_function(r_values, A, p, o, a, b)

plt.figure(figsize=(12, 6))

# 绘制函数曲线
plt.subplot(1, 2, 1)
plt.plot(r_values, function_values, label='Complex Function', color='b')
plt.title('Complex Function Curve')
plt.xlabel('r')
plt.ylabel('f(r)')
plt.legend()
plt.grid()

# 绘制样本的直方图
plt.subplot(1, 2, 2)
plt.hist(samples, bins=50, density=True, alpha=0.7, color='lightblue', edgecolor='black')
plt.title('Histogram of Samples')
plt.xlabel('r')
plt.ylabel('Density')
plt.grid()

plt.tight_layout()
plt.show()