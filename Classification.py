# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 22:13:44 2022

@author: Mars
"""

import os
import cv2

labels = open("test\label.txt","r")  
label = labels.read().split(',')
print(len(label))


path = 'test/'
#path =  'train/'
for cnt in range(len(label)):
    print(str(cnt) + '\n')
    image_path = (path+str(cnt)+'.png')
    img = cv2.imread(image_path)
    #根据图片对应的标签分类到对应的文件夹下：
    cv2.imwrite('Test_png/'+label[cnt]+'/'+str(cnt)+'.png',img) #
    cnt += 1
