import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch6/data/'


#-----------------------------------------------------------------------------------------------------------
# < Canny edge 검출 >
# cv2.Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
#   -threshold1 : 하단 임계값
#   -threshold2 : 상단 임계값      (보통 threshold1 : threshold2 = 1:2 또는 1:3)
#-----------------------------------------------------------------------------------------------------------




src = cv2.imread(path + 'building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.Canny(src, 50, 150)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
