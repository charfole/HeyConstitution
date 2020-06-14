from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import numpy as np

WIDTH = 100
HEIGHT = 100

#定义图像读取
def get_image_pixel(file):
  img = Image.open(file)
  img = img.resize((WIDTH,HEIGHT))
  #图片灰度化-l
  img = img.convert("L")
  img_array = img_to_array(img)
  return img_array


#获取要预测的图片的像素矩阵
def get_test_image_pixel(file):
  X_test = []
  img_array = get_image_pixel(file)
  X_test.append(img_array)
  X_test = np.array(X_test)
  X_test = X_test.reshape(1, WIDTH, HEIGHT, 1)
  X_test = X_test.astype('float32')
  X_test /= 255   #归一化
  return X_test

#获取上传图片对应体质结果
def getResult(filePath):
  #根据tag输出对应的分类
  newModel = load_model('20200203.model')
  # newModel.summary()

  predictions_array = newModel.predict(get_test_image_pixel(filePath))

  predictions_list = predictions_array.tolist()[0]
 # print(predictions_list)
  #各个分类的预测列表

  predictions_tag = predictions_list.index(max(predictions_list))
#  print(predictions_tag)
  return predictions_tag
  #预测值最大的那个tag
