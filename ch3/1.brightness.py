import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch3/data/'


#------------------------------------------------------------------------------------------------------------------------
# < 영상의 밝기 조절 >
# - 기본적인 화소 처리 기법은 dst(x,y) = f(src(x,y)).  여기서 dst는 destination, src는 source
# - 영상의 밝기 조절 dst(x,y) = f(src(x,y)) + n.  여기서 +n에 의해 0보다 작아지는 구간은 0으로, 255보다 커지는 구간은 255로 세팅해야 한다.
# cv2.add(src1, src2, dst=None, mask=None, dtype=None)
#   - 참고사항
#       - scalar는 실수 값 하나 또는 실수 값 네 개로 구성된 튜플!
#------------------------------------------------------------------------------------------------------------------------


# 그레이스케일 영상 불러오기
src = cv2.imread(path + 'lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
    
dst = cv2.add(src, 100)
#dst = src + 100? : 255보다 큰 값은 dst에 0으로 세팅되서 이상한 그림이 나온다.
#대신, dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()



# 컬러 영상 불러오기
src = cv2.imread(path + 'lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0))      # 스칼라는 네 개의 튜플로 구성되어 있다. 즉, BGR 부분에 모두 +를 해줘야 골고루 밝기가 올라가는 것!
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
