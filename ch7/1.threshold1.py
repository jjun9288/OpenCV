import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch7/data/'


#-----------------------------------------------------------------------------------------------------------
# < 영상의 이진화 >
# 영상의 픽셀 값을 0 또는 255로 만드는 연산
# cv2.threshold(src, thresh, maxval, type)
#   -thresh : 사용자 지정 임계값
#   -maxval : cv2.THRESH_BINARY 또는 cv2.THRESH_BINARY_INV 방법 사용 시 최댓값. 보통 255로 지정
#   -type : cv2.THRESH_로 시작하는 플래그
#-----------------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'cells.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, dst1 = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)   # _은 뒤에서 배울 otsu
_, dst2 = cv2.threshold(src, 210, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
