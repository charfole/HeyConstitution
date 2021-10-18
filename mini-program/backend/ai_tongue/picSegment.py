# encoding:utf-8

#time:2020-8-26 17:26
#task:图像分割

import urllib.request
import base64
import json
import pycocotools.mask as mask_util#先pip Cython再pip install pycocotools，好坑
import cv2
import numpy as np
# from google.colab.patches import cv2_imshow
import glob
import os
import requests


# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=udjj3x3uB16w2A5CAIUWfCy6&client_secret=IxwXNR6HQf8cKtPm2wVcBCjC4qmmTY6x'
response = requests.get(host)
token = "24.e02b5cdcccad55ba8599ad7168b4a127.2592000.1603329667.282335-22076750"
if response:
    token = response.json()["access_token"]#随时更新access_token


'''
图像分割函数，三个参数依次为：图片路径、矩形分割图片的命名、mask分割图片的命名
'''

def pictureProcess(path):
  
  # recString = path.split("/")[-1].split(".")[0] + "_rec.jpg" # 重命名矩形分割的图片，第1518张_rec.jpg
  recString = path.replace(".", "_rec.")
  maskString = path.replace(".", "_mask.")
  # maskString = imgPath.split("/")[-1].split(".")[0] + "_mask.jpg" # 重命名mask分割的图片，第1518张_mask.jpg

  # 第一部分：读图片

  with open(path, 'rb') as f:  # 以二进制读取图片
    data = f.read()
    encodestr = base64.b64encode(data) # 得到 byte 编码的数据

  # 第二部分：请求分割API，获得结果参数

  params = {
        "image" : encodestr.decode('ascii'),
        "threshold" : 0.9 # 注意这里是图片分割置信度的阈值，百度建议的是0.4，模型只会返回大于0.4的分割结果。
        }
  params = json.dumps(params)
  params=bytes(params,'utf8')
  
  access_token = token # 根据上面AK和SK获取的access_token
  request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/segmentation/seg4miniProgram" # 模型API地址
  request_url = request_url + "?access_token=" + access_token
  request = urllib.request.Request(url=request_url,data=params)
  request.add_header('Content-Type', 'application/json')
  response = urllib.request.urlopen(request)
  content = response.read()

  # print(content)

  try:

    results = json.loads(content)['results']

    # print(results)

    # 获取结果，并画图
    try:

      results = json.loads(content)['results']
      # print(results)
      ori_img = cv2.imread(path).astype(np.float32) #读图片
      height, width = ori_img.shape[:2]

      if results==[]:
        return False

      for item in results:
          scores = float(item["score"])
          if scores >= 0.0:
            # Draw bbox
            x1 = int(item["location"]["left"])
            y1 = int(item["location"]["top"])
            w = int(item["location"]["width"])
            h = int(item["location"]["height"])
            x2 = x1 + w
            y2 = y1 + h

            cv2.rectangle(ori_img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(ori_img, "{} score: {}".format(item["name"], round(float(item["score"]),4)), (x1, y1 - 10), cv2.FONT_HERSHEY_PLAIN, 0.7, (255, 255, 255), 1)

            # Draw mask
            rle_obj = {"counts": item['mask'],
                      "size": [height, width]}
            mask = mask_util.decode(rle_obj)

            for i in range(0,height):
              for j in range(0,width):
                if mask[i][j]==1 :
                  mask[i][j]=2
                elif mask[i][j]==0:
                  mask[i][j]=1
            
            for i in range(0,height):
              for j in range(0,width):
                if mask[i][j]==2 :
                  mask[i][j]=0

            new_rle_obj = mask_util.encode(mask)
            idx = np.nonzero(mask)

            #注释时间为2020-9-22 9：35 原因：这个模型用到的是mask
            # # 处理矩形分割，并保存矩形分割图
            # cropped_rec = ori_img[y1:y2,x1:x2]
            # cropped_rec2 = cv2.resize(cropped_rec, (350, 350), interpolation=cv2.INTER_LANCZOS4)#图片resize：https://blog.csdn.net/C_chuxin/article/details/82817407
            # # cv2_imshow(cropped_rec)
            # recString = "" + recString
            # cv2.imwrite(recString, cropped_rec2)
            # # print(recString.split('/')[-1] + " sussessfully processed")

            # 处理mask分割，并保存mask分割图
            ori_img[idx[0], idx[1], :] = np.array([255,255,255])
            cropped_mask = ori_img[y1:y2,x1:x2]
            cropped_mask2 = cv2.resize(cropped_mask, (350, 350), interpolation=cv2.INTER_LANCZOS4)#图片resize：https://blog.csdn.net/C_chuxin/article/details/82817407

            # cv2_imshow(cropped_mask2)
            maskString = "" + maskString
            cv2.imwrite(maskString, cropped_mask2)
            # print(maskString.split('/')[-1] + " sussessfully processed")

      return True


    except ValueError:
      return False
  
  except Exception as e:
    # print(e)
    return False