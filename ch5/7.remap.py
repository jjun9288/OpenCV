import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch5/data/'



#-----------------------------------------------------------------------------------------------------------
# < 리매핑 >
# cv2.remap(src, map1, map2, interpolation, borderMode=None, borderValue=None)
#   -map1 : 결과 영상의 (x,y) 좌표가 참조할 입력 영상의 x좌표
#   -map2 : 결과 영상의 (x,y) 좌표가 참조할 입력 역상의 y좌표
#   -borderMode : 가장자리 픽셀 확장 방식 (기본 값은 cv2.BORDER_CONSTANT)
#   -borderValue : cv2.BORDER_CONSTANT일 때 사용할 상수 값. 기본 값은 0.
#-----------------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

map2, map1 = np.indices((h, w), dtype=np.float32)
map2 = map2 + 10 * np.sin(map1 / 32)

dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
