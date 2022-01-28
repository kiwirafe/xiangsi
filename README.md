# 相识(Xiangshi)

### 中文文本相似度计算器 + 中文聚类计算器
[![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=Pypi%20Version)](https://img.shields.io/pypi/v/xiangshi)
[![Pypi Downloads](https://static.pepy.tech/personalized-badge/xiangshi?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads)](https://pepy.tech/project/xiangshi)
[![Pypi and Github License](https://img.shields.io/pypi/l/xiangshi?label=Pypi%20and%20Github%20License)](https://img.shields.io/github/license/kiwirafe/xiangshi)
[![Language](https://img.shields.io/github/languages/top/kiwirafe/xiangshi)](https://github.com/kiwirafe/xiangshi)

### [在线计算文本相似度](https://xs.datavisdev.com)
### [English Version of README](https://github.com/kiwirafe/xiangshi/blob/master/README(Eng).md)

相识的优势有：
  - 专攻中文文本相似度比较
  - 支持余弦、Simhash、Minhash和Ngram算法
  - 100%Python语言
  - 可以单独计算TF和IDF
  - 安装容易
  - 100%开源
  - 长期维护和更新

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
### v4.0.0:
  - 再次减少20%时间
  - 增加Kmeans聚类
  - 重新修改Cache方法
  - 重新修改Input输入
### v4.1.0:
  - 修改Kmeans中variation的计算
  - 输出格式修改

### 注意：
  - v4.0.0的计算结果可能和v3.0.0不一样因为v4.0.0不再自动TFIDF加权
  - 注意：v4.0.0中的Input均为`list`

## 使用方法
### 计算文本相似度
#### 余弦相似度示例
```python
import xiangshi as xs
xs.cossim(["我曾经失落失望失掉所有方向", "直到看见平凡才是唯一的答案"])
```
#### Simhash & Minhash & Ngram相似度示例
```python
import xiangshi as xs
# Simhash
xs.simhash(["我曾经失落失望失掉所有方向", "直到看见平凡才是唯一的答案"])
# Minhash
xs.minhash(["我曾经失落失望失掉所有方向", "直到看见平凡才是唯一的答案"])
# Ngram(适用于英文文本)
xs.ngram(["When life gives you lemons", "eat watermelons"])
```

### 聚类
#### 计算Kmeans Clustering示例
```python
import xiangshi as xs
arg = [
    "我曾经失落失望失掉所有方向", 
    "直到看见平凡才是唯一的答案", 
    "我曾经跨过山和大海", 
    "也穿过人山人海", 
    "转眼都飘散如烟",
    "我曾经拥有着的一切", 
    "也哭也笑平凡着",
    "那片笑声让我想起我的那些花儿",
]
# 第一个输入值为组的数量，需要聚类成三个组就为3
# 第二个输入值为Data
# 第三个输入值为是否需要Clusters的中心，True为需要，False为不需要默认值为False
xs.kmeans(3, arg, WithKeys=True) 
```
注意：kmeans自动TFIDF加权且用欧几里得距离算出文本之间的距离

#### 计算Kmeans的K值示例
```python
import xiangshi as xs
arg = [
    "我曾经失落失望失掉所有方向", 
    "直到看见平凡才是唯一的答案", 
    "我曾经跨过山和大海", 
    "也穿过人山人海", 
    "转眼都飘散如烟",
    "我曾经拥有着的一切", 
    "也哭也笑平凡着",
    "那片笑声让我想起我的那些花儿",
]
# 第一个输入值为Data
xs.calk(arg) 
```
注意：calk()从0到MaxNum算出每个Kmeans并找出最优K值，其中因为算量较大所以会导致时间较长。下一个版本将会支持以C为内核的多线程Kmeans

### 计算TF，IDF，TFIDF
```python
import xiangshi as xs
xs.GetTF(corpus) # corpus为文本，必须先分词好
xs.GetIDF(corpus, lists) # corpus和lists为文本，必须先分词好
xs.GetTFIDF(corpus, lists) # corpus和lists为文本，不用分词
```

### 其它加权方法
```python
xs.weight = "tf"
xs.weight = "tfidf"
```
如果是TFIDF加权的话将用于IDF的文本加在原来的list后面。
假如原来是：
｀xs.cossim(["我曾经失落失望失掉所有方向", "直到看见平凡才是唯一的答案"])｀
则TFIDF加权为
```python
arg = [
    "我曾经失落失望失掉所有方向", 
    "直到看见平凡才是唯一的答案", 
    "我曾经跨过山和大海", # 用于TFIDF
    "也穿过人山人海", # 用于TFIDF
    "转眼都飘散如烟", # 用于TFIDF
    "我曾经拥有着的一切", # 用于TFIDF
    "也哭也笑平凡着", # 用于TFIDF
    "那片笑声让我想起我的那些花儿", # 用于TFIDF
]
xs.cossim(arg)
```

### 其他函数
```python
import xiangshi as xs
xs.file2list(file1, file2, EncodeArg="utf-8") # v3.0.0用文件输入的可以先用这个转为list再进行文本相似度计算
xs.SegDepart(corpus) # 分词＋停用词过滤
xs.dict2file(dict) # Dict到File
xs.SortDict(dict) # Dict排序
```

### 修改默认函数
```python
import xiangshi as xs
#计算TFIDF时是否使用log，True是使用，False是不使用。默认值为True
xs.UseLog = True
#计算Simhash时取前多少的TFIDF值。默认值为64
xs.feature = 64
#计算Minhash时算出多少个哈希值。默认值为16
xs.HashNums = 16
#计算Minhash时的最大哈希。默认值为4294967311
xs.prime = 4294967311
```

## 其他链接
  - 在线计算文本计算器:
  https://xs.datavisdev.com
  - English Version of README.md:
  https://github.com/kiwirafe/xiangshi/blob/master/README(Eng).md
  - Change Log:
  https://github.com/kiwirafe/xiangshi/blob/master/CHANGES.md
  - Pypi:
  https://pypi.org/project/xiangshi/
  - Github:
  https://github.com/kiwirafe/xiangshi
  - 下载数量:
  https://pepy.tech/project/xiangshi
  - Gitee（中国开源）:
  https://gitee.com/kiwirafe/xiangshi
  - 关于算法的其他链接:
  https://github.com/kiwirafe/xiangshi/blob/master/LINKS.md


## 相识寓意
>同是天涯沦落人，相逢何必曾**相识**

## MIT License
Copyright (c) [2021] [Kiwirafe]

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
