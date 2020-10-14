# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

pic1 = cv2.imread('/Users/alitootoonchi/Downloads/Telegram Desktop/AMoo/1.jpg')
pic2 = cv2.imread('/Users/alitootoonchi/Downloads/Telegram Desktop/AMoo/2.jpg')
pic3 = cv2.imread('/Users/alitootoonchi/Downloads/Telegram Desktop/AMoo/3.jpg')
testPic = cv2.imread('/Users/alitootoonchi/Downloads/Telegram Desktop/AMoo/test.jpg')


# %%
def histogram(img):
    hist = cv2.calcHist([img], [0, 1, 2], None, [16, 16, 16], [0, 256, 0, 256, 0, 256])
    hist = np.reshape(hist, (4096, 1))
    return hist



    # %%


def trainImgs(imgsFeatures):
    labels = np.ones([1, len(imgsFeatures)]);
    trainData = imgsFeatures[0]
    for i in xrange(0, len(imgsFeatures)):
        labels[0, i] = i
    labels = labels.astype('float32')
    labels = labels.transpose(1, 0)
    for i in xrange(1, len(imgsFeatures)):
        trainData = np.hstack((imgsFeatures[i], trainData))
    trainData = trainData.transpose(1, 0)
    model = cv2.ml.KNearest_create();
    model.train(trainData, cv2.ml.ROW_SAMPLE, labels)
    return model


    # %%


def classifyImgs(img, model):
    h1 = histogram(img);
    result = model.findNearest(h1.transpose(1, 0), 1)
    return result[0]

    # %%

    histPic1 = histogram(pic1)
    histPic2 = histogram(pic2)
    histPic3 = histogram(pic3)
    imgsFeatures = list()
    imgsFeatures.append(histPic3)
    imgsFeatures.append(histPic2)
    imgsFeatures.append(histPic1)

    model = trainImgs(imgsFeatures)

    classifyImgs(testPic, model)

