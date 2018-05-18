#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 10:35
# @Author  : zhuohf1
# @File    : Chapter01.py
'''
第一章 处理文件，摄像头和图形用户界面


'''

import cv2
import numpy as np
import os


''' ========例子1. 生产2张随机图片====== '''
# 生产120000个字节的随机数组
radomByteArray = bytearray(os.urandom(120000))
# 转化成numpy数组
flatNumpyArray = np.array(radomByteArray)
# 转化成400*300的灰度图片,一个像素一个字节
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png', grayImage)
# 转化成400*100的有颜色的图片，一个像素需要3个字节
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)


''' ========例子2. 生产2张随机图片====== '''