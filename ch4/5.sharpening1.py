import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch4/data/'


#------------------------------------------------------------------------------------------------
# <Sharpening : Unsharp mask filter>
# - 부드러워진 unsharp 영상을 이용하여 날카로운 영상을 생성
# - 함수로 구현되어 있지 않아서 우리가 직접 구현해서 써야한다.
#------------------------------------------------------------------------------------------------



src = cv2.imread(path + 'rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 1) blur
blr = cv2.GaussianBlur(src, (0, 0), 2)

# 2) unsharp mask filtering
dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
