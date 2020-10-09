# 相识极速版(XiangshiFast)

#### 相识极速版是相识的加速版本。

#### 相识正式版本请到
#### https://github.com/kiwirafe/xiangshi 或
#### https://pypi.org/project/xiangshi/ 

#### 相识极速版现在已和相识合并！

相识与极速版的比较：
```
Functions       | Xiangshi     | XiangshiFast 
Cossim          | ✅           | ✅
Simhash         | ✅           | ❌
Minhash         | ✅           | ❌

GetTF           | ✅           | ✅
GetIDF          | ✅           | ✅
GetTFIDF        | ✅           | ✅

Stop Words      | ✅           | ✅
input2list      | ✅           | ✅
dict2file       | ✅           | ❌
SortDict        | ✅           | ❌
Logging         | ✅           | ❌
Choose TF/TFIDF | ✅           | ❌

File Input      | ✅           | ✅
List Input      | ✅           | ❌
String Input    | Projected    | ❌

Speed           | 10 ~ 15s     | 5 ~ 7s
```

### 下载与安装
```sh
$ pip3 install xiangshi
```

### 使用方法
##### 计算文本相似度
```py
from xiangshi import fast as xsf
xsf.cossim(Input1, Input2):
```
 - 计算文本相似度时自动由TFIDF过滤
 - Input1 - 第一个输入值，可以是文件的地址或是一个列表
 - Input2 - 第二个输入值，可以是文件的地址或是一个列表

### MIT License
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
