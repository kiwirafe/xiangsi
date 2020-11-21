# 相识(Xiangshi)

### 中文文本相似度计算器
[![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=Pypi%20Version)](https://img.shields.io/pypi/v/xiangshi)
[![Pypi Downloads](https://static.pepy.tech/personalized-badge/xiangshi?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads)](https://pepy.tech/project/xiangshi)
[![Pypi and Github License](https://img.shields.io/pypi/l/xiangshi?label=Pypi%20and%20Github%20License)](https://img.shields.io/github/license/kiwirafe/xiangshi)
[![Language](https://img.shields.io/github/languages/top/kiwirafe/xiangshi)](https://github.com/kiwirafe/xiangshi)

相识是一款专门为中文打造的文本相似度计算器。
这是唯一也是最好的中文文本相似度计算器。

相识的优势有：
  - 专攻中文文本相似度比较
  - 支持余弦和N-gram算法
  - 支持Simhash和Minhash算法
  - 100%Python语言
  - 自动TFIDF过滤
  - 可以单独计算TF和IDF
  - 支持List和File两种类型
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

### 版本v3.0.0来了！
  - 减少时间，10-15s减少至0.1-3s
  - 增加N-gram算法
  - 增加Format
  - 修改重要IDF Bug
  - 增加Developement版本
  - 修改Logging

  版本v3.0.1:
  - 修复List输入
  - 暂时删除Fast版本（速度并不如相识）

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
xs.simhash(Input1, Input2) # Simhash
xs.minhash(Input1, Input2) # Minhash
```
 - 计算文本相似度时自动由TFIDF过滤
 - Input1 - 第一个输入值，可以是文件的地址或是一个列表
 - Input2 - 第二个输入值，可以是文件的地址或是一个列表

### 计算TF，IDF，TFIDF
```python
import xiangshi as xs
xs.GetTF(Input)
xs.GetIDF(Input)
xs.GetTFIDF(Input)
```
**相识自动从同一Folder里来计算IDF**，具体方法请到*计算文本相似度的Input类型*

### 其它加权方法
#### 
```python
from xiangshi import tfweight as xs #只有TF加权
from xiangshi import noweight as xs #不加权
# 其他使用一样
```

### 其他函数
```python
import xiangshi as xs
xs.input2list(Input) #分词
xs.dir2list(dict) #Dir到List
xs.dict2file(dict) #Dict到File
xs.SortDict(dict) #Dict排序
```

### 修改默认函数
```python
import xiangshi as xs
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
  |_input1.txt
  |_input2.txt
  |_Other Files 3 ~ 10.txt（自动用于IDF的计算）
```
列表：
```py
input1 = ["相识是一款专门为中文打造的文本相似度计算器"]
input2 = ["相识是唯一也是最好的中文文本相似度计算器"]
]
```
**相识自动从同一Folder里所有支持的文件类型来计算IDF**
如果需要设定，使用：
```python
xs.FileDir = ""
```
侧可在想要的Folder里的计算IDF

### 计算文件的类型
目前相识默认有**两种文件**类型来计算IDF：
```
.doc
.txt
```
如果需要增加，请**先用Python自己试验一下**，是否能读取所想要的结果，
不然读取的话全是乱码。
测试代码如下：
```python
f = open("file.xlsx", "r", encoding="utf-8") 
# Encoding需要自己调试，中文常用的有：
# utf-8, gbk, gbk2312, gbk18030
print(f)
```
#### 增加 & 删除
```python
from xiangshi import formats
formats.AppendFormat(".xlsx") #增加
formats.RemoveFormat(".xlsx") #删除
```

### Development
这里是给二次开发者使用的，目前只支持余弦相似度。
```python
from xiangshi import dev as xs
```
使用方法请自己看源代码

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