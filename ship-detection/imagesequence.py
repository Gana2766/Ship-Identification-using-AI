from PIL.Image import open
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import os
import numpy as np
import math


class ImageSequence(tf.keras.utils.Sequence):

    def __init__(self, dir, maskdir, batch_size=32, offset=0, num_samples=None, usecache=False):
        print(maskdir)
        self.dir = dir
        self.usecache = usecache
        # self.files = ['00a52cd2a.jpg','00d0a646b.jpg','00d412548.jpg','00fd8e126.jpg','0a9bc3e3a.jpg','0a50e22e5.jpg','0a997bd3f.jpg',  '0acf5fee5.jpg','0b7305a8c.jpg','0b74971bb.jpg']
        # + os.listdir("/content/Data/sample/noship/")
        self.files = sorted(os.listdir(maskdir))
        if num_samples != None:
            self.files = self.files[offset:offset+num_samples]
        self.maskdir = maskdir
        self.batch_size = batch_size
        self.cache_image = {}
        self.cache_mask = {}

    def __getitem__(self, index):
        # index=index//self.batch_size

        opimages = []
        opclasses = []
        for i in range(self.batch_size):
            file = self.files[index*self.batch_size+i]
            # print(file)
            filepath = os.path.join(self.dir, file)
            maskfilepath = os.path.join(self.maskdir, file)

            if self.usecache and file in self.cache_image:
                # print("*")
                opimages.append(self.cache_image[file])
                opclasses.append(self.cache_mask[file])
            else:
                # print("·")
                image = open(filepath)
                imagepixels = img_to_array(image)/255.0
                image.close()

                # print(np.max(imagepixels))

                n_img = open(maskfilepath)#.resize((43,43))
                n_img_array = img_to_array(n_img) / 255.0
                n_img_array = n_img_array.reshape((128, 128, 1))  # (psize)

                # print(np.max(n_img_array))

                maskpixels = n_img_array
                opimages.append(imagepixels)
                opclasses.append(maskpixels)

                if self.usecache:
                    self.cache_image[file] = imagepixels
                    self.cache_mask[file] = maskpixels

        return np.array(opimages), np.array(opclasses)

    def __len__(self):
        return math.floor(len(self.files)/self.batch_size)

    def on_epoch_end(self):
        #
        pass

    def __iter__(self):
        return super().__iter__()
