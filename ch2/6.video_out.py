import sys
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch2/data/'

#--------------------------------------------------------------------------------
#cv2.VideoWriter 클래스를 이용하여 일련의 프레임을 동영상 파일로 저장할 수 있다.
#Fourcc - 동영상 파일의 코덱, 압축 방식, 색상, 픽셀 포맷 등을 정의하는 정수 값
#   -cv2.VideoWriter_fourcc(*'DIVX') : DIVX MPEG-4 코덱
#   -cv2.VideoWriter_fourcc(*'XVID') : XVID MPEG-4 코덱
#   -cv2.VideoWriter_fourcc(*'FMP4') : FFMPEG MPEG-4 코덱
#   -cv2.VideoWriter_fourcc(*'X264') : H.264/AVC 코덱
#   -cv2.VideoWriter_fourcc(*'MJPG') : Motion-JPEG 코덱
# 1. 저장을 위한 동영상 파일 열기
# cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor=None)
# -isColor : 컬러영상이면 True, 아니면 False
# cv2.VideoWriter.open(filename, fourcc, fps, frameSize, isColor=None)
# 2. 프레임 저장하기
# v2.VideoWriter.write(image)
# -image : 저장할 프레임
#--------------------------------------------------------------------------------



cap = cv2.VideoCapture(0)   

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'     _fourcc('D','I','V','X') 라고 써도 된다.
delay = round(1000 / fps)

out = cv2.VideoWriter(path + 'output.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #inversed = ~frame
    #edge = cv2.Canny(frame, 50, 150)       -> 이렇게 하면 저장이 안 됨
    #edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    
    
    out.write(frame)
    #out.write(inversed)
    #out.write(edge)
    
    
    cv2.imshow('frame', frame)
    #cv2.imshow('inversed', inversed)
    #cv2.imshow('edge', edge)             -> 이렇게 하면 저장이 안 됨. 메모리 사용에 차이가 있음
    #cv2.imshow('edge_color', edge_color) 
    
    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
