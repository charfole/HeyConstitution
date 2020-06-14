import numpy as np
import cv2

image = cv2.imread("001.jpg")
faceCascade = cv2.CascadeClassifier('tongue_cascade_test.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.65,#该参数需要根据自己训练的模型进行调参
        minNeighbors=3,#控制误检测，为3表明至少要3次重叠检测，才认为舌头存在
        minSize=(30,30),#寻找人脸的最小区域。设置这个参数过大，会以丢失小物体为代价减少计算量。
        flags = cv2.IMREAD_GRAYSCALE
    )

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
