# 多模态信息融合主导的体质分析与膳食推荐小程序

本项目基于多模态信息融合的思想，打造了一款症状分析与智能舌诊的体质分析与膳食推荐小程序。

##  项目结构
项目的开发主要分为以下四个模块

- 数据获取与预处理模块

    主要用到的技术是网络爬虫，使用Python对网上的舌象图片爬取并下载到本地，之后删除掉一些冗余的图片，建立起初步的数据集并做好每张图片的数据标注。

- 算法开发模块

    利用OpenCV进行图片分割、去除噪声，并且利用imgaug进行数据增广扩充数据集。舌象分类采用PyTorch框架进行开发，选择ResNet50构建模型。

- 后端部署模块

    使用Gunicorn+Flask+阿里云服务器部署，将舌象分类模型与症状匹配模块信息融合后综合部署。

- 微信小程序模块

    依托WXML、WXSS、JavaScript和众多开源的微信小程序组件，构建并提供一个界面精美，交互友好的小程序给用户。

## 小程序截图

### 1. 首页

<div align=center><img src="https://github.com/charfole/HeyConstitution/blob/master/images/首页.jpg" width="40%" height="40%"></div>
<!-- ![首页](https://github.com/charfole/HeyConstitution/blob/master/images/首页.jpg) -->

### 2. 使用说明

<div align=center><img src="https://github.com/charfole/HeyConstitution/blob/master/images/使用说明.png" width="50%" height="50%"></div>
<!-- ![使用说明](https://github.com/charfole/HeyConstitution/blob/master/images/使用说明.png) -->

### 3. 症状匹配

<div align=center><img src="https://github.com/charfole/HeyConstitution/blob/master/images/症状匹配.png" width="50%" height="50%"></div>
<!-- ![症状匹配](https://github.com/charfole/HeyConstitution/blob/master/images/症状匹配.png) -->

### 4. 体质分析

<div align=center><img src="https://github.com/charfole/HeyConstitution/blob/master/images/体质分析.png" width="50%" height="50%"></div>
<!-- ![体质分析](https://github.com/charfole/HeyConstitution/blob/master/images/体质分析.png) -->

### 5. 个人信息

<div align=center><img src="https://github.com/charfole/HeyConstitution/blob/master/images/个人信息.png" width="50%" height="50%"></div>
<!-- ![个人信息](https://github.com/charfole/HeyConstitution/blob/master/images/个人信息.png) -->

### 6. 膳食推荐

<div align=center><img src="https://github.com/charfole/HeyConstitution/blob/master/images/膳食推荐.png" width="50%" height="50%"></div>
<!-- ![膳食推荐](https://github.com/charfole/HeyConstitution/blob/master/images/膳食推荐.png) -->

### 7. 体质记录

<div align=center><img src="https://github.com/charfole/HeyConstitution/blob/master/images/体质记录.png" width="50%" height="50%"></div>
<!-- ![体质记录](https://github.com/charfole/HeyConstitution/blob/master/images/体质记录.png) -->

## License

[MIT License](https://github.com/charfole/HeyConstitution/blob/master/LICENSE).
