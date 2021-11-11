import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt
path = 'C:/Users/jjun8/Desktop/CV_study/ch3/data/'


#----------------------------------------------------------------------------------------------------------------------
#<영상의 산술 및 논리 연산>
# 1. 덧셈
# dst(x,y) = saturate(src1(x,y) - src2(x,y))
#cv2.add(src1, src2, dst=None, mask=None, dtype=None)
#   -dst는 덧셈 연산의 결과 영상
#가중치 합 dst(x,y) = saturate(a*src1(x,y) + b*src2(x,y))
#   a+b>1일 때에는 255를 넘는 값이 많아지므로 a+b=1로 설정
#   a=b=0.5로 하면 두 이미지의 윤곽선이 골고루 드러난다.
#   cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)       gamma는 그냥 추가연산 필요하면 쓰는 것
# 2. 뺄셈
# dst(x,y) = saturate(src1(x,y) - src2(x,y))
#cv2.subtract(src1, src2, dst=None, mask=None, dtype=None)
#cv2.absdiff(src1, src2, dst=None)
# 3. 영상의 논리연산 (그냥 이런게 있구나 하고 넘어가자)
# - cv2.bitwise_and(src1, src2, dst=None, mask=None)
# - cv2.bitwise_or(src1, src2, dst=None, mask=None)
# - cv2.bitwise_xor(src1, src2, dst=None, mask=None)
# - cv2.bitwise_not(src1, src2, dst=None, mask=None)
#----------------------------------------------------------------------------------------------------------------------



src1 = cv2.imread(path + 'lenna256.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread(path + 'square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst3 = cv2.subtract(src1, src2)
dst4 = cv2.absdiff(src1, src2)

plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
plt.show()
