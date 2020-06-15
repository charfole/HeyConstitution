# :star: 基于信息融合的体质分析研究

本项目基于信息融合的思想，打造了一款症状匹配与智能舌诊的体质分析小程序，并将在未来加入养生饮品推荐和基于自然语言处理的体质分析功能。

##  项目结构
项目的开发主要分为以下五个模块

- 数据获取与预处理模块

    主要用到的技术是网络爬虫，使用Python对网上的舌象图片爬取并下载到本地，之后删除掉一些冗余的图片，建立起初步的数据集并做好每张图片的数据标注。
- 算法开发模块

    利用OpenCV进行图片分割降噪，并且利用imgaug进行数据增广扩充数据集。舌象分类采用PyTorch框架进行开发，选择ResNet构建模型。

- 后端部署模块

    使用Nginx+Flask+阿里云服务器部署，将舌象分类模型与症状匹配模块信息融合后综合部署。

- 微信小程序模块

    依托WXML、WXSS、JavaScript和众多开源的微信小程序组件，构建并提供一个界面精美，交互友好的小程序给用户。

- NLP体质分析模块（正在研究）

    基于BERT和XLNET的预处理模型，用于处理文本中存在的多标签风险。

## 小程序截图

### 1. 主页

![主页](https://github.com/charfole/HeyConstitution/blob/master/img/%E4%B8%BB%E9%A1%B5.png)

### 2. 症状匹配

![症状匹配](https://github.com/charfole/HeyConstitution/blob/master/img/%E7%97%87%E7%8A%B6%E5%8C%B9%E9%85%8D.png)

### 3. 图片裁剪

![图片裁剪](https://github.com/charfole/HeyConstitution/blob/master/img/%E5%9B%BE%E7%89%87%E8%A3%81%E5%89%AA.png)

### 4. 体质分析

![体质分析](https://github.com/charfole/HeyConstitution/blob/master/img/%E4%BD%93%E8%B4%A8%E5%88%86%E6%9E%90.png)

### 5. 药膳推荐

![药膳推荐](https://github.com/charfole/HeyConstitution/blob/master/img/%E8%8D%AF%E8%86%B3%E6%8E%A8%E8%8D%90.png)

### 6. 体质记录

![体质记录](https://github.com/charfole/HeyConstitution/blob/master/img/%E4%BD%93%E8%B4%A8%E8%AE%B0%E5%BD%95.png)

## License

[MIT License](https://github.com/charfole/HeyConstitution/blob/master/LICENSE).
