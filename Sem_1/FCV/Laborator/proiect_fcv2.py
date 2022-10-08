#!/usr/bin/env python3

from email.policy import default
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
configList = configs.read(config_file)
if not configList:
    sys.exit("Error: The configuration list is empty!")

#functions section
def augment(image, augmentsVector):
    iterator = 0
    #iterate through the augmentation array    
    for augment in augmentsVector:
        #make a match-case statement to check which 
        #augmentation it is.
        match augment:
            case 'dummy':
                #increase the index
                iterator += 1
                #apply the augmentation
                rotated_image = cv.rotate(image, augment.get('dummy'))
                #write augmented image to the output directory.
                cv.imwrite(output_dir + image + augment + iterator, rotated_image)
                break
                
def augmentFile(path, augments):
    #open file, read them as an image and the call the augment procedure. After
    #that write the augmented image to the output directory.
    image = cv.imread(path)
    if not image:
        sys.exit("Error: Could not read the image!")
    augment(image, augments)
    writeValue = cv.imwrite(output_dir + path + '_aug', image)
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
    if file.endswith('.txt') or file.endswith('.png'):
        #call the augmentation procedure
        augmentFile(file, configs['DEFAULT'])
