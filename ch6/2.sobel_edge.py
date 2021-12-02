import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch6/data/'



#-----------------------------------------------------------------------------------------------------------
# < gradient와 edge 검출 >
# 
# - 2D 벡터의 크기 계산 함수
# cv2.magnitude(x, y, magnitude=None)
#   -x : 2D 벡터의 x좌표 행렬
#   -y : 2D 벡터의 y좌표 행렬
#   -magnitude : 2D 벡터의 크기 행렬
#-----------------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

dst = np.zeros(src.shape[:2], np.uint8)
dst[mag > 120] = 255
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
