from scipy.ndimage import rotate as rotate_image
import cv2
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
