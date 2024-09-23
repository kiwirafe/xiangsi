import math
import jieba
import random
import pickle
import string
import re

class Functions(object):
    def __init__(self):
        self.lang = "zh"
        self.weight = "Default"

    # Algorithm: h(x) = (a*x + b) % c
    def HashAlg(self, k):
        MaxHash = 2**32 - 1
        # Create a list of 'k' random values.
        RandomList = []
        
        while k > 0:
            random.seed(k)
            # Get a random shingle ID.
            RandIndex = random.randint(0, MaxHash) 
        
            # Make sure the hash is unique
            while RandIndex in RandomList:
                RandIndex = random.randint(0, MaxHash) 
            
            # Append the value
            RandomList.append(RandIndex)
            k = k - 1
            
        return RandomList


    def update_stopwords(self, stopwords, lang="zh"):
        with open(f"xiangshi/stopword_{lang}", 'w') as f:
            for word in stopwords:
                f.write(f"{word}\n")


    def segment_zh(self, corpus):
        path = "xiangshi/stoptext_zh.txt"
        StopWords = [line.strip() for line in open(path, encoding='utf-8').readlines()]
        
        WordCut = jieba.lcut(corpus)

        output = []
        for word in WordCut:
            word = word.lower()
            if word not in StopWords and word != '\n' and word != ' ':
                output.append(word)
        
        return output

    def segment_en(self, corpus):
        path = "xiangshi/stoptext_en.txt"
        StopWords = [line.strip() for line in open(path, encoding='utf-8').readlines()]
        
        WordCut = [word.strip(string.punctuation) for word in corpus.split()]

        output = []
        for word in WordCut:
            word = word.lower()
            if word not in StopWords and word != '\n' and word != ' ':
                output.append(word)
        
        return output


    def segment(self, corpus):
        if re.search(r'[\u4e00-\u9fff]', corpus) or self.lang == "zh":
            return self.segment_zh(corpus)
        else:
            return self.segment_en(corpus)
    
    
    def construct(self, data):
        segmented = []
        for d in data:
            WordCut = self.segment(d)
            segmented.append(WordCut)

        with open("xiangshi/cache.pickle", "wb") as handle:
            pickle.dump(segmented, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def GetTF(self, corpus):
        tf = {}
        total = len(corpus)
        for word in corpus:
            tf[word] = corpus.count(word) / total
        
        return tf
    

    def GetIDF(self, corpus, data):
        freq = dict.fromkeys(corpus, 0)
            
        idf = {}
        total = len(data)

        for word in corpus:
            for d in data:
                if word in d:
                    freq[word] += 1

        for word in freq:
            idf[word] = math.log10(total / (freq[word] + 1))
        return idf
    

    def GetTFIDF(self, input):
        tf = self.GetTF(input)
        idf = self.GetIDF(input, pickle.load(open('xiangshi/cache.pickle', 'rb')))

        result = {}
        for key, value in tf.items():
            result[key] = value * idf[key]

        return result
    
    
    def GetWeight(self, input):
        input = self.segment(input)
        if self.weight == "TFIDF":
            return self.GetTFIDF(input)
        elif self.weight == "None":
            weight = {}
            for word in input:
                weight[word] = 1
            return weight
        else:
            weight = {}
            for word in input:
                weight[word] = input.count(word)
            return weight
