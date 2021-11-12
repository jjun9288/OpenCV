import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch3/data/'


#------------------------------------------------------------------------------------------------------------------------
# < 컬러 영상과 색 공간 >

#1. 채널 분리
#cv2.split(m, mv=None)
#   - m : 다채널 영상(B,G,R)으로 구성된 컬러 영상
#   - mv : 출력 영상

#2. 채널 결합
#cv2.merge(mv, dst=None)
#- 영상 처리에서는 특정 목적을 위해 RGB 색공간을 HSV, YCrCb, Grayscale 등의 다른 색 공간으로 변환하여 처리

#3. 색 공간 변환 함수
#cv2.cvtColor(src, code, dst=None, dstCn=None)
#   - src : 입력 영상
#   - code : 색 변환 코드
#       - cv2.COLOR_BGR2GRAY / cv2.COLOR_GRAY2BGR
#       - cv2.COLOR_BGR2RGB / cv2.COLOR_RGB2BGR
#       - cv2.COLOR_BGR2HSV / cv2.COLOR_HSV2BGR
#       - cv2.COLOR_BGR2YCrCb / cv2.COLOR_YCrCb2BGR

#- RGB 색상을 grayscale로 변환 : Y = 0.299R + 0.587G + 0.114B (3:6:1의 비율로 생각하면 된다)
#   데이터 저장 용량 감소, 데이터 처리 속도가 향상하지만 컬러 정보가 중요하지 않을 때에만 해당된다.

# HSV, YCrCb 정리 간단하게..
#------------------------------------------------------------------------------------------------------------------------



# 컬러 영상 불러오기
src = cv2.imread(path + 'candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

# RGB 색 평면 분할
b_plane, g_plane, r_plane = cv2.split(src)

#b_plane = src[:, :, 0]     # 이미지에서 파란색 부분이 굉장히 밝게 나온다.
#g_plane = src[:, :, 1]     # 이미지에서 초록색 부분이 굉장히 밝게 나온다.
#r_plane = src[:, :, 2]     # 이미지에서 빨간색 부분이 굉장히 밝게 나온다.

cv2.imshow('src', src)
cv2.imshow('B_plane', b_plane)
cv2.imshow('G_plane', g_plane)
cv2.imshow('R_plane', r_plane)
cv2.waitKey()

cv2.destroyAllWindows()
