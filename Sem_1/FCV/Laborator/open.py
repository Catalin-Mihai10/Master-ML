import cv2 as cv

bright = cv.imread("/home/supreme/Master/Sem_1/FCV/Laborator/output_folder/jonny-gios-86GgTVZ9q-0-unsplashbrightness1.jpg")
cv.imshow('Brightness', bright)
cv.waitKey()

blur = cv.imread("/home/supreme/Master/Sem_1/FCV/Laborator/output_folder/jonny-gios-86GgTVZ9q-0-unsplashblur2.jpg")
cv.imshow('Blur', blur)
cv.waitKey()

edge = cv.imread("/home/supreme/Master/Sem_1/FCV/Laborator/output_folder/jonny-gios-86GgTVZ9q-0-unsplashedge3.jpg")
cv.imshow('Brightness', edge)
cv.waitKey()

translation = cv.imread("/home/supreme/Master/Sem_1/FCV/Laborator/output_folder/jonny-gios-86GgTVZ9q-0-unsplashtranslation4.jpg")
cv.imshow('Image', translation)
cv.waitKey()