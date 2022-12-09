import cv2, os
from scipy.ndimage import rotate as rotate_image

# берём список букв
arrLetters = ['а', 'б', 'в', 'г1', 'д', 'е','ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о1', 'п', 'р', 'с', 'т', 'у1', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# переименовываем фотографии в божеский вид
i = 0

while(i < len(arrLetters)):
    p = os.listdir('./LettersUse/'+arrLetters[i])
    j = 0
    while( j < len(p)):
        os.rename('./LettersUse/'+arrLetters[i]+'/'+p[j], './LettersUse/'+arrLetters[i]+'/'+str(i)+str(j)+'_.jpg')
        j=j+1
        print(j)
    
    i = i + 1

print(

)
