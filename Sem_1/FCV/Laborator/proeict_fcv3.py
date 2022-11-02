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

    cv.imshow('Old image', image)
    cv.waitKey()
    cv.imshow('New image', copyImage)
    cv.waitKey()

def blurImage(image: cv.Mat):
    sigma = 4
    imageBlur = cv.GaussianBlur(image, (5,5), sigma)
    cv.imshow('Blured image', imageBlur)
    cv.waitKey()

def myBlurImage(image: cv.Mat) :
    #create new image
    image = np.array(image)
    bluredImage = np.zeros(image.shape)
    #get image height and width
    height, width, channels = image.shape

    #pad the image
    paddedImage = np.pad(image, ((0, 4), (0, 4), (0, 0)), mode='edge')

    #define a Gaussian Kernel
    gaussianKernel = np.array([[1, 2, 3, 2, 1],
                               [2, 4, 5, 4, 2],
                               [3, 5, 9, 5, 3],
                               [2, 4, 5, 4, 2],
                               [1, 2, 3, 2, 1]])
    gaussianKernel = np.divide(gaussianKernel, np.sum(gaussianKernel))
    gaussianKernel = np.expand_dims(gaussianKernel, axis=2)
    gaussianKernel = np.dstack((gaussianKernel, gaussianKernel, gaussianKernel))
    for i in range(height):
        for j in range(width):
            bluredImage[i, j] = np.sum(paddedImage[i:i+5, j:j+5] * gaussianKernel, axis=(0, 1))
    cv.imshow('Blured image', bluredImage)
    cv.waitKey()

def edgeDetection(image: cv.Mat):
    kernel = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
    depth = -1
    edgeDetectionImage = cv.filter2D(image, depth, kernel)
    cv.imshow('Edge Detection', edgeDetectionImage)
    cv.waitKey()

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
                
    cv.imshow('Translated image', translatedImage)
    cv.waitKey()

def scaling(image: cv.Mat, new_scale: float):
    #get the height, width and channels of the image
    height, width, channels = image.shape
    newHeight = int((height * new_scale) / 100)
    newWidth = int((width * new_scale) / 100)

    scaledImage = cv.resize(image, (newHeight, newWidth), interpolation= cv.INTER_AREA)
    cv.imshow('Scaled image', scaledImage)
    cv.waitKey()

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
    cv.imshow('Sheared image on X axis', shearedImageX)
    cv.waitKey()
    shearedImageY = cv.warpPerspective(image, matrixY, (int(width * (1 + y)), int(height * (1 + x))));
    cv.imshow('Sheared image on Y axis', shearedImageY)
    cv.waitKey()

image_path_folder = "/home/supreme/Master/Sem_1/FCV/Laborator/test_folder/854110.jpg"
image = cv.imread(image_path_folder)

#adjustBrightness(image, 10)
#blurImage(image)
#edgeDetection(image)
#translation(image, 10, 10)
opencvTranslation(image, 10, 10)
#scaling(image, 1.6)
#shearing(image, 0.3, 0.3)
#myBlurImage(image)