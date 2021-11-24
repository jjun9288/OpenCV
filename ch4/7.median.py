import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch4/data/'


#-----------------------------------------------------------------------------------------------------
# < 잡음 제거 : Median filter >
# - 주변 픽셀들의 값들을 정렬하여 그 중앙값으로 픽셀 값을 대체 (소금-후추 잡음 제거에 효과적)
# - cv2.medianBlur(src, ksize)
#-----------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
