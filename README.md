# 相识(Xiangshi)

### 中文文本相似度计算器
[![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=Pypi%20Version)](https://img.shields.io/pypi/v/xiangshi)
[![Downloads](https://pepy.tech/badge/xiangshi)](https://pepy.tech/project/xiangshi)
[![Pypi and Github License](https://img.shields.io/pypi/l/xiangshi?label=Pypi%20and%20Github%20License)](https://img.shields.io/github/license/kiwirafe/xiangshi)
[![Language](https://img.shields.io/github/languages/top/kiwirafe/xiangshi)](https://github.com/kiwirafe/xiangshi)

相识是一款专门为中文打造的文本相似度计算器。这是唯一也是最好的中文文本相似度计算器

相识的优势有：
  - 专攻中文文本相似度比较
  - 使用余弦计算，Simhash和Minhash两种算法
  - 100%Python语言
  - 自动TFIDF过滤
  - 可以单独计算TF和IDF
  - 支持List和File两种类型
  - 支持多个文件相似度比较
  - 高效、迅速
  - 安装容易
  - 100%开源
  - 长期维护和更新

## 下载与安装
Pip安装：
```sh
$ pip3 install xiangshi
```
国内较慢的话可以使用清华镜像：
```sh
$ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple xiangshi
```

### 版本v2.1.1~v2.3.0来了！
  - v2.1.1: 支持只有TF的加权
  - v2.1.2：Minhash加权选定用Quantization-Based来实现
  - v2.1.3: Minhash由set转为dict，与v1.0.1原因一样
  - v2.2.0：
    - Minhash加权成功
    - 使用Quantization-Based算法
    - 具体用Multiset实现
  - v2.2.1: 增加CHANGES.md
  - v2.2.2: README更新，更多注释
  - v2.3.0: 使用Logging，所有运算记录均保存在xiangshi.log
  - v2.3.1: 发现Stoptext无法使用
  - v2.3.2: Pip加入Stoptext
  - v2.3.3: Stoptext由所相识文件里调用，而不是从运行地点里调用
  - v2.4.0：
    - 相识极速版并入相识
    - 减少时间，20~30s减少至10~15s
    - 完全支持列表

## 使用方法
### 计算文本相似度
#### 余弦相似度
```python
import xiangshi as xs
xs.cossim(Input1, Input2)
```
#### Simhash & Minhash 相似度
```python
import xiangshi as xs
# Simhash
xs.simhash(Input1, Input2)
# Minhash
xs.minhash(Input1, Input2)
```
 - 计算文本相似度时自动由TFIDF过滤
 - Input1 - 第一个输入值，可以是文件的地址或是一个列表
 - Input2 - 第二个输入值，可以是文件的地址或是一个列表

#### 计算TF，IDF，TFIDF
```python
import xiangshi as xs
xs.GetTF(Input)
xs.GetIDF(Input)
xs.GetTFIDF(Input)
```
#### 其他函数
```python
import xiangshi as xs
xs.input2list(Input) #分词
xs.dict2file(dict) #Dict到File
xs.SortDict(dict) #Dict排序
xs.HashString(str) #哈希Str
```

### 修改默认函数
```python
import xiangshi as xs
xs.TFIDF = True 
#是否使用TFIDF，True是使用TFIDF，False是只是用TF。默认值为True
xs.UseLog = True
#计算TFIDF时是否使用log，True是使用，False是不使用。默认值为True
xs.FileDir = ""
#计算IDF时其他文件的目录。默认值为""
xs.InputTarget = 0
#输入列表时指定计算的目标。默认值为1
xs.feature = 64
#计算Simhash时取前多少的TFIDF值。默认值为64
xs.HashNums = 16
#计算Minhash时算出多少个哈希值。默认值为16
xs.prime = 4294967311
#计算Minhash时的最大哈希。默认值为4294967311
```

### 计算文本相似度的Input类型
目前相识支持两种类型 - 文件和列表
文件：
```
data/
  |_test1.txt
  |_test2.txt
  |_test3 ~ 10.txt（用于IDF的计算）
```
列表：
```py
data = [
  ["相识是一款专门为中文打造的文本相似度计算器"]
  ["相识是唯一也是最好的中文文本相似度计算器"]
  ["相识支持Cosine, Simhash, Minhash Similarity"] #用于IDF的计算
  ["有问题一定要在Github上提Issue"] #用于IDF的计算
  ["有改进一定要在Github上提Pull Request"] #用于IDF的计算
]
```

## 其他链接：
  - English Version of README.md:
  https://github.com/kiwirafe/xiangshi/blob/master/README(Eng).md
  - Change Log（没事就看一看）
  https://github.com/kiwirafe/xiangshi/blob/master/CHANGES.md
  - Pypi: 
  https://pypi.org/project/xiangshi/
  - Github:
  https://github.com/kiwirafe/xiangshi
  - 下载数量:
  https://pepy.tech/project/xiangshi
  - Gitee（中国开源）:
  https://gitee.com/kiwirafe/xiangshi
  - 清华镜像链接:
  https://pypi.tuna.tsinghua.edu.cn/simple/xiangshi/

## 相识寓意
>与君初**相识**，
犹如故人归。
天涯明月新，
朝暮最相思。

![Xiangshi](https://imgur.com/zoAnNfx.jpg)

## MIT License
Copyright (c) [2020] [Kiwirafe]

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