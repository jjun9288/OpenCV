import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch4/data/'


#-----------------------------------------------------------------------------------------
# < 블러링 >
# - 평균 값 필터 : 영상의 특정 좌표 값들의 평균으로 설정, 픽셀들 간 grayscale 값 변화가
#                  줄어들어 날카로운 edge가 무뎌진다. 
# cv2.blur(src, ksize, dst=None, anchor=None, borderType=None)

# 평균값 필터는 멀리 있는 픽셀의 영햐을 많이 받는다는 단점이 있다.
#-----------------------------------------------------------------------------------------



src = cv2.imread(path + 'rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


dst = cv2.blur(src, (3, 3))

#다른 방법)
#kernel = np.ones((3, 3), dtype=np.float64) / 9.
#dst = cv2.filter2D(src, -1, kernel)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()


# 두번째 방법

src = cv2.imread(path + 'rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
    
kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])

dst = cv2.filter2D(src, -1, kernel)

cv2.imshow(src)
cv2.imshow(dst)
cv2.waitKey()

cv2.destroyAllWindows()

