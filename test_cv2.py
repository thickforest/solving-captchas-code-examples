#!/usr/bin/python
#coding:utf-8
########################################################################
# File Name: test.py
# Author: forest
# Mail: thickforest@126.com 
# Created Time: 2018年04月20日 星期五 10时21分59秒
########################################################################

import cv2
import imutils
import sys
import matplotlib.pyplot as plt

image_path = 'generated_captcha_images/23XT.png'
if len(sys.argv) > 1:
	image_path = sys.argv[1]
image = cv2.imread(image_path)
print image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 画直方图(Histogram)
print len(gray.ravel()) # = width * height
plt.hist(gray.ravel(), 256)
plt.show()

# 增加8px边框
gray = cv2.copyMakeBorder(gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)

# THRESH_BINARY_INV: 黑白颠倒 0=>255,255=>0
# THRESH_OTSU: 自动计算阈值(thresh)
thresh, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
# 原文 https://blog.csdn.net/lcalqf/article/details/71170171
#      https://blog.csdn.net/jningwei/article/details/77747959
# cv2.threshold (源图片, 阈值, 填充色, 阈值类型)
#  src：源图片，必须是单通道
#  thresh：阈值，取值范围0～255
#  maxval：填充色，取值范围0～255
#  type：阈值类型，具体见下
#  type=0(THRESH_BINARY) 小于阈值的像素点置0，大于阈值的像素点置填充色
#  type=1(THRESH_BINARY_INV) 小于阈值的像素点置填充色，大于阈值的像素点置0
#  type=2(THRESH_TRUNC) 小于阈值的像素点保持原色，大于阈值的像素点置灰色
#  type=3(THRESH_TOZERO) 小于阈值的像素点置0，大于阈值的像素点保持原色
#  type=4(THRESH_TOZERO_INV) 小于阈值的像素点保持原色，大于阈值的像素点置0

contours = cv2.findContours(th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]

for contour in contours:
	# 假设轮廓有100个点,OpenCV返回的ndarray的维数是(100, 1, 2),而不是我们认为的(100, 2)
	print contour.shape
	(x, y, w, h) = cv2.boundingRect(contour)
	print x, y, w, h
	cv2.rectangle(gray, (x-2, y-2), (x + w + 4, y + h + 4), (0, 255, 0), 1)

cv2.imshow('xxx', gray)
cv2.waitKey()
