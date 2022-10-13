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

image_path_folder = "/home/supreme/Master/Sem_1/FCV/Laborator/test_folder/854061.jpg"
image = cv.imread(image_path_folder)

adjustBrightness(image, 10)
blurImage(image)
edgeDetection(image)