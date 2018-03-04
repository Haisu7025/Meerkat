# coding=utf-8

import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
import time

mu_x = 800
sigma_x = 134.63975
mu_y = 450
sigma_y = 61.00864

origsize_x = 1600
origsize_y = 900
cropsize_x = 160
cropsize_y = 160

while True:
    np.random.seed(time.time().__int__())
    x = np.random.normal(mu_x, sigma_x)
    y = np.random.normal(mu_y, sigma_y)

    # 超出边界重新采样
    if x - cropsize_x / 2 < 0 or x + cropsize_x / 2 > origsize_x:
        continue
    if y - cropsize_y / 2 < 0 or y + cropsize_y / 2 > origsize_y:
        continue
    return x, y

print x, y
