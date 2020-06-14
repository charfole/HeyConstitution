import numpy as np
import cv2
from PIL import Image

image = cv2.imread("001.jpg") 
faceCascade = cv2.CascadeClassifier('tongue_cascade.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.65,	#该参数需要根据自己训练的模型进行调参
        minNeighbors=3,	#控制误检测，为3表明至少要3次重叠检测，才认为舌头存在
        minSize=(30,30),	#寻找舌头的最小区域。
        flags = cv2.IMREAD_GRAYSCALE
    )

cropBox=()

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    box1 = (x, y, x+w, y+h)  	# 设置舌体矩形框区域

cv2.imwrite("rec001.jpg",image)
pil_image=Image.open("rec001.jpg")	#使用PIL来编辑图片
image_2 = pil_image.crop(cropBox)  	# 图像裁剪--根据识别出的特征坐标剪切
Image.show(image2)
