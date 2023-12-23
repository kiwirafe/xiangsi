# 相识(Xiangshi)

#### 中文文本相似度计算器
#### Chinese Text Similarity Calculator ([English README](https://github.com/kiwirafe/xiangshi/blob/master/README(Eng).md))
#### [在线计算文本相似度](https://kiwirafe.com)
[![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=Pypi%20Version)](https://img.shields.io/pypi/v/xiangshi)
[![Pypi Downloads](https://static.pepy.tech/personalized-badge/xiangshi?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads)](https://pepy.tech/project/xiangshi)

相识是一个侧重于中文的文本相似度计算器，并提供４个传统相似度算法，分别是：余弦相似度，Simhash，Minhash以及Jaccard(杰卡德)。

## 下载与安装
Pip安装：
```sh
pip3 install xiangshi
```
国内较慢的话可以使用清华镜像：
```sh
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple xiangshi
```

## 新版本
### v4.2.0:
  - 删除logging
  - 删除`file2list`，`dict2file`等辅助函数
  - 删除Ngrams
  - 删除Kmeans
  - 增加Jaccard相似度
  - 提升余弦、Simhash相似度计算速度

### 注意：
  - v4.2.0文本相似度的计算结果可能和v4.1.0不一样，因为v4.1.0加权方式不同。
  - v4.2.0文本相似度的输入均为两个`string`，且**不与**v4.1.0反向兼容。
  - v4.2.0不再支持文本聚类（如果还有人需要的话请联系我，我会另开一个包）

## 使用方法
### 计算文本相似度
#### 余弦相似度示例
```python
import xiangshi as xs
xs.cossim("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
```
#### Simhash & Minhash & Jaccard相似度示例
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

### 修改默认函数
```python
import xiangshi as xs
#计算Simhash时取前多少的TFIDF值。默认值为64
xs.feature = 64
#计算Minhash时算出多少个哈希值。默认值为16
xs.HashNums = 16
#计算Minhash时的最大哈希。默认值为4294967311
xs.prime = 4294967311
```

## 目前状态
持续维护并且持续关注Issues & Pull Requests

### 未来版本
- 内嵌C语言提速
- 使用BERT或类似机器学习模型实现更精确的文本相似度

## 其他链接
  - 在线计算文本计算器:
  https://kiwirafe.com
  - English Version:
  https://github.com/kiwirafe/xiangshi/blob/master/README(Eng).md
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

## MIT License
Copyright (c) [2021] [kiwirafe]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
