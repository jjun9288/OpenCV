import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch4/data/'

#-------------------------------------------------------------------------------------------------
# 평균값 필터는 멀리 있는 픽셀의 영햐을 많이 받는다는 단점이 있다.
# 가우시안 분포를 이용하여 이 단점을 극복할 수 있다.
# cv2.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
#   -kernel size는 안 주는게 좋다. sigma에 의해 결정되게 두는 것이 좋다.
#    그래서 ksize에 (0,0)을 지정해두자. 그렇게 하면 sigma 값에 의해 자동 결정된다.
#-------------------------------------------------------------------------------------------------

src = cv2.imread(path + 'rose.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.GaussianBlur(src, (0, 0), 2)
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
