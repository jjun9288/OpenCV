import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch5/data/'



#-------------------------------------------------------------------------------------------------
# < 이미지 피라미드 > 
# - 영상 피라미드 다운샘플링
# cv2.pryDown(src)
#
# - 영상 피라미드 업샘플링
# cv2.pyyUp(src)
#-------------------------------------------------------------------------------------------------




src = cv2.imread(path + 'cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple (x 좌표, y 좌표, width, height)

# 원본 영상에 그리기
cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드 영상에 그리기
for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()
