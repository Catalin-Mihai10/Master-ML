#!/usr/bin/env python3

import cv2 as cv
import sys

image_path_folder = "/home/supreme/Master/Sem_1/FCV/Laborator/test_folder/854061.jpg"
image = cv.imread(image_path_folder)

if image is None:
    sys.exit("Error: the images could not be read!")

cv.imshow("Display Window", image)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(image, 'Ancuta Catalin-Mihai', (10, 450),
           font, 3, (0, 255, 0), 2, cv.LINE_AA)
cv.imwrite(
    "/home/supreme/Master/Sem_1/FCV/Laborator/output_folder/new_854061.jpg", image)
