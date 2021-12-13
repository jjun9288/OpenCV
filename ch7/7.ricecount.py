import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch7/data/'



#-----------------------------------------------------------------------------------------------------------
# <Morphology(2) : 열기와 닫기 >
# -열기 연산 : 침식 -> 팽창
# -닫기 연산 : 팽창 -> 침식
# cv2.morphologyEx(src, op, kernel, anchor=None, iterations=None, borderType=one, borderValue=None)
#   -op : 모폴로지 연산 플래그
#       -cv2.MORPH_ERODE : 침식
#       -cv2.MORPH_DILATE : 팽창
#       -cv2.MORPH_OPEN : 열기
#       -cv2.MORPH_CLOSE : 닫기
#       -cv2.MORPH_GRADIENT : 모폴로지 그래디언트 = 팽창 - 침식
#-----------------------------------------------------------------------------------------------------------

src = cv2.imread(path + 'rice.png', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# src 영상에 지역 이진화 수행 (local_th.py 참고)
dst1 = np.zeros(src.shape, np.uint8)

bw = src.shape[1] // 4
bh = src.shape[0] // 4

for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst1[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)

cnt1, _ = cv2.connectedComponents(dst1)
print('cnt1:', cnt1)

dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)
#dst2 = cv2.erode(dst1, None)
#dst2 = cv2.dilate(dst2, None)

cnt2, _ = cv2.connectedComponents(dst2)
print('cnt2:', cnt2)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
