## Xiangsi

### Text Similarity Calculator

![Pypi Version](https://img.shields.io/pypi/v/xiangsi?label=version)
![Downloads](https://static.pepy.tech/badge/xiangshi)

**[简体中文](README.md)** | English
  
Xiangsi is a Python package for calculating text similarity. It provides 4 algorithms: Cosine Similarity, Jaccard Similarity, Simhash and Minhash. 

[Online Text Similarity Calculator](https://kiwirafe.pythonanywhere.com/app/xiangsi)

## Installation
Pip install:
```sh
pip3 install xiangsi
```

## Usage
### Calculate Text Similarity
#### Cosine
```python
import xiangsi as xs
xs.cossim("A mathematician found a solution to the problem.", "The problem was solved by a young mathematician.")
```
#### Simhash & Minhash & Jaccard
```python
import xiangsi as xs
# Simhash
xs.simhash("A mathematician found a solution to the problem.", "The problem was solved by a young mathematician.")
# Minhash
xs.minhash("A mathematician found a solution to the problem.", "The problem was solved by a young mathematician.")
# Jaccard
xs.jaccard("A mathematician found a solution to the problem.", "The problem was solved by a young mathematician.")
```

### Modify Weights
#### Default weight (frequency of the words).
```python
import xiangsi as xs
xs.simhash("A mathematician found a solution to the problem.", "The problem was solved by a young mathematician.")
```

#### TFIDF
For TF-IDF, first construct the IDF corpus. This calculates the IDF for all the strings inside the corpus. You only need to do this once for multiple calculations, given that you are using the same IDF corpus.

```python
import xiangsi as xs

arg = [
    "There was a time in his life when her rudeness would have set him over the edge.",
    "He would have raised his voice and demanded to speak to the manager.",
    "That was no longer the case. He barely reacted at all, letting the rudeness melt away without saying a word back to her. ",
    "A mathematician found a solution to the problem."
    "The problem was solved by a young mathematician."
] # IDF 
xs.weight = "TFIDF" # Set weight method as TFIDF
xs.construct(arg) # Constructs the IDF corpus. We only need to do this once.
xs.cossim("A mathematician found a solution to the problem.", "The problem was solved by a young mathematician.")
```

#### No weight (all words have weight 1)
```python
import xiangsi as xs

xs.weight = "None"
xs.cossim("A mathematician found a solution to the problem.", "The problem was solved by a young mathematician.")
```

### Modify Default Variables
```python
import xiangsi as xs
xs.feature = 64
# The first TFIDF values used when calculating Simhash. The default value is 64
xs.HashNums = 16
# Calculate the number of hash values ​​when calculating Minhash. The default value is 16
xs.prime = 4294967311
# Calculate the maximum hash when calculating Minhash. The default value is 4294967311
```

## Other Links:
  - PyPI:
  https://pypi.org/project/xiangsi/
  - Github:
  https://github.com/kiwirafe/xiangsi
  - PyPI Downloads:
  https://pepy.tech/project/xiangsi
