#!/usr/bin/env python3

from tkinter import image_names
import cv2 as cv
import os
import tkinter.filedialog as tk
import sys
import configparser as cp
import proiect_fcv3 as augFun

# Global variables
config_file = "/home/supreme/Master/Sem_1/FCV/Laborator/project.ini"
output_dir = "/home/supreme/Master/Sem_1/FCV/Laborator/output_folder/"

#read the configurations
configs = cp.ConfigParser()
configs.read(config_file)
for section in configs.sections():
    print(section)
    for option in configs.options(section):
        configurations = configs.get(section, option)
        dictionary = dict(x.split('=') for x in configurations.split(','))
        print(dictionary)
if not dictionary:
    sys.exit("Error: The configuration list is empty!")

#functions section
def removeFormat(imageFormat: str):
    if hasattr(imageFormat, '.png'):
        return True
    elif hasattr(imageFormat, '.jpg'):
        return False

def formatImageName(imageFormat: str):
    if removeFormat(imageFormat):
        stripImageFormat = imageFormat.rstrip('.png')
        newFormat = stripImageFormat + '_aug.png' 
    else:
        stripImageFormat = imageFormat.rstrip('.jpg')
        newFormat = stripImageFormat + '_aug.jpg'
    return newFormat

def augment(image: cv.Mat, augmentsVector: dict[str, str], imageName: str):
    iterator = 0
    #iterate through the augmentation array
    for key in augmentsVector.keys():
        #make a match-case statement to check which 
        #augmentation it is.
        print(key)
        match key:
            case 'brightness':
                #increase the index
                iterator += 1
                #apply the augmentation
                rotated_image = augFun.adjustBrightness(image, int(augmentsVector[key]))
                if removeFormat(imageName):
                    stripImageFormat = imageName.rstrip('.png')
                    augmentedImageName = output_dir + stripImageFormat + key + '{}.png'.format(iterator)
                else:
                    stripImageFormat = imageName.rstrip('.jpg')
                    augmentedImageName = output_dir + stripImageFormat + key + '{}.jpg'.format(iterator)
                #write augmented image to the output directory.
                cv.imwrite(augmentedImageName, image)
            case 'blur':
                iterator += 1
                
                if(bool(dictionary[key]) == True):
                    blurImage = augFun.blurImage(image)
                    if removeFormat(imageName):
                        stripImageFormat = imageName.rstrip('.png')
                        augmentedImageName = output_dir + stripImageFormat + key + '{}.png'.format(iterator)
                    else:
                        stripImageFormat = imageName.rstrip('.jpg')
                        augmentedImageName = output_dir + stripImageFormat + key + '{}.jpg'.format(iterator)
                    #write augmented image to the output directory.
                    cv.imwrite(augmentedImageName, image)
            case 'edge':
                iterator += 1

                if(bool(dictionary[key]) == True):
                    edgeDetection = augFun.edgeDetection(image)

                    if removeFormat(imageName):
                        stripImageFormat = imageName.rstrip('.png')
                        augmentedImageName = output_dir + stripImageFormat + key + '{}.png'.format(iterator)
                    else:
                        stripImageFormat = imageName.rstrip('.jpg')
                        augmentedImageName = output_dir + stripImageFormat + key + '{}.jpg'.format(iterator)
                    #write augmented image to the output directory.
                    cv.imwrite(augmentedImageName, image)
            case 'translation':
                iterator += 1

                translationValues = augmentsVector[key].split(' ')
                translateX = translationValues[0]
                translateY = translationValues[1]
                
                translatedImage = augFun.translation(image, int(translateX), int(translateY))
                if removeFormat(imageName):
                    stripImageFormat = imageName.rstrip('.png')
                    augmentedImageName = output_dir + stripImageFormat + key + '{}.png'.format(iterator)
                else:
                    stripImageFormat = imageName.rstrip('.jpg')
                    augmentedImageName = output_dir + stripImageFormat + key + '{}.jpg'.format(iterator)
                #write augmented image to the output directory.
                cv.imwrite(augmentedImageName, image)
            case 'scaling':
                iterator += 1

                scaledImage = augFun.scaling(image, float(augmentsVector[key]))
                if removeFormat(imageName):
                    stripImageFormat = imageName.rstrip('.png')
                    augmentedImageName = output_dir + stripImageFormat + key + '{}.png'.format(iterator)
                else:
                    stripImageFormat = imageName.rstrip('.jpg')
                    augmentedImageName = output_dir + stripImageFormat + key + '{}.jpg'.format(iterator)
                #write augmented image to the output directory.
                cv.imwrite(augmentedImageName, image)
            case 'shearing':
                iterator += 1

                shearingValues = augmentsVector[key].split(' ')
                print(shearingValues)
                shearingX = shearingValues[0]
                shearingY = shearingValues[1]
                shearedImageOnX, shearedImageOnY = augFun.shearing(image, int(shearingX), int(shearingY))
                
                if removeFormat(imageName):
                    stripImageFormat = imageName.rstrip('.png')
                    augmentedImageName = output_dir + stripImageFormat + key + '{}.png'.format(iterator)
                else:
                    stripImageFormat = imageName.rstrip('.jpg')
                    augmentedImageName = output_dir + stripImageFormat + key + '{}.jpg'.format(iterator)
                #write augmented image to the output directory.
                cv.imwrite(augmentedImageName, image)

def augmentFile(path: str, augments: dict[str, str]):
    #open file, read them as an image and the call the augment procedure. After
    #that write the augmented image to the output directory.
    image = cv.imread(path)
    if image is None:
        sys.exit("Error: Could not read the image!")
    imageName = formatImageName(path)
    augment(image, augments, path)
    newFileName = output_dir + imageName
    writeValue = cv.imwrite(newFileName, image)
    if not writeValue:
        sys.exit("Error: Could not save the augmented image!")

# create new window
root = tk.Tk()
root.withdraw()
# ask for directory selection
images_directory = tk.askdirectory()
if images_directory is None:
    sys.exit("Error: Could not save the augmented image!")
root.destroy()

#go to the selected directory
os.chdir(images_directory)
filesList = os.listdir()
if not filesList:
    sys.exit("Error: There are no files in the directory!")

# iterate through every file
for file in os.listdir():
    # iterate through each file
    if file.endswith('.jpg') or file.endswith('.png'):
        #call the augmentation procedure
        augmentFile(file, dictionary)
