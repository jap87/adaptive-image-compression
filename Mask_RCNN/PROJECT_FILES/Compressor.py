import cv2
import numpy as np
import skimage.io as skio
import os


HYBRID_FILE = "hybrid.png"
LOSSLESS_FILE = "lossless.png"
LOSSY_FILE = "lossy.jpg"

ROOT_DIR = os.path.abspath("..")
UPLOAD_FOLDER = '/images/'

# ROOT_DIR = os.path.abspath("./")
# UPLOAD_FOLDER = '/'

#Usage:

# testImage = 'kodim12.png'
# testMask = 'mask.png'
# compressImage(ROOT_DIR+UPLOAD_FOLDER+testImage, ROOT_DIR+UPLOAD_FOLDER+testMask, quality = 50)

def compressImage(image, mask, quality=50):
    '''
        image: Image that should be compressed, can be either a 3d numpy array or a string of the filepath of an image
        mask: Mask that positively defines area of high-quality, can be either a 2d numpy array or a string of the filepath of an image
        quality: 0 - 100 level of compression (higher means better)
    '''
    if isinstance(mask, str):
        mask = cv2.imread(mask,0)

    baseline = genPNG(image)
    compressed = genJPG(baseline, quality)
    highQuality = cv2.bitwise_and(baseline,baseline, mask = mask)
    negativeMask = cv2.bitwise_not(mask)
    lowQuality = cv2.bitwise_and(compressed,compressed, mask = negativeMask)
    hybrid = lowQuality + highQuality
    tempDir = HYBRID_FILE
    save(tempDir, hybrid, png_compression=9)

    path = ROOT_DIR+UPLOAD_FOLDER
    files = [HYBRID_FILE, LOSSY_FILE, LOSSLESS_FILE]

    out = {file : getFileSize(path+file) for file in files}
    return out
    
    
def genJPG(image, quality):
    '''
        img: Image that should be compressed, can be either a 3d numpy array or a string of the filepath of an image
        quality: 0 - 100 level of compression (higher means better)
    '''
    tempDir = LOSSY_FILE
    save(tempDir, image, jpg_quality=quality)
    out = cv2.imread(tempDir)
    return out

def genPNG(image):
    '''
        img: Image that should be compressed, can be either a 3d numpy array or a string of the filepath of an image
    '''
    tempDir = LOSSLESS_FILE
    save(tempDir, image, png_compression=9)
    out = cv2.imread(tempDir)
    return out

def save(fileName, image, jpg_quality=None, png_compression=None):
    '''
        persist: image: object to disk. if path is given, load() first.
        jpg_quality: for jpeg only. 0 - 100 (higher means better). Default is 95.
        png_compression: For png only. 0 - 9 (higher means a smaller size and longer compression time).
                        Default is 3.
    '''
    path = ROOT_DIR+UPLOAD_FOLDER+fileName
    if isinstance(image, str):
        image = cv2.imread(image)
    if jpg_quality:
        cv2.imwrite(path, image, [cv2.IMWRITE_JPEG_QUALITY, jpg_quality])
    elif png_compression:
        cv2.imwrite(path, image, [cv2.IMWRITE_PNG_COMPRESSION, png_compression])
    else:
        cv2.imwrite(path, image)

def getFileSize(path):
    return os.path.getsize(path)


#Usage:

testImage = 'kodim12.png'
testMask = 'mask.png'
compressImage(ROOT_DIR+UPLOAD_FOLDER+testImage, ROOT_DIR+UPLOAD_FOLDER+testMask, quality = 50)
