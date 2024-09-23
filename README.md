# Xiangshi

### 中文文本相似度计算器

![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=version)
![Downloads](https://static.pepy.tech/badge/xiangshi)

简体中文 | **[English](README_en.md)**

相识是一个中文文本相似度计算器，提供４个传统相似度算法，分别是：余弦相似度，Simhash，Minhash以及Jaccard(杰卡德)。

[在线计算文本相似度](https://kiwirafe.pythonanywhere.com/xiangshi)

## 下载与安装
Pip安装：
```sh
pip3 install xiangshi
```
国内较慢的话可以使用清华镜像：
```sh
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple xiangshi
```


## 使用方法
### 计算文本相似度
#### 余弦相似度
```python
import xiangshi as xs
xs.cossim("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
```

#### Simhash & Minhash & Jaccard相似度
```python
import xiangshi as xs
# Simhash
xs.simhash("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
# Minhash
xs.minhash("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
# Jaccard
xs.jaccard("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
```

### 其它加权方法 
默认的加权方法是计算每个单词在文中出现的数量，以下还有其他两种加权方法可供选择。
#### TFIDF
```python
arg = [
    "西班牙失业率创新高",
    "澳大利亚失业率高达5.1%",
    "花呗更改绑定银行卡",
    "我什么时候开通了花呗",
    "从这个角度来看， 我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。"
    "从这个角度来看， 每个人都不得不面对这些问题。"

]
xs.weight = "TFIDF" # 将加权方式设置为TFIDF
xs.construct(arg) # 输入TFIDF文本，相同的文本只需调用这个函数一次

xs.cossim("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
xs.simhash("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
```

#### 没有加权
```python
xs.weight = "None" # 将加权方式设置为None
xs.cossim("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
```

### 英文文本相似度
在v4.2.1之后，相识支持英文文本相似度（即使用英文停用词、英文分词方法）。
```python
import xiangshi as xs
xs.lang = "en"
xs.cossim("A mathematician found a solution to the problem.", "The problem was solved by a young mathematician.")
```

### 
#### 修改默认函数
```python
import xiangshi as xs
#计算Simhash时取前多少的TFIDF值。默认值为64
xs.feature = 64
#计算Minhash时算出多少个哈希值。默认值为16
xs.HashNums = 16
#计算Minhash时的最大哈希。默认值为4294967311
xs.prime = 4294967311
```

#### 修改停用词
在v4.2.1之后，相识支持更改默认停用词：
```python
import xiangshi as xs
stopwords = ["你好", "世界"]
xs.update_stopwords(stopwords)
```


## 新版本
### v4.2.1:
  - 支持英文文本相似度

### 注意：
  - v4.2.0+文本相似度的计算结果可能和v4.1.0不一样，因为v4.1.0加权方式不同。
  - v4.2.0+文本相似度的输入均为两个`string`，且**不与**v4.1.0反向兼容。
  - v4.2.0+不再支持文本聚类（如果还有人需要的话请联系我，我会另开一个包）


## 其他链接
  - 在线计算文本计算器:
  https://kiwirafe.com/xiangshi
  - PyPI:
  https://pypi.org/project/xiangshi/
  - Github:
  https://github.com/kiwirafe/xiangshi
  - 下载数量:
  https://pepy.tech/project/xiangshi
  - Gitee（中国开源）:
  https://gitee.com/kiwirafe/xiangshi
  - 关于算法的其他链接:
  https://github.com/kiwirafe/xiangshi/blob/master/Bibliography.md


## 相识寓意
>同是天涯沦落人，相逢何必曾**相识**