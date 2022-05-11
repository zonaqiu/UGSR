import os
import shutil
from imageio import imread, imwrite
from PIL import Image
import numpy as np
# path为批量文件的文件夹的路径

path_1 = './flir_test_20220419_211821/20220427-134431/imgs/'
path_2 = './flir_test_20220419_211821/outputs/'
# 文件夹中所有文件的文件名
# file_names_2 = '_network_densefuse_addition_1e0.png'
index = 0
for filename in os.listdir(path_1):
    # filename_1 = os.path.splitext(filename)[1]  # 文件名后缀
    filename_1 = os.path.splitext(filename)[0] # 文件名
    # print(filename_1[0:12])
    # exit(0)

    if filename_1[18:24] == 'output':
        # img = imread(path_1+filename)
        # print(img.shape) # 512 * 640

        full_path = os.path.join(path_1,filename)
        despath = path_2 + filename_1[0:12]+'.png'
        shutil.copyfile(full_path,despath)
        index = index + 1

print('total',index)