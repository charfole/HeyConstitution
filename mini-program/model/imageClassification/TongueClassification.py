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

batch_size = 100
test_batch_size = 10
mini_batch_size = 10
epochs = 20
lr = 0.005
gamma = 0.7
no_cuda = True
seed = 1
log_interval = 10
save_model = True
class_num=8
criterion = nn.CrossEntropyLoss()  # 交叉熵
base_dirs = ['pinghe/', 'qixu/', 'qiyu/', 'shire/', 'tanshi/', 'xueyu/', 'yangxu/', 'yinxu/']
classes = ['pinghe', 'qixu', 'qiyu', 'shire', 'tanshi', 'xueyu', 'yangxu', 'yinxu']
train_root = "./drive/My Drive/data/dataset3/mask/"
test_root = "./drive/My Drive/data/dataset3/mask/"
model_path = 'res01.pt'
img_path = '1_1.jpg'





def default_loader(path):
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    preprocess = transforms.Compose([transforms.ToTensor(), normalize])

    img_pil = Image.open(path)
    img_tensor = preprocess(img_pil)
    return img_tensor


class MyDataset(Dataset):
    def __init__(self, root, base_dirs, loader=default_loader):
        self.image_label_list, self.image_path_list = self.read_file(root, base_dirs)
        self.root = root
        self.base_dirs = base_dirs
        self.len = len(self.image_label_list)
        self.loader = loader

    def __getitem__(self, i):
        index = i
        label = self.image_label_list[index]
        path = self.image_path_list[index]
        img = self.loader(path)
        return img, label

    def __len__(self):
        data_len = len(self.image_label_list)
        return data_len

    # 返回标签列表、目录列表
    def read_file(self, root, base_dirs):
        image_label_list = []
        image_path_list = []

        for i in range(len(base_dirs)):
            dir = root + base_dirs[i]
            listImages = [dir + Image for Image in (os.listdir(dir))]
            for file in listImages:
                image_label_list.append(i)
                image_path_list.append(file)

        return image_label_list, image_path_list


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, padding=1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(91875, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output



def train(model, device, train_loader, optimizer, epoch):
    model.train()
    tot_loss = 0.0
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()

        # forward backward
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        tot_loss += loss.item()

        print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
            epoch, batch_idx * len(data), len(train_loader.dataset),
                   100. * batch_idx / len(train_loader), loss.item()))
        tot_loss = 0.0


def test(model, device, test_loader):
    model.eval()
    test_loss = 0.0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += criterion(output, target)
            pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


def main():
    use_cuda = not no_cuda and torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    torch.manual_seed(seed)

    kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}

    train_loader = torch.utils.data.DataLoader(MyDataset(train_root, base_dirs),
                                               batch_size=batch_size, shuffle=True, **kwargs)
    test_loader = torch.utils.data.DataLoader(MyDataset(test_root, base_dirs),
                                              batch_size=test_batch_size, shuffle=True, **kwargs)
    '''
    model =Net().to(device)    
    '''

    model = models.resnet18(pretrained=True)
    model.fc = nn.Linear(512, 8)
    model = model.to(device)

    # 交叉熵
    criterion = nn.CrossEntropyLoss()
    # momentumSGD
    optimizer = optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=5e-4)

    # scheduler = StepLR(optimizer, step_size=1, gamma=gamma)
    for epoch in range(1, epochs + 1):
        train(model, device, train_loader, optimizer, epoch)
        test(model, device, test_loader)
        # scheduler.step()

    if save_model:
        torch.save(model.state_dict(), "res01.pt")


def predict(model_path, img_path, class_name):
    # 环境
    use_cuda = not no_cuda and torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    preprocess = transforms.Compose([transforms.ToTensor(), normalize])
    img_pil = Image.open(img_path)
    img = preprocess(img_pil)
    img = img.unsqueeze(0)
    img = img.to(device)

    model = torch.load(model_path)
    model = model.to(device)
    model.eval()
    with torch.no_grad():
        py = model(img)
    _, predicted = torch.max(py, 1)  # 获取分类结果
    classIndex_ = predicted[0]

    print('预测结果：类{} {}'.format(classIndex_, class_name[classIndex_]))








