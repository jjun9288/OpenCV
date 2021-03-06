import sys
import numpy as np
import cv2
path = 'C:/Users/jjun8/Desktop/CV_study/ch7/data/'



#-----------------------------------------------------------------------------------------------------------
# < Labeling >
# - 동일 객체에 속한 모든 픽셀에 고유한 번호를 매기는 작업
#-----------------------------------------------------------------------------------------------------------

mat = np.array([
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)

cnt, labels = cv2.connectedComponents(mat)

print('sep:', mat, sep='\n')
print('cnt:', cnt)
print('labels:', labels, sep='\n')
