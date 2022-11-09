import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt

def adjustBrightness(image, brightness):
    copyImage = image * (brightness / 100)
    return copyImage

def blurImage(image):
    sigma = 4
    imageBlur = cv.GaussianBlur(image, (5,5), sigma)
    return imageBlur

def myBlurImage(image) :
    bluredImage = np.zeros(image.shape)
    paddedImage = np.pad(image, ((4, 4), (4, 4), (0, 0)), mode='edge')
    gaussianKernel = np.array([[1, 2, 3, 2, 1],
                               [2, 4, 5, 4, 2],
                               [3, 5, 9, 5, 3],
                               [2, 4, 5, 4, 2],
                               [1, 2, 3, 2, 1]])
    gaussianKernel = np.divide(gaussianKernel, np.sum(gaussianKernel))
    gaussianKernel = np.expand_dims(gaussianKernel, axis=2)
    gaussianKernel = np.dstack((gaussianKernel, gaussianKernel, gaussianKernel))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            blurMatrix = paddedImage[i:i+5, j:j+5] * gaussianKernel
            bluredImage[i, j] = np.sum(blurMatrix, axis=(0,1))

    return bluredImage

def edgeDetection(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
    depth = -1
    edgeDetectionImage = cv.filter2D(image, depth, kernel)
    return edgeDetectionImage

def opencvTranslation(image,  newX, newY):
    translationMatrix = np.float32([[1, 0, newX],
                                  [0, 1, newY]])
    translatedImage = cv.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
    return translatedImage

def translation(image, newX, newY):
    translatedImage = np.zeros(image.shape)

    for i in range(newY, image.shape[0]):
        for j in range(newX, image.shape[1]):
            translatedImage[i, j] = image[i - newY, j - newX]

    return translatedImage

def scaling(image, new_scale):
    newHeight = int((image.shape[0] * new_scale) / 100)
    newWidth = int((image.shape[1] * new_scale) / 100)

    scaledImage = cv.resize(image, (newHeight, newWidth), interpolation= cv.INTER_AREA)
    return scaledImage

def shearing(image, x, y):
    matrixX = np.float32([[1, x, 0],
                         [0, 1, 0],
                         [0, 0, 1]])
    matrixY = np.float32([[1, 0, 0],
                         [y, 1, 0],
                         [0, 0, 1]])
    shearedImageX = cv.warpPerspective(image, matrixX, (int(image.shape[1] * (1 + y)), int(image.shape[0] * (1 + x))));
    shearedImageY = cv.warpPerspective(image, matrixY, (int(image.shape[1] * (1 + y)), int(image.shape[0] * (1 + x))));
    return (shearedImageX, shearedImageY)