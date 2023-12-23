import os
import math
import jieba
import random
import pickle

class Functions(object):
    def __init__(self):
        self.SysPath = os.path.dirname(os.path.abspath(__file__))
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


    def segment(self, sentence):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stoptext.txt")
        StopWords = [line.strip() for line in open(path, \
                encoding='utf-8').readlines()]
        
        WordCut = jieba.lcut(sentence.strip())

        output = []
        for word in WordCut:
            word = word.lower()
            if word not in StopWords and word != '\n':
                output.append(word)
        
        return output
    
    
    def construct(self, data):
        SegmentedData = []
        for d in data:
            WordCut = self.segment(d)
            SegmentedData.append(WordCut)

        with open('cache.pickle', 'wb') as handle:
             pickle.dump(SegmentedData, handle, protocol=pickle.HIGHEST_PROTOCOL)


    def GetTF(self, corpus):
        tf = {}
        total = len(corpus)
        for x in corpus:
            tf[x] = corpus.count(x) / total
        
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
            TempIDF = total / (freq[word] + 1)
            idf[word] = math.log10(TempIDF)
        return idf
    

    def GetTFIDF(self, input):
        tf = self.GetTF(input)
        idf = self.GetIDF(input, pickle.load(open('cache.pickle', 'rb')))

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
