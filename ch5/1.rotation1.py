import sys
import math
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch5/data/'


#--------------------------------------------------------------------------------------------------------------
# < 영상의 이동변환과 전단변환 >
# - cv2.warpAffine(src, M, dsize)
#   - M : 2x3 어파인 변환 행렬
#   - dsize : 결과 영상 크기. (w, h) 인데 (0,0) 을 넣으면 src와 같은 크기
#--------------------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

#이동변환
aff = np.array([[1,0,200], [0,1,100]], dtype=np.float32)               # 2x3 어파인 변환 행렬을 [[1,0,a], [0,1,b]] 형태가 되어야 함

#전단변환
rad = 20 * math.pi / 180
aff2 = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0, 0))
dst2 = cv2.warpAffine(src, aff2, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
