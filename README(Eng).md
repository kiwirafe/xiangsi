# Xiangshi

#### Chinese Text Similarity Calculator + Text Clustering

[![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=Pypi%20Version)](https://img.shields.io/pypi/v/xiangshi)
[![Downloads](https://pepy.tech/badge/xiangshi)](https://pepy.tech/project/xiangshi)

Xiangshi is a Text Similarity Calculator that mainly focuses on Chinese. It also supports Kmeans Clustering.

## Download and install
PIP installation:
```sh
pip3 install xiangshi
```

## Usage Method
### Calculate Text Similarity
#### Cosine Similarity
```python
import xiangshi as xs
xs.cossim("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
```
#### Simhash & Minhash Similarity
```python
import xiangshi as xs
# Simhash
xs.simhash("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
# Minhash
xs.minhash("如何更换花呗绑定银行卡", "花呗更改绑定银行卡")
```

### Other Weighting Methods
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

### Modify Default Arguments
```python
import xiangshi as xs
xs.feature = 64
# The first TFIDF values used when calculating Simhash. The default value is 64
xs.HashNums = 16
# Calculate the number of hash values ​​when calculating Minhash. The default value is 16
xs.prime = 4294967311
# Calculate the maximum hash when calculating Minhash. The default value is 4294967311
```

## Other Links:
  - Chinese Version of README.md:
  https://github.com/kiwirafe/xiangshi/blob/master/README.md
  - PyPI:
  https://pypi.org/project/xiangshi/
  - Github:
  https://github.com/kiwirafe/xiangshi
  - PyPI Downloads:
  https://pepy.tech/project/xiangshi
  - Gitee (Chinese Open Source):
  https://gitee.com/kiwirafe/xiangshi

### MIT License
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
