import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch5/data/'



#-----------------------------------------------------------------------------------------------------------
# <어파인 변환과 투시 변환 >
# - 어파인 변환 : 이동되는 점 3개의 좌표를 알고 있으면 된다.
# cv2.getAffineTransform(src)
# - 투시 변환 : 이동되는 점 4개의 좌표 모두 알고 있어야 한다.
# cv2.getPerspectiveTransform(src, solveMethod=None)
# cv2.warpPerspective(src, M, dsize, flags=None, borderMode=None, borderValue=None)
#-----------------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (w, h))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
