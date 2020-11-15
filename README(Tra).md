# 相識(Xiangshi)

### 中文文本相似度計算器
[![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=Pypi%20Version)](https://img.shields.io/pypi/v/xiangshi)
[![Pypi Downloads](https://static.pepy.tech/personalized-badge/xiangshi?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads)](https://pepy.tech/project/xiangshi)
[![Pypi and Github License](https://img.shields.io/pypi/l/xiangshi?label=Pypi%20and%20Github%20License)](https://img.shields.io/github/license/kiwirafe/xiangshi)
[![Language](https://img.shields.io/github/languages/top/kiwirafe/xiangshi)](https://github.com/kiwirafe/xiangshi)

相識是一款專門爲中文打造的文本相似度計算器。
這是唯一也是最好的中文文本相似度計算器。

相識的優勢有：
  - 專攻中文文本相似度比較
  - 支持餘弦和N-gram算法
  - 支持Simhash和Minhash算法
  - 100%Python語言
  - 自動TFIDF過濾
  - 可以單獨計算TF和IDF
  - 支持List和File兩種類型
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

### 版本v3.0.0來了！
  - 減少時間，10-15s減少至0.1-3s
  - 增加N-gram算法
  - 增加Format
  - 修改重要IDF Bug
  - 增加Developement版本
  - 修改Logging

## 使用方法
### 計算文本相似度
#### 餘弦相似度
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
 - 計算文本相似度時自動由TFIDF過濾
 - Input1 - 第一個輸入值，可以是文件的地址或是一個列表
 - Input2 - 第二個輸入值，可以是文件的地址或是一個列表

### 計算TF，IDF，TFIDF
```python
import xiangshi as xs
xs.GetTF(Input)
xs.GetIDF(Input)
xs.GetTFIDF(Input)
```
**相識自動從同一Folder里來計算IDF**，具體方法請到*計算文本相似度的Input類型*

### 其它加權方法
#### 
```python
from xiangshi import tfweight as xs #只有TF加權
from xiangshi import noweight as xs #不加權
# 其他使用一樣
```

### 其他函數
```python
import xiangshi as xs
xs.input2list(Input) #分詞
xs.dir2list(dict) #Dir到List
xs.dict2file(dict) #Dict到File
xs.SortDict(dict) #Dict排序
```

### 修改默認函數
```python
import xiangshi as xs
xs.UseLog = True
#計算TFIDF時是否使用log，True是使用，False是不使用。默認值爲True
xs.FileDir = ""
#計算IDF時其他文件的目錄。默認值爲""
xs.InputTarget = 0
#輸入列表時指定計算的目標。默認值爲1
xs.feature = 64
#計算Simhash時取前多少的TFIDF值。默認值爲64
xs.HashNums = 16
#計算Minhash時算出多少個哈希值。默認值爲16
xs.prime = 4294967311
#計算Minhash時的最大哈希。默認值爲4294967311
```

### 計算文本相似度的Input類型
目前相識支持兩種類型 - 文件和列表
文件：
```
data/
  |_test1.txt
  |_test2.txt
  |_test3 ~ 10.txt（自動用於IDF的計算）
```
列表：
```py
data = [
  ["相識是一款專門爲中文打造的文本相似度計算器"]
  ["相識是唯一也是最好的中文文本相似度計算器"]
  ["相識支持Cosine, Simhash, Minhash Similarity"] #用於IDF的計算
  ["有問題一定要在Github上提Issue"] #用於IDF的計算
  ["有改進一定要在Github上提Pull Request"] #用於IDF的計算
]
```
**相識自動從同一Folder里所有支持的文件類型來計算IDF**
如果需要設定，使用：
```python
xs.FileDir = ""
```
側可在想要的Folder里的計算IDF

### 計算文件的類型
目前相識默認有**兩種文件**類型來計算IDF：
```
.doc
.txt
```
如果需要增加，請**先用Python自己試驗一下**，是否能讀取所想要的結果，
不然讀取的話全是亂碼。
測試代碼如下：
```python
f = open("file.xlsx", "r", encoding="utf-8") 
# Encoding需要自己調試，中文常用的有：
# utf-8, gbk, gbk2312, gbk18030
print(f)
```
#### 增加 & 刪除
```python
from xiangshi import formats
formats.AppendFormat(".xlsx") #增加
formats.RemoveFormat(".xlsx") #刪除
```

### Development
這裡是給二次開發者使用的，目前只支持餘弦相似度。
```python
from xiangshi import dev as xs
```
使用方法請自己看源代碼

## 其他鏈接：
  - English Version of README.md:
  https://github.com/kiwirafe/xiangshi/blob/master/README(Eng).md
  - Change Log（沒事就看一看）
  https://github.com/kiwirafe/xiangshi/blob/master/CHANGES.md
  - Pypi: 
  https://pypi.org/project/xiangshi/
  - Github:
  https://github.com/kiwirafe/xiangshi
  - 下載數量:
  https://pepy.tech/project/xiangshi
  - Gitee（中國開源）:
  https://gitee.com/kiwirafe/xiangshi

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