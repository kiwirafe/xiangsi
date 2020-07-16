# Xiangshi

#### 中文文本相似度计算器
[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

相识是一款专门为中文打造的文本相似度计算器。这是唯一也是最好的中文文本相似度计算器

相识的优势有：
  - 多个文本相似度比较
  - 使用TFIDF算法和Python语言
  - 可以单独计算TF和IDF
  - 支持List和File两种类型
  - 高效、迅速
  - 安装容易

#### 版本1.0.0来了！
 - 在pip上发布
 - 在github上发布
 - 暂时还无法计算文本相似度，只能算TFIDF

### 下载与安装
```sh
$ pip3 install jeiba
$ pip3 install xiangshi
```
[Jeiba](https://stackoverflow.com/questions/40832533/pip-or-pip3-to-install-packages-for-python-3)是一个中文分词软件
pip3也可以是pip根据个人环境选择
### 使用方法
```
import xiangshi as xs
xs.get("Input", "InputTarget", UseLog")
```
 - Input - 输入值，可以是文件的地址或是一个列表
 - InputTarget - 文件类型不需要，使用None就可以了（不填也行）
 - UseLog - 是否使用L，默认是使用，不使用的话设定为False（如果不使用的话InputTarget一定要填）

### MIT License
Copyright (c) [2020] [相识]

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

