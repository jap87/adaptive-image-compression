import os
import sys
import numpy as np
import skimage.io as skio
import time
import Compressor
import cv2
import csv

def genMask(img, maskPercent):
    shape = img.shape
    rows, cols, _ = shape
    rowsCovered, colsCovered = int(rows*maskPercent), int(cols*maskPercent)
    rowsOffset, colsOffset = int((rows-rowsCovered)/2), int((cols-colsCovered)/2)
    mask = np.zeros((rows,cols),dtype=np.uint8)
    mask[rowsOffset:rowsOffset+rowsCovered, colsOffset:colsOffset+colsCovered]=1
    return mask

    i = 5
    while i < 96:
    
        for  root, dirs, files in os.walk('./rawImages/'):
            for name in files:
                img = skio.imread('./rawImages/'+name)
                results = Compressor.compressImage('./rawImages/'+name, genMask(img, .4), i)
                params = list(results.values())
                print(name + ',' + str(params[0]) + ',' + str(params[1]) + ',' + str(i))

        i = i + 3
