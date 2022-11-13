import os
import pytesseract
import cv2

path_dir = "img of the path"


def files(opt):
    file = open('file.txt','w+')
    file.write(opt)
    file.close()

def img_p(path_dir):
    img = cv2.imread(path_dir)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    opt = pytesseract.image_to_string(gray)
    files(opt)

img_p(path_dir)

