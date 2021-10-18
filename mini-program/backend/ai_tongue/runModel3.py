# encoding:utf-8
#time: 2020-9-22 8:36
#author:Tang Gaozhi
#target:新的图像分类模型

import requests 
import urllib.request
import base64
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=2lmGPrCIikIwRlqbeRT5Eg9E&client_secret=1rhxcHAG9OtEy3AR2o3sQij7WKdzUHz2'
response = requests.get(host)
token = "24.fe1b146c2966d72551635a05202c370f.2592000.1603179060.282335-22710328"
if response:
    token = response.json()["access_token"]

classes = ['pinghe', 'qixu', 'qiyu', 'shire', 'tanshi', 'xueyu', 'yangxu', 'yinxu']

def getResult(path):
  request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/tongueClassfication"

  # 读入图片
  with open(path, 'rb') as f:
      base64_data = base64.b64encode(f.read())
      s = base64_data.decode('UTF8')

  params = {"image": s, "top_num": "8"} # 两个参数分别为图片的base64编码和返回的分类结果数目
  params = json.dumps(params)
  params=bytes(params,'utf8')

  access_token = token
  request_url = request_url + "?access_token=" + access_token
  request = urllib.request.Request(url=request_url, data=params)
  request.add_header('Content-Type', 'application/json')
  response = urllib.request.urlopen(request)
  content = response.read()
  
  if content:
    # print(content) # 结果数组
    results = json.loads(content)['results']
    results_dict = {}
    for result in results:
      results_dict[result["name"]] = result["score"]
    confidence = []

    for i in range(0,len(results_dict)):
      confidence.append(results_dict[classes[i]])

    return confidence
