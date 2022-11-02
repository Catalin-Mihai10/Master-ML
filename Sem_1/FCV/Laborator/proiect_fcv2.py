#!/usr/bin/env python3

from tkinter import image_names
import cv2 as cv
import os
import tkinter.filedialog as tk
import sys
import configparser as cp

# Global variables
config_file = "/home/supreme/Master/Sem_1/FCV/Laborator/project.ini"
output_dir = "/home/supreme/Master/Sem_1/FCV/Laborator/output_folder/"

#read the configurations
configs = cp.ConfigParser()
configs.read(config_file)
configSection = configs['DEFAULT']
if not configSection:
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

def augment(image: cv.Mat, augmentsVector: cp.SectionProxy, imageName: str):
    iterator = 0
    #iterate through the augmentation array    
    for augment in augmentsVector:
        #make a match-case statement to check which 
        #augmentation it is.
        print(augment)
        match augment:
            case 'dummy':
                #increase the index
                iterator += 1
                #apply the augmentation
                rotate_value = augmentsVector.get('dummy')
                print(rotate_value)
                rotated_image = cv.rotate(image, int(rotate_value))
                if removeFormat(imageName):
                    stripImageFormat = imageName.rstrip('.png')
                    augmentedImageName = output_dir + stripImageFormat + augment + '{}.png'.format(iterator)
                else:
                    stripImageFormat = imageName.rstrip('.jpg')
                    augmentedImageName = output_dir + stripImageFormat + augment + '{}.jpg'.format(iterator)
                #write augmented image to the output directory.
                cv.imwrite(augmentedImageName, image)
                break!

def augmentFile(path: str, augments: list[str]):
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
        augmentFile(file, configSection)
