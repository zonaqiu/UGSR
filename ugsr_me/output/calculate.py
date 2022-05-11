import os
from imageio import imread
from PIL import Image
import numpy as np
import math
import cv2



def calculate_psnr(img1, img2):
    # img1 and img2 have range [0, 255]
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return float('inf')
    return 20 * math.log10(255.0 / math.sqrt(mse))
def ssim(img1, img2):
    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2

    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())

    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()



def calculate_ssim(img1, img2):
    '''calculate SSIM
    the same outputs as MATLAB's
    img1, img2: [0, 255]
    '''
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    if img1.ndim == 2:
        return ssim(img1, img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(img1, img2))
            return np.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim(np.squeeze(img1), np.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')

HR_path = '/data_d/zona/data/align/test_IR/'
SR_path = './flir_test_20220419_211821/outputs/'
total_num = 0
total_psnr = 0.
total_ssim = 0.

for HR_filename in os.listdir(HR_path):
    # print(HR_filename[:-4])
    # exit(0)
    SR_filename = HR_filename[:-4]+'png'
    SR_img = cv2.imread(SR_path+SR_filename) # 0-255
    HR_img = cv2.imread(HR_path+HR_filename) # 0-255
    total_num += 1
    cur_psnr = calculate_psnr(SR_img,HR_img)
    cur_ssim = calculate_ssim(SR_img,HR_img)
    total_psnr += cur_psnr
    total_ssim += cur_ssim
    print('current psnr is :',cur_psnr)
    print('current ssim is :',cur_ssim)

avg_psnr = total_psnr / total_num
avg_ssim = total_ssim / total_num
print('the number of images is :',total_num)
print('average psnr is :',avg_psnr)
print('average ssim is :',avg_ssim)
