from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import save_model, load_model


import matplotlib.pyplot as plt
import numpy as np

# from model_autoencoder import create_model
# from model128_2 import create_model
# from model128 import create_model

from imagesequence import ImageSequence
from modelUNET import create_model

import datetime
import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


if len(sys.argv) > 2:
    epochsCMD = int(sys.argv[2])
else:
    epochsCMD = 5
if len(sys.argv) > 1:
    print('Loading model from ' + sys.argv[1])
    model = load_model(sys.argv[1])  # , custom_objects={'iou_loss': iou_loss})
else:
    print('Creating new model')
    model = create_model()

model.summary()
onlyships128 = 'E:/Final Project  - Ship Detection/dataset/onlyship128'
onlyshipsmasks128 = 'E:/Final Project  - Ship Detection/dataset/onlyshipmask128'
g = ImageSequence(onlyships128, onlyshipsmasks128, batch_size=4, num_samples=1008, usecache=True)


d = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')

os.mkdir('model_cp_' + d)

cb1 = ReduceLROnPlateau(monitor='loss', patience=10, cooldown=10,
                        factor=0.96, min_lr=10e-5, verbose=1, min_delta=0)
cb2 = EarlyStopping(monitor='loss', patience=20)
cb3 = ModelCheckpoint(filepath='model_cp_' + d + '/model_cp{epoch}.h5', save_best_only=False, verbose=1)

# model.fit(g, epochs=500, callbacks=[cb1,cb2,cb3], shuffle=True, validation_data=g_val)

h = model.fit(g, epochs=epochsCMD, callbacks=[cb1, cb3], shuffle=True)


L = [] 
A = []
losss= h.history['loss']
accuuu = h.history['accuracy']

L.append(losss*100)
A.append(accuuu*100)
print(A)
print(L)


plt.plot(L)
plt.plot(A)

plt.show()

save_model(model, 'model_' + d + '.h5')
