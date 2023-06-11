import tensorflow
# import tensorflow.keras
import os
# import keras
import numpy as np
import cv2
# import keras 
from keras.models import Sequential

from keras.layers import Dense, Dropout , Conv2D , Flatten, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from keras.layers import Activation
from keras.models import load_model

from tensorflow import keras

input_shape = (100, 100, 1)


data = []
data1 = []
# i = 2500 
# while (i < 3000):




#   data1.append( [0., 1.])
#   data1.append( [1., 0.])
#   i = i + 1

j = 0

while(j <= 161):
    o = 1
    h = 0
    while(o<=33):
        data.append( 
            np.array(cv2.imread('./grey/'+str(o)+'_'+str(j)+'.jpg', cv2.IMREAD_UNCHANGED))
        )
        data1.append(h)
        o = o + 1
        h = h + 1
    j = j + 1

num_classes = 33
data = np.array(data)
data1 = np.array(data1)
data = np.expand_dims(data, -1)

print(data1.shape)
y_test = keras.utils.to_categorical(data1, num_classes)






model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        Conv2D(32, kernel_size=(3, 3), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, kernel_size=(3, 3), activation="relu"),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dropout(0.5),
        Dense(num_classes, activation="softmax"),
    ]
)

model.summary()


batch_size = 128
epochs = 10

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(data, y_test, batch_size=batch_size, epochs=epochs,)

















# model.fit(np.array(data), np.array(data1) ,      epochs=7 )

# n = [

# ['500',' 1000'],
# ['1000',' 2000'],
# ['2000 ','3000'],
# ['3000','4000'],
# ['4000','5000'],
# ['5000','6000'],
# ['6000','7000'],
# ['7000','8000'],
# ['8000','9000'],
# ['9000','10000'],
# ['10000','11000'],
# ['11000','12000'],
# ['12000','13000'],
# ['13000','14000'],
# ['14000','15000'],
# ['15000','16000'],
# ['16000','17000'],
# ['17000','18000'],
# ['18000','19000'],
# ['19000','19550'],

# ]







# g=0
# while(g< len(n)):
#     model = load_model(modelName)
#     data = []
#     data1 = []
#     i = int(n[g][0])
#     while (int(n[g][0]) < int(n[g][1])):


#         data.append( 
#             np.array(cv2.imread('./v/'+str(i)+'.jpg', cv2.IMREAD_UNCHANGED))/255
#         )
#         data.append(
#             np.array(cv2.imread('./Women/'+str(i)+'.jpg', cv2.IMREAD_UNCHANGED))/255
#             )
#         data1.append( [0., 1.])
#         data1.append( [1., 0.])
#         i = i + 1

#     model.fit(np.array(data), np.array(data1) ,      epochs=5 )
#     model.save(modelName)
#     time.sleep(2)

#     g = g + 1