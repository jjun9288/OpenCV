import sys
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch2/data/'

#------------------------------------------------------------------------------------------------
#카메라와 동영상으로부터 프레임을 받아오는 작업을 cv2.VideoCapture 클래스 하나로 처리한다.
#1. 카메라 열기
#cv2.VideoCapture(index, apiPreference= None) 
# - index : camera id + domain offset id.   시스템 기본 카메라로 열려면 index=0
# - apiPreference : 선호하는 카메라 처리 방법을 지정
#2. 동영상 열기
#cv2.VideoCapture(filename, apiPreference= None) 
#3. 비디오 캡쳐가 준비되었는지 확인
#cv2.VideoCapture.isopened()
#4. 프레임 받아오기
#cv2.VideoCapture.read(image=None)
#5. 카메라, 비디오 장치 속성 값 참조
#cv2.VideoCapture.get(propId)
# - propId : 속성 상수
#   -CAP_PROP_FRAME_WIDTH : 프레임 가로 크기
#   -CAP_PROP_FRAME_HEIGHT : 프레임 세로 크기
#   -CAP_PROP_FPS : 초당 프레임 수
#   -CAP_PROP_FRAME_COUNT : 비디오 파일의 총 프레임 수
#   -CAP_PROP_POS_MSEC : 밀리초 단위로 현재 위치
#   -CAP_PROP_POS_FRAMES : 현재 프레임 번호
#   -CAP_PROP_EXPOSURE : 노출
#6. 카메라, 비디오 장치 속성 값 참조
#cv2.VideoCapture.set(propId, value)
#------------------------------------------------------------------------------------------------



# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    edge = cv2.Canny(frame, 50, 150)

    inversed = ~frame  # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()



