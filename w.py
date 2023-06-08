import cv2, os
l = './writeimg/'
p = os.listdir(l)
from PIL import Image
import numpy as np
# print(l+p[0])


# i = 0
# while(i < len(p)):

#     img = cv2.imread(l+p[i])
#     height, width, channels = img.shape
#     if(W<width):
#         W = width
#     if(H<width):
#         H = height

    # l = cv2.resize(cv2.imread('./writeimg/'+p[i]), (100, 100))
    # cv2.imwrite('./wr1/'+p[i],l)
    # i = i + 1

p = os.listdir('./wr1/')
o = 0

while(o < len(p)):
    i = 0
    l = cv2.cvtColor(cv2.imread('./wr1/'+p[o]), cv2.COLOR_BGR2GRAY).reshape(100*100)

    while(i < len(l)):
        if(l[i] <= 230):
            l[i] = 0
        else:
            l[i] = 255
        i = i + 1

    cv2.imwrite('./grey/'+p[o],l.reshape(100,100))
    o = o + 1
