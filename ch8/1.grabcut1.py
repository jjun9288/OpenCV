import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch8/data/'


#-----------------------------------------------------------------------------------------------------------
# < 그랩컷 >
# -Graph cut 기반 영역 분할 알고리즘. 영상의 픽셀을 그래프 정점으로 간주하고, 픽셀들을 두 개의 그룹으로 나누는
#  최적의 컷을 찾는 방식
#
# -cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None)
#-----------------------------------------------------------------------------------------------------------



# 입력 영상 불러오기
src = cv2.imread(path + 'nemo.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 사각형 지정을 통한 초기 분할
rc = cv2.selectROI(src)
mask = np.zeros(src.shape[:2], np.uint8)

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

# 0: cv2.GC_BGD, 2: cv2.GC_PR_BGD
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')   # mask 행렬에서 값이 0 또는 2인 원소는 0으로, 그렇지 않은 원소는 1로 설정
dst = src * mask2[:, :, np.newaxis]

# 초기 분할 결과 출력
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
