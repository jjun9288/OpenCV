import sys
import random
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch7/data/'



#-----------------------------------------------------------------------------------------------------------
# < 외곽선 검출 >
# 객체의 외곽선 좌표를 모두 추출하는 작업
# - 외곽선 검출
# cv2.findContours(image, mode, method, contours=None, hierarchy=None, offset=None)
#   -mode : 외곽선 검출 모드. cv2.RETR_
#   -method : 외곽선 근사화 방법. cv2.CHAIN_APPROX_
#   -contours : 검출된 외곽선 좌표
#   -hierarchy : 와곽선 계층 정보
#   -offset : 좌표 값 이동 offset. 기본 값은 (0,0)
#
# - 외곽선 그리기
# cv2.drawContours(image, contours, contourIdx, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None, offset=None)
#   -contours : cv2.findContours() 함수로 구한 외곽선 좌표 정보
#   -contourIdx : 외곽선 인덱스. -1을 지정하면 모든 외곽선을 그린다.
#   -color : 외곽선 색상
#   -thickness : 외곽선 두께
#   -lineType : LINE_4, LINE_8, LINE_AA 중 하나 지정
#   -hierarchy : 외곽선 계층 정보
#   -maxLevel : 그리기를 수행할 때 최대 외곽선 레벨. 0이면 contourIdx로 지정된 외곽선만 그린다.
#-----------------------------------------------------------------------------------------------------------

src = cv2.imread(path + 'contours.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

contours, hier = cv2.findContours(src, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

idx = 0
while idx >= 0:
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, idx, c, 2, cv2.LINE_8, hier)
    idx = hier[0, idx, 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
