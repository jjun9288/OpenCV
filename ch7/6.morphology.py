import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch7/data/'



#-------------------------------------------------------------------------------------------------------------------
# <Morphology(1) : 침식과 팽창 >
# morphology 연산 : 영상을 형태학적인 측면에서 다루는 기법. 다양한 영상 처리 시스템에서 전처리, 후처리 형태로 널리 사용
# - 침식 연산 : 객체 외곽을 깎아내는 연산. 객체 크기는 감소, 배경은 확대
#   - cv2.erode(src, kernel, anchor=None, iterations=None, borderType=None, borderValue=None)
#       -anchor : 고정점 위치. 기본값은 (-1,-1). 기본값 사용하면 중앙점을 사용
#       -kernel : 구조요소. getStructuringElements() 함수에 의해 생성 가능. None을 지정하면 3x3 사용
#       -iterations : 반복 횟수. 기본값은 1
#       -borderType : 가장자리 픽셀 확장 방식. 기본값은 cv2.BORDER_CONSTANT
#       -borderValue : cv2.BORDER_CONSTANT인 경우, 확장된 가장자리 픽셀을 채울 값
#
# - 팽창 연산 : 객체 외곽을 확대시키는 연산. 객체 크기는 증가, 배경은 감소
#   -cv2.dilate(src, kernel, anchor=None, iterations=None, borderType=None, borderValue=None)
#
#   -cv2.getStructuringElements(shape, ksize, anchor=None)
#       -shape  -cv2.MORPH_RECT : 사각형 모양
#               -cv2.MORPH_CROSS : 십자가 모양
#               -cv2.MORPH_ELLIPSE : 사각형에 내접하는 타원
#       -ksize : 구조 요소 크기 (width, height) 튜플
#       -anchor : 고정점 좌표
#-------------------------------------------------------------------------------------------------------------------

src = cv2.imread(path + 'circuit.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
dst1 = cv2.erode(src, se)

dst2 = cv2.dilate(src, None)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
