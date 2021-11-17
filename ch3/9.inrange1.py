import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch3/data/'


#-------------------------------------------------------------------------------------------------------------------
# < 특정 색상 영역 추출 >
# cv2.inRange(src, lowerb, upperb, dst=None)
#   -lowerb : 하한 값 행렬 또는 스칼라   
#   -upperb : 상한 값 행렬 또는 스칼라
#-------------------------------------------------------------------------------------------------------------------


src = cv2.imread(path + 'candies.png')


if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))             # 0 <= R < 100 / 128 <= G < 255 / 0 <= B < 100  (초록색 부분만 추출)
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))         # 50 <= H < 80 / 150 <= S < 255 / 0 <= V < 255  (초록색 부분만 추출)
                                                                  # 50~80이 초록색 구간, S는 선명도. V는 밝기 정도. 즉, S를 150~로 두는 것은
                                                                  # 선명도를 높게 주겠다는 것이고, V는 0~255 이므로 신경쓰지 않겠다는 것이다.
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
