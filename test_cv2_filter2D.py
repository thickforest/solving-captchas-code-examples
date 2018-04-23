#!/usr/bin/python
#coding:utf-8
########################################################################
# File Name: test_cv2_filter2D.py
# Author: forest
# Mail: thickforest@126.com 
# Created Time: 2018年04月23日 星期一 16时04分18秒
########################################################################

import cv2
import numpy as np

path = 'extracted_letter_images/5/000001.png'

image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#kernel = np.array([[-1,-1,0],[-1,0,1],[0,1,1]])
kernel = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
image2 = cv2.filter2D(image, -1, kernel)
cv2.imshow('image', image)
cv2.imshow('image2', image2)
cv2.waitKey()
