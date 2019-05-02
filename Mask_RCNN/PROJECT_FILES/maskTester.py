#import detector
import Compressor
import numpy as np 
import skimage.io as skio
import os
import cv2
import math
import skimage
from matplotlib import pyplot as plt

def genMask(img, maskPercent):
    maskPercent = math.sqrt(maskPercent)
    shape = img.shape
    rows, cols, _ = shape
    rowsCovered, colsCovered = int(rows*maskPercent), int(cols*maskPercent)
    rowsOffset, colsOffset = int((rows-rowsCovered)/2), int((cols-colsCovered)/2)
    mask = np.zeros((rows,cols),dtype=np.uint8)
    mask[rowsOffset:rowsOffset+rowsCovered, colsOffset:colsOffset+colsCovered]=255
    return mask


def getImages():
    for i in sorted(os.listdir("rawImages/"), reverse = True):
        yield cv2.imread("rawImages/"+i)

def loop():
    with open("blurTester.csv", 'w') as file:
        for count, img in enumerate(getImages()):     
            for maskPercent in np.linspace(.05,.95, 30):
                quality = 30
                mask = genMask(img, maskPercent)
                out = Compressor.compressImage(img, mask, quality)
                original = out['lossless.png']
                hybrid = out['hybrid.png']
                writeString = f'{maskPercent},{original},{hybrid}\n'
                print(writeString,end='')
                file.write(writeString)
            break
        
        
#loop()
# img = skio.imread('static/images/jpeg2000.png')
# x=img[800:1000,800:1000]
# skio.imsave('output/jp2.png',x)