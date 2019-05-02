#import detector
import Compressor
import numpy as np 
import skimage.io as skio
import os
import cv2

def genMask(img, maskPercent):
    shape = img.shape
    rows, cols, _ = shape
    rowsCovered, colsCovered = int(rows*maskPercent), int(cols*maskPercent)
    rowsOffset, colsOffset = int((rows-rowsCovered)/2), int((cols-colsCovered)/2)
    mask = np.zeros((rows,cols),dtype=np.uint8)
    mask[rowsOffset:rowsOffset+rowsCovered, colsOffset:colsOffset+colsCovered]=1
    skio.imshow(mask)
    skio.show()
    return mask


def getImages():
    for i in os.listdir("rawImages/"):
        yield cv2.imread("rawImages/"+i)


with open("maskRegression.csv", 'w') as file:
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
       
        

  