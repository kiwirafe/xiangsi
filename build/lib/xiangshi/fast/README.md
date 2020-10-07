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
$ pip3 install XiangshiFast
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

SAME AS XIANGSHI

