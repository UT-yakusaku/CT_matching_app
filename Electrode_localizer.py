import pydicom as dicom
import cv2
import os
import tifffile
import numpy as np
import keyboard
from lib import *
from config import *

def main():
    d = {}
    d['idx'] = image_start
    d['points'] = []
    img = read_image(d['idx'])
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    wname = "MouseEvent"
    d['wname'] = wname
    d['img'] = img
    cv2.namedWindow(wname)
    cv2.setMouseCallback(wname, onMouse, d)
    cv2.imshow(wname,img)

    while True:
        if  keyboard.is_pressed("."):
            d['idx'] += 1
            img = read_image(d['idx'])
            cv2.imshow(wname,img)
        if keyboard.is_pressed(","):
            d['idx'] -= 1
            img = read_image(d['idx'])
            cv2.imshow(wname,img)
        while  cv2.waitKey() == ord('q'):
            cv2.destroyAllWindows()
            exit()
            break


if __name__=="__main__":
  main()
