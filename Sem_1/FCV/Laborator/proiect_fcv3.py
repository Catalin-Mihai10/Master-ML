import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt

def adjustBrightness(image: cv.Mat, brightness:int):
    copyImage = np.array(image)
    height, width, channels = copyImage.shape
    
    for i in range(height):
        for j in range(width):
            copyImage[i, j] += brightness
    
    return new_image

def blurImage(image: cv.Mat):
    sigma = 4
    imageBlur = cv.GaussianBlur(image, (5,5), sigma)
    return imageBlur

def myBlurImage(image: cv.Mat) :
    #create new image
    image = np.array(image)
    bluredImage = np.zeros(image.shape)
    #get image height and width
    height, width, channels = image.shape

    #pad the image
    paddedImage = np.pad(image, ((4, 4), (4, 4), (0, 0)), mode='edge')

    #define a Gaussian Kernel
    gaussianKernel = np.array([[1, 2, 3, 2, 1],
                               [2, 4, 5, 4, 2],
                               [3, 5, 9, 5, 3],
                               [2, 4, 5, 4, 2],
                               [1, 2, 3, 2, 1]])

    gaussianKernel = np.expand_dims(gaussianKernel, axis=2)
    gaussianKernel = gaussianKernel / np.sum(gaussianKernel)
    gaussianKernel = np.dstack((gaussianKernel, gaussianKernel, gaussianKernel))
    for i in range(height):
        for j in range(width):
            bluredImage[i, j] = np.sum(paddedImage[i:i+5, j:j+5] * gaussianKernel, axis=(0,1))

    return bluredImage
def edgeDetection(image: cv.Mat):
    kernel = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
    depth = -1
    edgeDetectionImage = cv.filter2D(image, depth, kernel)
    return edgeDetectionImage

def opencvTranslation(image: cv.Mat,  newX: int, newY: int):
    #define translation matrix
    translationMatrix = np.float32([[1, 0, newX],
                                  [0, 1, newY]])
    translatedImage = cv.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
    cv.imshow('Translated image', translatedImage)
    cv.waitKey()

def translation(image: cv.Mat, newX: int, newY: int):
     #get the height, width and channels of the image
    height, width, channels = image.shape
    #define the translation matrix
    # shape should be of form:
    translatedImage = np.zeros(image.shape)

    #compute new values
    for i in range(newY, height):
        for j in range(newX, width):
            translatedImage[i, j] = image[i - newY, j - newX]

    return translatedImage

def scaling(image: cv.Mat, new_scale: float):
    #get the height, width and channels of the image
    height, width, channels = image.shape
    newHeight = int((height * new_scale) / 100)
    newWidth = int((width * new_scale) / 100)

    scaledImage = cv.resize(image, (newHeight, newWidth), interpolation= cv.INTER_AREA)
    return scaledImage

def shearing(image: cv.Mat, x: int, y: int):
    #get the height, width and channels of the image
    height, width, channels = image.shape

    #define the transformation Matrix
    matrixX = np.float32([[1, x, 0],
                         [0, 1, 0],
                         [0, 0, 1]])
    matrixY = np.float32([[1, 0, 0],
                         [y, 1, 0],
                         [0, 0, 1]])
    shearedImageX = cv.warpPerspective(image, matrixX, (int(width * (1 + y)), int(height * (1 + x))));
    shearedImageY = cv.warpPerspective(image, matrixY, (int(width * (1 + y)), int(height * (1 + x))));
    return (shearedImageX, shearedImageY)