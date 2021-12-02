import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch6/data/'



#-----------------------------------------------------------------------------------------------------------
# < 영상의 미분과 소벨 필터 >
# - 에지 검출 방법 : 영상을 (x,y) 변수의 함수로 간주했을 때,  1차 미분 값이 크게 나타나는 부분 검출
#       - 중앙 차분 : dI/dx = (I(x+h) - I(x-h)) / 2h
#
# - 소벨 필터
#   - 다양한 미분 마스크 
#       - Prewitt, Sobel, Scharr (Sobel을 가장 많이 사용한다)
#
# - 소벨 필터를 이용한 미분 함수
# cv2.Sobel(src, ddepth, dx, dy, ksize=None, scale=None, delta=None, borderType=None)
#   -ddepth : 출력 영상 데이터 타입. -1을 주면 입력 영상과 같은 데이터 타입 (ex : cv2.CV_32F)
#   -dx : x 방향 미분 차수
#   -dy : y 방향 미분 차수
#   -ksize : kernel 사이즈. 기본값은 3
#   -scale : 연산 결과에 추가적으로 곱할 값. 기본값은 1
#   -delta : 연산 결과에 추가적으로 더할 값. 기본값은 0
#-----------------------------------------------------------------------------------------------------------




src = cv2.imread(path + 'lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
