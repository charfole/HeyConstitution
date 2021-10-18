#@title
import torch
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
from torchvision import datasets, transforms, models
from torchvision.datasets import ImageFolder
import torchvision.models as models
import numpy as np
import cv2
from PIL import Image
import os

# classes = ['pinghe', 'qixu', 'qiyu', 'shire', 'tanshi', 'xueyu', 'yangxu', 'yinxu']
WIDTH, HEIGHT=350,350

def getResult(filePath):
    # 环境
    # use_cuda = not no_cuda and torch.cuda.is_available()
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    preprocess = transforms.Compose([transforms.ToTensor(), normalize])
    img_pil = Image.open(filePath)
    img_pil = img_pil.resize((WIDTH, HEIGHT),Image.ANTIALIAS)
    img = preprocess(img_pil)
    img = img.unsqueeze(0)
    img = img.to(device)

    #读模型参数
    # model = models.resnet18(pretrained=True)
    # model.fc = nn.Linear(512,8)
    # model=model.to(device)
    # model.load_state_dict(torch.load(model_path))
    # model.eval()

    # #读整个模型
    model=(torch.load('RecWholeModel_5.pt'))
    model=model.to(device)
    model.eval()
    
    with torch.no_grad():
      py = model(img)
    # print(py)

    py = F.softmax(py,1)
    confidence = py.numpy()

    return confidence[0]#返回置信度进行加权

    # print(py)

    '''
    res,predicted = torch.max(py, 1)  # 获取分类结果
    predicted = predicted.numpy()
    classIndex = predicted[0]
    res = res.numpy() #将tensor转换成numpy，再取出置信度的int
    rate = res[0]
    # print(rate,classIndex)
    return res,predicted
    '''
    # return rate,classIndex

    # print("置信度:",rate)
    # print("种类:",classIndex)
    # print('预测结果：类{} {}'.format(classIndex, class_name[classIndex]))

# predict(model_path,img_path,classes)  