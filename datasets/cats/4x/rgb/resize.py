import cv2 as cv
import os
path = '/dataz_d/zona/UGSR/datasets/cats/x4/rgb'
for filename in os.listdir(path):
    print(filename[:-4])
    exit(0)
    img=cv.imread(path+filename)
    res_img=cv.resize(img,(640,480))
    cv.imwrite(path+filename,res_img)
