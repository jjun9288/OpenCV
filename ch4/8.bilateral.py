import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch4/data/'


#---------------------------------------------------------------------------------
# < 잡음 제거 : 양방향 필터링 >
# - 가우시안 필터와는 다르게 특정 edge는 살리는 모습을 볼 수 있다.
# - 그래서 blur를 해도 이미지의 형태를 어느정도 지킬 수 있다.
# - cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, borderType=None)
#   - d : 필터링에 사용될 이웃 픽셀의 거리 (음수를 입력하면 sigmaspace 값에 의해 자동 처리)
#   - sigmaColor : 색 공간에서 필터의 표준편차  (10~20 정도 주는게 좋다)
#   - sigmaSpace : 좌표 공간에서 필터의 표준편차  (3~5 정도 주는게 좋다)
#---------------------------------------------------------------------------------



src = cv2.imread(path + 'lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
