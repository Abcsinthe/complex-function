import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # 更改后端
import matplotlib.pyplot as plt

def complex_function(r, A, p, o, a, b):
    # 计算函数值
    term1 = (r + p) / (o + p)
    term2 = np.exp((r - o) / (o + p) * (-b))
    return A * (term1 ** a) * term2

# 参数值和误差
o = 8.3
A = 20.14
p = 3.76
a = 9.03
b = 13.99

# 误差范围
A_err = 0.31
a_err = 1.08
b_err = 1.36
p_err = 0.42

# 计算函数值
r_values = np.linspace(0, 10, 100)
function_values = complex_function(r_values, A, p, o, a, b)

# 计算误差
function_values_upper = complex_function(r_values, A + A_err, p + p_err, o, a + a_err, b + b_err)
function_values_lower = complex_function(r_values, A - A_err, p - p_err, o, a - a_err, b - b_err)

# 计算误差棒的高度
error_upper = function_values_upper - function_values
error_lower = function_values - function_values_lower
errors = np.maximum(error_upper, error_lower)

# 绘制图像
plt.figure(figsize=(10, 6))
plt.plot(r_values, function_values, label='Complex Function', color='b')
plt.fill_between(r_values, function_values - errors, function_values + errors, color='lightblue', alpha=0.5, label='Error Range')
plt.title('Complex Function with Error Bars')
plt.xlabel('r')
plt.ylabel('f(r)')
plt.legend()
plt.grid()
plt.show()