# 1. 求解微分方程初值问题(scipy.integrate.odeint)
from scipy.integrate import odeint  # 导入 scipy.integrate 模块
import numpy as np
import matplotlib.pyplot as plt

def dy_dt(y, t):  # 定义函数 f(y,t)
    return np.sin(t**2)

y0 = [1]  # y0 = 1 也可以
t = np.arange(-10,10,0.01)  # (start,stop,step)
y = odeint(dy_dt, y0, t)  # 求解微分方程初值问题

# 绘图
plt.plot(t, y)
plt.title("scipy.integrate.odeint")
plt.show()
