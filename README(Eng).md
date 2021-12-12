# Xiangshi

#### Chinese Text Similarity Calculator
#### Cossine, Simhash, Minhash Similarity Calculator

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

### Usage Method
#### Calculate Text Similarity
##### Cosine Similarity
```python
import xiangshi as xs
xs.cossim(["I was once disappointed and lost in all directions", "Until seeing ordinary is the only answer"])
```
#### Simhash & Minhash Similarity
```python
import xiangshi as xs
xs.simhash(["I was once disappointed and lost in all directions", "Until seeing ordinary is the only answer"]) # Simhash
xs.minhash(["I was once disappointed and lost in all directions", "Until seeing ordinary is the only answer"]) # Minhash
```

### Clustering
#### Calculating Kmeans Clustering example
```python
import xiangshi as xs
arg = [
    "I was once disappointed and lost in all directions",
    "Until seeing ordinary is the only answer",
    "I used to cross the mountains and the sea",
    "Also across the sea of ​​people",
    "In a blink of an eye it is scattered like smoke",
    "Everything I Owned",
    "Cry and laugh",
    "That piece of laughter reminds me of my flowers",
]
# The first input value is the number of clusters, which is 3 if the strings need to be clustered into three groups
# The second input value is the raw data
xs.kmeans(3, arg)
```
Note: kmeans automatically weights with TFIDF and uses Euclidean Distance to calculate the distance between strings
(For the time being, other weights and other distances such as Cosine Similarity are not supported)

Result format: `LoopX-String: [Cluster]`,
(Loop)X is the number of clustering loops, String is the central string of the Cluster, and are the contents of the clusters

#### Calculating the K value of Kmeans
```python
import xiangshi as xs
arg = [
    "I was once disappointed and lost in all directions",
    "Until seeing ordinary is the only answer",
    "I used to cross the mountains and the sea",
    "Also across the sea of ​​people",
    "In a blink of an eye it is scattered like smoke",
    "Everything I Owned",
    "Cry and laugh ordinary",
    "That piece of laughter reminds me of my flowers",
]
# The first input value is the raw data
# The second input value is the MaxNum
xs.calk(arg, 5)
```
Note: calk() calculates each Kmeans from 0 to MaxNum and finds the optimal K value, which will lead to a longer time because of the large amount of calculation. The next version will support multi-threaded Kmeans with C as the core

### Calculate TF, IDF, TFIDF
```python
import xiangshi as xs
xs.GetTF(corpus) # Corpus is text, it must be segmented first
xs.GetIDF(corpus, lists) # Corpus and lists are text, it must be segmented first
xs.GetTFIDF(corpus, lists) # Corpus and lists are text, no need for segmentation
```

### Other weighting methods
####
```python
xs.weight = "tf"
xs.weight = "tfidf"
```
If it is TFIDF weight, append the text used for IDF to the original list.
For example if it used to be like below when used as default
｀xs.cossim(["I was disappointed and lost in all directions", "Until seeing ordinary is the only answer"])｀
Then cbange it like below when using TFIDF weight
```python
arg = [
    "I was once disappointed and lost in all directions",
    "Until seeing ordinary is the only answer",
    "I used to cross the mountains and the sea",
    "Also across the sea of ​​people",
    "In a blink of an eye it is scattered like smoke",
    "Everything I Owned",
    "Cry and laugh ordinary",
    "That piece of laughter reminds me of my flowers",
]
xs.cossim(arg)
```

### Other functions
```python
import xiangshi as xs
xs.file2list(file1, file2, EncodeArg="utf-8") # For v3.0.0 if you are using file input, you can use this to convert to a list and then perform Text Similarity calculations
xs.SegDepart(corpus) # Word segmentation + stop word filtering
xs.dict2file(dict) # Dict to File
xs.SortDict(dict) # Dict sort
```

### Modify the default function
```python
import xiangshi as xs
xs.UseLog = True
# Whether log is used when calculating TFIDF, True is using, False is not using. The default value is True
xs.feature = 64
# The first TFIDF values used when calculating Simhash. The default value is 64
xs.HashNums = 16
# Calculate the number of hash values ​​when calculating Minhash. The default value is 16
xs.prime = 4294967311
# Calculate the maximum hash when calculating Minhash. The default value is 4294967311
```

## Other links:
  - Chinese Version of README.md:
  https://github.com/kiwirafe/xiangshi/blob/master/README.md
  - Change Log
  https://github.com/kiwirafe/xiangshi/blob/master/CHANGES.md
  - Pypi:
  https://pypi.org/project/xiangshi/
  - Github:
  https://github.com/kiwirafe/xiangshi
  - Pypi Downloads:
  https://pepy.tech/project/xiangshi
  - Gitee (Chinese Open Source):
  https://gitee.com/kiwirafe/xiangshi

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
