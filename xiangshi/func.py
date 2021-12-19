import os
import math
import logging
import jieba
import random
import hashlib
import codecs
import pickle
from .stoptext import StopWords

class functions(object):
    def __init__(self):
        self.SysPath = os.path.dirname(os.path.abspath(__file__))
        self.UseLog = True

    # 中文分词
    def SegDepart(self, sentence):
        try:
            cached = pickle.load(open('cache', 'rb'))
        except:
            cached = {}

        hashed = self.HashString(sentence)
        if hashed not in cached:
            cache = open('cache', 'wb')
            SentenceDepart = jieba.lcut(sentence.strip())
            output = []
            for word in SentenceDepart:
                if word not in StopWords:
                    output.append(word)
            cached[hashed] = output
            if len(cached) > 50:
                cached.pop(next(iter(cached)))
            pickle.dump(cached, cache)
            cache.close()
        else:
            output = cached[hashed]
        
        return output
    
    def file2list(self, input1, input2, EncodeArg="utf-8"):
        if os.path.isfile(input1) is False:
            raise Exception("Wrong File: " + input1)
        #return files
        elif os.path.isfile(input2) is False:
            raise Exception("Wrong File: " + input2)
    
        files = []
        TempDir = os.path.dirname(input1) or "."
        TempDir += "/"

        for inputname in os.listdir(TempDir):
            TempName = TempDir + inputname
            if inputname == input1:
                files.insert(0, TempName)
            elif inputname == input2:
                files.insert(1, TempName)

            if inputname.endswith(".txt"):
                with open(TempName, encoding=EncodeArg) as f:
                    corpus = f.read()
                files.append(corpus)
            else:
                logging.debug("File Format Not Supported: " + inputname)

        return files

    def dict2file(self, result, name="result.txt"):
        open(name, "w").close()
        f = codecs.open(name, "a", "utf-8")
        
        for key, value in result.items():
            f.write(str(key) + ": " + str(value) + "\n")
        f.close()
        logging.info("Result saved in" + name)

    def SortDict(self, input):
        return dict(sorted(input.items(), \
            key=lambda kv: kv[1], reverse=True))

    def HashString(self, s):
        return hashlib.sha256(s.encode('utf-8')).hexdigest()

    # 公式 h(x) = (a*x + b) % c
    def HashAlg(self, k):
        MaxHash = 2**32 - 1
        # Create a list of 'k' random values.
        RandomList = []
        
        while k > 0:
            random.seed(k)
            # Get a random shingle ID.
            RandIndex = random.randint(0, MaxHash) 
        
            # 确保数字唯一
            while RandIndex in RandomList:
                RandIndex = random.randint(0, MaxHash) 
            
            # Append值
            RandomList.append(RandIndex)
            k = k - 1
            
        return RandomList

    def Get1(self, corpus):
        one = {}
        for x in corpus:
            one[x] = 1
        return one

    # 计算TF值 
    def GetTF(self, corpus):
        WordsSum = len(corpus)

        tf = {}
        for word in corpus: 
            tf[word] = corpus.count(word) / WordsSum

        return tf

    # 计算IDF值
    def GetIDF(self, corpus, lists):
        freq = dict.fromkeys(corpus, 0)
            
        idf = {}
        total = len(lists)

        # 对于文档中的每个词，统计其在文档中的出现频率
        for word in corpus:
            if freq[word] == 0:
                if word in lists:
                    freq[word] += 1

        for word in freq:
            # IDF的公式
            TempIDF = total / (freq[word] + 1)
            if self.UseLog == True:
                idf[word] = math.log(TempIDF)
            else:
                idf[word] = TempIDF
        return idf

    def GetTFIDF(self, input, lists):
        IDFInput = []
        for x in lists:
            if x != input:
                WordCut = self.SegDepart(x)
                IDFInput += WordCut

        tf = self.GetTF(input)
        idf = self.GetIDF(input, IDFInput)
            
        result = {}

        for key, value in tf.items():
            result[key] = value * idf[key]

        return result

    # A function that vectorizes the inputs
    def init(self, input, target=0):
        if self.weight == "TF":
            return self.GetTF(self.SegDepart(input[target]))
        elif self.weight == "TFIDF":
            return self.GetTFIDF(input[target], input)
        else:
            return self.Get1(self.SegDepart(input[target]))