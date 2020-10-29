# 相識(Xiangshi)

### 中文文本相似度計算器
[![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=Pypi%20Version)](https://img.shields.io/pypi/v/xiangshi)
[![Downloads](https://pepy.tech/badge/xiangshi)](https://pepy.tech/project/xiangshi)
[![Pypi and Github License](https://img.shields.io/pypi/l/xiangshi?label=Pypi%20and%20Github%20License)](https://img.shields.io/github/license/kiwirafe/xiangshi)
[![Language](https://img.shields.io/github/languages/top/kiwirafe/xiangshi)](https://github.com/kiwirafe/xiangshi)

相識是壹款專門為中文打造的文本相似度計算器。這是唯壹也是最好的中文文本相似度計算器

相識的優勢有：
  - 專攻中文文本相似度比較
  - 使用余弦計算，Simhash和Minhash兩種算法
  - 100%Python語言
  - 自動TFIDF過濾
  - 可以單獨計算TF和IDF
  - 支持List和File兩種類型
  - 支持多個文件相似度比較
  - 高效、迅速
  - 安裝容易
  - 100%開源
  - 長期維護和更新

## 下載與安裝
Pip安裝：
```sh
$ pip3 install xiangshi
```
國內較慢的話可以使用清華鏡像：
```sh
$ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple xiangshi
```

### 版本v2.1.1~v2.3.0來了！
  - v2.1.1: 支持只有TF的加權
  - v2.1.2：Minhash加權選定用Quantization-Based來實現
  - v2.1.3: Minhash由set轉為dict，與v1.0.1原因壹樣
  - v2.2.0：
    - Minhash加權成功
    - 使用Quantization-Based算法
    - 具體用Multiset實現
  - v2.2.1: 增加CHANGES.md
  - v2.2.2: README更新，更多註釋
  - v2.3.0: 使用Logging，所有運算記錄均保存在xiangshi.log
  - v2.3.1: 發現Stoptext無法使用
  - v2.3.2: Pip加入Stoptext
  - v2.3.3: Stoptext由所相識文件裏調用，而不是從運行地點裏調用
  - v2.4.0：
    - 相識極速版並入相識
    - 減少時間，20~30s減少至10~15s
    - 完全支持列表

## 使用方法
### 計算文本相似度
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
 - 計算文本相似度時自動由TFIDF過濾
 - Input1 - 第壹個輸入值，可以是文件的地址或是壹個列表
 - Input2 - 第二個輸入值，可以是文件的地址或是壹個列表

#### 計算TF，IDF，TFIDF
```python
import xiangshi as xs
xs.GetTF(Input)
xs.GetIDF(Input)
xs.GetTFIDF(Input)
```
#### 其他函數
```python
import xiangshi as xs
xs.input2list(Input) #分詞
xs.dict2file(dict) #Dict到File
xs.SortDict(dict) #Dict排序
xs.HashString(str) #哈希Str
```

### 修改默認函數
```python
import xiangshi as xs
xs.TFIDF = True 
#是否使用TFIDF，True是使用TFIDF，False是只是用TF。默認值為True
xs.UseLog = True
#計算TFIDF時是否使用log，True是使用，False是不使用。默認值為True
xs.FileDir = ""
#計算IDF時其他文件的目錄。默認值為""
xs.InputTarget = 0
#輸入列表時指定計算的目標。默認值為1
xs.feature = 64
#計算Simhash時取前多少的TFIDF值。默認值為64
xs.HashNums = 16
#計算Minhash時算出多少個哈希值。默認值為16
xs.prime = 4294967311
#計算Minhash時的最大哈希。默認值為4294967311
```

### 計算文本相似度的Input類型
目前相識支持兩種類型 - 文件和列表
文件：
```
data/
  |_test1.txt
  |_test2.txt
  |_test3 ~ 10.txt（用於IDF的計算）
```
列表：
```py
data = [
  ["相識是壹款專門為中文打造的文本相似度計算器"]
  ["相識是唯壹也是最好的中文文本相似度計算器"]
  ["相識支持Cosine, Simhash, Minhash Similarity"] #用於IDF的計算
  ["有問題壹定要在Github上提Issue"] #用於IDF的計算
  ["有改進壹定要在Github上提Pull Request"] #用於IDF的計算
]
```

## 其他鏈接：
  - English Version of README.md:
  https://github.com/kiwirafe/xiangshi/blob/master/README(Eng).md
  - Change Log（沒事就看壹看）
  https://github.com/kiwirafe/xiangshi/blob/master/CHANGES.md
  - Pypi: 
  https://pypi.org/project/xiangshi/
  - Github:
  https://github.com/kiwirafe/xiangshi
  - 下載數量:
  https://pepy.tech/project/xiangshi
  - Gitee（中國開源）:
  https://gitee.com/kiwirafe/xiangshi
  - 清華鏡像鏈接:
  https://pypi.tuna.tsinghua.edu.cn/simple/xiangshi/

## 相識寓意
>與君初**相識**，
猶如故人歸。
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