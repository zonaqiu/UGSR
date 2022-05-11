import cv2 as cv
import os
path = '/data_d/zona/UGSR/datasets/cats/4x/rgb/'
for filename in os.listdir(path):
    # print(filename[:-4])
    # exit(0)
    img=cv.imread(path+filename)
    # res_img=cv.resize(img,(640,480),interpolation=cv.INTER_AREA)
    res_img = cv.resize(img, (640,480))
    cv.imwrite(path+'x4/'+filename,res_img)
