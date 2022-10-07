#!/usr/bin/env python3

import cv2 as cv
import tkinter.filedialog as tk
import sys

# config file path
config_file = "/home/supreme/Master/Sem_1/FCV/Laborator/project.config"

# create new window
root = tk.Tk()
root.withdraw()
# load the config file.
configs = tk.askopenfile(parent=self, title="Open config file",
                         initialdir=config_file, filetypes=('text files', '*.config'))
# ask for directory selection
images_directory = tk.askdirectory(mustexist=True)
# load the files in the directory
files = tk.askopenfilenames(initialdir=images_directory, title="Select image files", filetypes=(
    ("Image files", "*.jpg;*.png"), ("all files", "*.*")))
root.mainloop()

if files is None:
    sys.exit("Error: the images could not be read!")

# iterate through every file
with open(files, encoding="utf-8") as file:
    # read the file as an image
    cv.imread(file)
