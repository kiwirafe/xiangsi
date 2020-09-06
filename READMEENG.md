# Xiangshi

#### Chinese text similarity calculator

Pypi Version Downloads Pypi and Github License Language
[![Pypi Version](https://img.shields.io/pypi/v/xiangshi?label=Pypi%20Version)](https://img.shields.io/pypi/v/xiangshi)
[![Downloads](https://pepy.tech/badge/xiangshi)](https://pepy.tech/project/xiangshi)
[![Pypi and Github License](https://img.shields.io/pypi/l/xiangshi?label=Pypi%20and%20Github%20License)](https://img.shields.io/github/license/kiwirafe/xiangshi)
[![Language](https://img.shields.io/github/languages/top/kiwirafe/xiangshi)](https://github.com/kiwirafe/xiangshi)

Xiangshi is a text similarity calculator specially designed for Chinese. This is the only and the best Chinese text similarity calculator

The advantages of Xiangshi are:

  - Focus on Chinese text similarity comparison
  - Cosine calculation and simhash algorithm are used
  - 100% Python language
  - Automatic TFIDF filtering
  - TF and IDF can be calculated separately
  - List and file are supported
  - Support multiple file similarity comparison
  - Efficient and quick
  - Easy to install
  - 100% open source
  - Long term maintenance and renewal

### Download and install
PIP installation:
```sh
$ pip3 install xiangshi
```
If it is slow in China, you can use Tsinghua image:
```sh
$ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple xiangshi
```

### Usage method

#### Calculate text similarity

##### Cosine similarity

import xiangshi as xs

xs.cossim (Input1, Input2)

##### Simhash & Minhash similarity
```py
import xiangshi as xs
# Simhash
xs.simhash (Input1, Input2)
# Minhash
xs.minhash (Input1, Input2)
```
  - When calculating the text similarity, it is automatically filtered by TFIDF
  - Input1 - the first input value, which can be the address of a file or a list
  - Input2 - the second input value, which can be the address of a file or a list

##### Calculate TF, IDF, TFIDF

import xiangshi as xs

xs.GetTF (Input)

xs.GetIDF (Input)

xs.GetTFIDF （Input)

Input - input value, which can be the address of a file or a list

Input type for calculating text similarity

At present, two types of acquaintance are supported: file and list file



data/

Wei test1.txt

Wei test2.txt

Wei test3 ~ 10.txt

List (function is not perfect yet)



data = [

test1.txt

test2.txt

test3 ~ 10.txt

]

Version history

V0.1.0: initial version

TFIDF only

The amount of calculation is large

V0.1.1: version modification

V0.1.2: virus repair

V0.1.3: detail modification

V0.1.4: TF, IDF and TFIDF are completely disconnected

V0.2.0: alpha version on GitHub

Remove the redundant loops

Using Python library function

The calculation time is increased by 30 times

V0.2.1: PIP preparation

V0.2.2: virus repair

V0.2.3: officially released on GitHub

V0.3.0: PIP release

V0.3.1: add readme on pip

V0.3.2: readme adds download and usage instructions

V0.3.3: modified on pip to allow users to use various functions directly

V1.0.0: support text similarity calculation

Support cosine similarity

Cosine similarity: the cosine value of the angle between two vectors is calculated to evaluate their similarity

Use- xs.cossim (Input1, Input2)

V1.0.1: set is no longer used, because the order of the two texts will be different, resulting in a huge difference in the results (0.1 for the first time and 0.9 for the second time). The solution to the problem is to keep the order of dict at the beginning, so that there is no randomness in the calculation.

V1.0.2: increase decimal precision calculation

V1.0.3: added stoptext, previously missing

V1.0.4: function automatically becomes PIP function

V1.1.0: added dict2file function

v1.2.0:

Increase the speed version of acquaintance, only support cosine similarity and file type, but increase the speed by 10%

V1.2.1: readme update, more comments

V1.2.2: canceling decimal calculation is not different from reservation

v1.3.0:

Gitee (Chinese version of GitHub) is released to make domestic users more convenient to use

Some cosine, TFIDF input into the class variable, making the call function more convenient

V1.3.1: virus repair

V1.3.2: support Tsinghua image, make it easier for domestic users to download

V1.3.3 (v2.0.0 beta): v2.0.0 beta released on GitHub and gitee

v2.0.0 Beta:

Add simhash algorithm

Simhash algorithm is suitable for large text analysis, and it is recommended to use more than 500 words

Use- xs.simhash (Input1, Input2)

Add minhash algorithm

Minhash algorithm is similar to simhash.

Use- xs.minhash (Input1, Input2)


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
