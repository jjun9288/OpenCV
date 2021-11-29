import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch5/data/'


#------------------------------------------------------------------------------
# < 영상의 회전 >
# cv2.getRotationMatrix2D(center, angle, scale)
#   -center : 회전 중심 좌표
#   -angle : 회전 각도
#   -scale : 추가적인 확대 비율
#------------------------------------------------------------------------------



src = cv2.imread(path + 'tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2)
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)


dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
