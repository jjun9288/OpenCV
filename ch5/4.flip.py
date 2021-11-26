import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch5/data/'

#-------------------------------------------------------------------------------------------------
# < 영상의 대칭 >
# cv2.flip(src, flipCode)
#   -flipCode : 대칭 방향 지정 (양수(+1) : 좌우 대칭, 0 : 상하 대칭, 음수(-1) : 좌우&상하 대칭)
#-------------------------------------------------------------------------------------------------

src = cv2.imread(path + 'rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()
    
    
dst1 = cv2.flip(src, 1)
dst2 = cv2.flip(src, 0)
dst3 = cv2.flip(src, -1)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()