import time
start_time = time.time()


import os
import cv2
# files = os.listdir('pullImg')
files = os.listdir('writeimg')

# l = [243,243,103,243,243,243,243,243,243,243,243,243,243,243,243,243,78,]

def isTrue(l):
    i = 0
    while (i < len(l)):
        # print(l[i])
        if (l[i] != 243):
            
            return True
        i = i + 1
    return False

print(len(files))
# isTrue(l)

i = 0 

while(i < 0):
    img = cv2.imread('pullImg/'+files[i], cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('pullImg/'+'1_0.jpg', cv2.IMREAD_GRAYSCALE)
    # 1_0
    height, width = img.shape
    w = 0 
    h = 0
    # widthLR = []
    # heightUD = []
    WR = 0 
    WL = 0
    HU = 0
    HD = 0
    while(w < width):
        lineW = img[0:height, w:w+1]
        # print(lineW[0])
        if(isTrue(lineW)):
            WL=w
            # print(w)
            break
        # print(w)
        w = w + 1
    w = 0 
    while(w < width):
        lineW = img[0:height, width-w-1:width-w]
        # print(lineW[0])
        if(isTrue(lineW)):
            # widthLR.append(w)
            WR = (width-w-1)
            break
        # print(w)
        w = w + 1


    while(h < height):
        lineH = img[h:h+1, 0:width]
        # print(lineH[0])
        if(isTrue(lineH[0])):
            # heightUD.append(h)
            HU = h
            break
        h = h + 1
    h = 0

    while(h < height):
        lineH = img[height-h-1:height-h, 0:width]
        # print(lineH[0])
        if(isTrue(lineH[0])):
            # heightUD.append(h)
            HD = height-h-1
            break
        h = h + 1
    

    cv2.imwrite('writeimg/'+files[i], img[HU:HD, WL:WR])
    i = i + 1


# print(widthLR)
# print(heightUD)

# 536
# 1024

# 288
# 985


# img = cv2.imread('eeee.jpg', cv2.IMREAD_GRAYSCALE)

# print(
#     img[0]
# )



































































































































# import os
# import cv2
# files = os.listdir('pullImg')

# # l = [243,243,103,243,243,243,243,243,243,243,243,243,243,243,243,243,78,]

# def isTrue(l):
#     i = 0
#     while (i < len(l)):
#         # print(l[i])
#         if (l[i] != 243):
            
#             return True
#         i = i + 1
#     return False

# # print(len(files))
# # isTrue(l)

# i = 0 

# while(i < 10):
#     img = cv2.imread('pullImg/'+files[i], cv2.IMREAD_GRAYSCALE)
#     # img = cv2.imread('pullImg/'+'1_0.jpg', cv2.IMREAD_GRAYSCALE)
#     # 1_0
#     height, width = img.shape
#     w = 0 
#     h = 0
#     widthLR = []
#     heightUD = []
#     WR = 0 
#     WL = 0
#     while(w < width):
#         lineW = img[0:height, w:w+1]
#         # print(lineW[0])
#         if(isTrue(lineW)):
#             widthLR.append(w)
#             # print(w)
#             # break
#         w = w + 1
#     # w = 0 
#     # while(w < width):
#     #     lineW = img[0:height, width-w-1:width-w]
#     #     # print(lineW[0])
#     #     if(isTrue(lineW)):
#     #         widthLR.append(w)
#     #         # print(width-w-1)
#     #         break
#     #     w = w + 1


#     while(h < height):
#         lineH = img[h:h+1, 0:width]
#         # print(lineH[0])
#         if(isTrue(lineH[0])):
#             heightUD.append(h)
#         h = h + 1

#     cv2.imwrite('writeimg/'+files[i], img[heightUD[0]:heightUD[-1], widthLR[0]:widthLR[-1]])
#     i = i + 1


# # print(widthLR)

# # 536
# # 1024


# # img = cv2.imread('eeee.jpg', cv2.IMREAD_GRAYSCALE)

# # print(
# #     img[0]
# # )











print("--- %s seconds ---" % (time.time() - start_time))
