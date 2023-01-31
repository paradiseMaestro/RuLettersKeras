from scipy.ndimage import rotate as rotate_image
import cv2
import os
os.makedirs('dataset1')
l = 1
while(l < 10):
  image = cv2.imread(str(l)+'.jpg', cv2.IMREAD_GRAYSCALE)
  #rotation angle in degree
  i = 0
  g = 0 
  while(i < 18):
    rotated_img1 = rotate_image(image,-45 + g, cval=243)
    cv2.imwrite('./dataset1/'+str(l)+'1lol'+str(i)+'.jpg',rotated_img1)
    i = i + 1
    g = g + 5
  l = l + 1
n = 21
# from os import listdir

g = os.listdir('./dataset1')

i = 0 
while( i < len(g)):
  os.rename('./dataset1/'+g[i], './dataset1/'+str(n)+'_'+str(i)+'.jpg')
  i = i + 1



# os.rename('a.txt', 'b.kml')