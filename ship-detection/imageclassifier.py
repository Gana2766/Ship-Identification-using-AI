from tensorflow.keras.models import load_model
from PIL.Image import open
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
import os
model = None

#serverPath="D:/Downloads/test3/test3/public/images/"

serverPath="E:/Final Project  - Ship Detection/Ship Identification using AI/test3/public/images"

def img(n):
    global model
    if model == None:
        model = load_model('E:/Final Project  - Ship Detection/Ship Identification using AI/ship-detection/new-UNET/model_cp500.h5')
        # model.summary()

    print(n)
    image = open(n)

    image = image.resize((128, 128))
    imagearr = np.array([img_to_array(image)/255.0])
    output = model.predict(imagearr)
    del image, imagearr
    image = cv2.imread(n)

    cv2.imwrite(os.path.join(serverPath,'input.png'),image)
    image.resize((128, 128, 3))
    image[:,:,2] = np.where(output[0,:,:,0] >0.4,
                            255, image[:, :, 2])
     # convert color from CV2 BGR back to RGB
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite('output.png', image)
    cv2.imwrite(os.path.join(serverPath,'output.png'),image)
    return image


# img('F:/zip/airbus-ship-detection/OriginalData/test_v2/0c5e35213.jpg')
