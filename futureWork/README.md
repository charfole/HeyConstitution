## 基于bert的多风险体质预测模型

本文是基于BERT和XLNET的预处理模型，用于处理文本中存在的多标签风险。旨在为项目《基于信息融合的体制分析研究》提供服务。

###  代码结构

```text
├── pybert
|  └── callback
|  |  └── lrscheduler.py　　
|  |  └── trainingmonitor.py　
|  |  └── ...
|  └── config
|  |  └── basic_config.py #基本设置：包括文件路径等
|  └── dataset　　　
|  └── io　　　　
|  |  └── dataset.py　　
|  |  └── data_transformer.py　　
|  └── model
|  |  └── nn　
|  |  └── pretrain　
|  └── output #保存结果
|  └── preprocessing #文本预处理
|  └── train #训练模型
|  |  └── trainer.py 
|  |  └── ...
|  └── common # 常用函数
├── run_bert.py
├── run_xlnet.py
```
### 各包配置如下

- csv
- tqdm
- numpy
- pickle
- scikit-learn
- Torch1.5.0+cuda10.1.0
- matplotlib
- pandas
- transformers=2.5.1

### 怎样使用本代码

因为本项目使用bert预训练模型，所以你需要先下载预训练bert和xlnet的词向量

<div class="note info"><p> BERT:  bert-base-uncased</p></div>
<div class="note info"><p> XLNET:  xlnet-base-cased</p></div>

1. 在(https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-pytorch_model.bin)  下载bert预训练模型

2. 在(https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-config.json) 下载bert配置文件
3. 在(https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt) 下载bert词向量
4. 重命名:

    - 将`bert-base-uncased-pytorch_model.bin` 重命名为 `pytorch_model.bin`
    - 将`bert-base-uncased-config.json` 重命名为 `config.json`
    - 将`bert-base-uncased-vocab.txt` 重命名为 `bert_vocab.txt`
5. 将 `model` ,`config` 和 `vocab` 文件放入 `/pybert/pretrain/bert/base-uncased` 文件夹。
6. `pip install pytorch-transformers` 从地址：https://github.com/huggingface/pytorch-transformers.
7. 将你的数据集(本项目数据集属于商业机密，暂不开放)放入 `pybert/dataset`，你可以修改 `io.task_data.py` 的相关配置，以处理你的数据.
8.修改文件路径 `pybert/configs/basic_config.py`(the path of data,...).
9. 运行 `python run_bert.py --do_data` 进行文件预处理
10. 运行 `python run_bert.py --do_train --save_best --do_lower_case` 进行bert模型的fine tuning.
11. 运行`run_bert.py --do_test --do_lower_case`用于预测新的文本.

### 训练结果

```text
[training] 8511/8511 [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>] -0.8s/step- loss: 0.0640
training result:
[2020-06-07 04:01:05]: bert-multi-label trainer.py[line:176] INFO  
Epoch: 6 - loss: 0.0338 - val_loss: 0.0373 - val_auc: 0.8392
```

### 结果展示

```python
---- train report every label -----
Label: 湿热质 - auc: 0.8303
Label: 气虚质 - auc: 0.8913
Label: 血瘀质 - auc: 0.9551
Label: 阴虚质 - auc: 0.7898
Label: 阳虚质 - auc: 0.7911
Label: 平和质 - auc: 0.7510
---- valid report every label -----
Label: 湿热质 - auc: 0.8292
Label: 气虚质 - auc: 0.8911
Label: 血瘀质 - auc: 0.9445
Label: 阴虚质 - auc: 0.7655
Label: 阳虚质 - auc: 0.7803
Label: 平和质 - auc: 0.7327
```