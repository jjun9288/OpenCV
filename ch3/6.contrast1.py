import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch3/data/'

#---------------------------------------------------------------------------------------------------------------------------------
# 기본적인 명암비 조절 함수
# dst(x,y) = saturate(s*src(x,y))
#   - s가 작아지면 명암비가 작아지는데, 대신 이미지가 어두워진다. 커지면 반대가 될 것이다.
# dst(x,y) = saturate(src(x,y) + (src(x,y) - 128) * alpha)             -> (1 + alpha) * src(x,y) - 128 * alpha
#   - alpha가 커질수록 명암비가 커진다. 사람마다 기준이 다르므로 어느정도의 alpha값이 최고의 명암비를 가져다주는 지는 모른다.
#   - 위 식보다는 많은 픽셀들을 살릴 수 있어서 장점이 있지만, 이 또한 0보다 작아지는 / 255보다 커지는 부분이 여전히 있긴 하다.
#---------------------------------------------------------------------------------------------------------------------------------


src = cv2.imread(path + 'lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
