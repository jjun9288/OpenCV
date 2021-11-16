import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch3/data/'

#-------------------------------------------------------------------------------------------------------------------------
# < Histogram stretching >
# 히스토그램을 그렸을 때 G(min) = 25, G(max) = 240이라 하자. 이걸 (0,255)로 늘리면 contrast가 올라가는 것을 볼 수 있다.
# cv2.normalize(src, dst, alpha=None, beta=None, norm_type=None, dtype=None, mask=None)
#   - alpha : 최솟값 (0)
#   - beta : 최댓값 (255)
#-------------------------------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
#dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()


'''
def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)                  # 히스토그램 그리기

    return imgHist

hist_1 = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg_1 = getGrayHistImage(hist_1)

hist_2 = cv2.calcHist([dst], [0], None, [256], [0, 256])
histImg_2 = getGrayHistImage(hist_2)
'''
