# -*- coding:utf-8 -*-
import os
from PIL import Image
import numpy as np
import time

mu_x = 800
sigma_x = 134.63975
mu_y = 450
sigma_y = 61.00864

origsize_x = 1600
origsize_y = 900
cropsize_x = 160
cropsize_y = 160


def Gaussian_Sample():
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


def window_extract(ori_img):
    x, y = Gaussian_Sample()
    x0 = x - cropsize_x / 2
    x1 = x + cropsize_x / 2
    y0 = y - cropsize_y / 2
    y1 = y + cropsize_y / 2
    new_img = ori_img.crop((x0, y0, x1, y1))
    return new_img


def main():
    img = Image.open('test.png')
    img = window_extract(img)
    img.show()


if __name__ == '__main__':
    main()
