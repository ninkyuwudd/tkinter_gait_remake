


import cv2
import numpy as np


def calculatingSobelForGfGei(gei_image):
    sobelx = cv2.Sobel(gei_image, cv2.CV_64F, 1, 0, ksize=3) 
    sobely = cv2.Sobel(gei_image, cv2.CV_64F, 0, 1, ksize=3) 
    # orientation_angel = np.arctan2(sobely,sobelx)
    sobel_calculated = cv2.magnitude(sobelx, sobely)

    sobel_normalization = cv2.convertScaleAbs(sobel_calculated)
    return sobel_normalization

def newGGMIcalculated(frame_list):
    gei = np.mean(frame_list,axis=0)
    sigma = 1
    smoothed_image = cv2.GaussianBlur(gei, (3, 3), sigma)
    sobel = calculatingSobelForGfGei(smoothed_image)
    return sobel