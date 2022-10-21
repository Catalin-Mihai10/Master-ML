import cv2 as cv
import numpy as np
import sys
from matplotlib import pyplot as plt

def adjustBrightness(image: cv.Mat, brightness:int):
    hSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    height, width, channels = image.shape
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                hSV[i][j][k] += brightness

    new_image = cv.cvtColor(hSV, cv.COLOR_HSV2BGR)
    cv.imshow('Old image', image)
    cv.waitKey()
    cv.imshow('New image', new_image)
    cv.waitKey()

def blurImage(image: cv.Mat):
    sigma = 4
    imageBlur = cv.GaussianBlur(image, (5,5), sigma)
    cv.imshow('Blured image', imageBlur)
    cv.waitKey()

def edgeDetection(image: cv.Mat):
    kernel = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
    depth = -1
    edgeDetectionImage = cv.filter2D(image, depth, kernel)
    cv.imshow('Edge Detection', edgeDetectionImage)
    cv.waitKey()

def translation(image: cv.Mat, newX: int, newY: int):
    #get the height, width and channels of the image
    height, width, channels = image.shape
    #define the translation matrix
    # shape should be of form:
    translationMatrix = np.array([[1, 0, newX], [0, 1, newY]])
    translatedImage = np.zeros(image.shape)

    #compute new values
    for i in range(height - newY):
        for j in range(width - newX):
            for k in range(channels):
                origin = np.array([i, j, 1])
                translation_values = np.dot(translationMatrix, origin)

                if translation_values[0] >= 0 and translation_values[0] < width and translation_values[1] >= 0 and translation_values[1] < height:
                    translatedImage[translation_values[0], translation_values[1]] = image[i, j]
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

image_path_folder = "/home/supreme/Master/Sem_1/FCV/Laborator/test_folder/854061.jpg"
image = cv.imread(image_path_folder)

#adjustBrightness(image, 10)
#blurImage(image)
#edgeDetection(image)
translation(image, 1, 1)
scaling(image, 1.6)
shearing(image, 0.3, 0.3)
