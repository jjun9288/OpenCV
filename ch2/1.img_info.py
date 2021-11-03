# < 영상의 속성과 픽셀 값 >
import sys
import cv2
path = 'C:/Users/jjun8/Desktop/CV/ch2/'

# 영상 불러오기
img1 = cv2.imread(path + 'cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(path + 'cat.bmp', cv2.IMREAD_COLOR)

if img1 is None:
    print('Image load failed')
    sys.exit()

print('type(img1):', type(img1))
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img2.dtype:', img2.dtype)

h, w = img2.shape[:2]
print('img2 size : {} x {}'.format(w, h))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')      # h, w만 정의되어 있다면 grayscale로 봐도 무방하다.
elif len(img1.shape) == 3:
    print('img1 is a color image')          # (h, w, 3) 여기서 3은 RGB채널을 뜻한다.

img1[: , :] = 255
img2[: , :] = (0,0,255)

