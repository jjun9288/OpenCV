import sys
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch2/data/'

# 마스크 영상을 이용한 영상 합성
src = cv2.imread(path+'airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread(path+'mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread(path+'field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

cv2.copyTo(src, mask, dst)         #src : 입력 영상 / mask : 마스크 영상 / dst(destinatino) : 출력 영상
# dst[mask > 0] = src[mask > 0]  -> 픽셀 값 자체를 변경

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()


# 알파 채널을 마스크 영상으로 이용  (알파 채널을 불러올 때 cv2.IMREAD_UNCHANGED 명령어로 4채널 영상을 불러올 수 있다.)
src = cv2.imread(path+'cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread(path+'opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

# mask는 알파 채널로 만든 마스크 영상
mask = logo[:, :, 3]    #grayscale 이어야 하므로 3 마지막 값만 갖고 와서 1차원으로 만듬 
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상. 4채널이므로 -1까지 갖고 온다.
h, w = mask.shape[:2]
#src와 dst 크기가 다르므로 마스크 연산이 안 된다.
#src와 동일한 크기의 영상을 추출 = crop
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
