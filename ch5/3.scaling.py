import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch5/data/'



#-------------------------------------------------------------------------------------------------------------------------------------------
# < 영상의 확대와 축소 >
# - cv2.resize(src, dsize, fx=None, fy=None, interpolation=None)
#   - dsize : 결과 영상 크기. (0,0) 이면 fx와 fy값을 이용하여 결정
#   - fx, fy : x와 y방향 스케일 비율 (dsize 값이 0일 때 사용)
#   - interpolation : 보간법 지정. 기본값은 cv2.INTER_LINEAR
#           -cv2.INTER_NEAREST : 최근방 이웃 보간법
#           -cv2.INTER_LINEAR : 양선형 보간법 (2x2 이웃 픽셀 참조)
#           -cv2.INTER_CUBIC : 3차회선 보간법 (4x4 이웃 픽셀 참조)
#           -cv2.INTER_LANCZOS4 : Lanczos 보간법 (8x8 이웃 픽셈 참조). 
#                                         4 -> 16 -> 64개의 픽셀을 쓰므로 퀄리티는 올라가지만 연산 속도가 더 걸린다는 단점이 있다.
#           -cv2.INTER_AREA : 영상 축소 시 효과적
#
# - 영상 축소 시 고려할 사항
#     영상 축소 시 디테일이 사라지는 경우가 발생한다. 그래서 축소 시 입력 영상을 부드럽게 필터링한 후 축소하거나, 다단계로 축소해야 한다.
#     cv2.resize 함수에서는 cv2.INTER_AREA 사용하는 것을 추천
#-------------------------------------------------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800])           #출력 이미지가 커서 일부분만 보여주는 코드
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800]) 
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()