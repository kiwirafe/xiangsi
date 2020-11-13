import os
import re
import math
import sys
import logging
import jieba
import random
import hashlib
import formats
import CacheFile
import importlib
import time

FormatList = formats.FormatList


class functions(object):
    def __init__(self):
        self.SysPath = os.path.dirname(os.path.abspath(__file__))
        self.UseLog = True
        self.FileDir = ""
        self.InputTarget = 0

    # 中文分词
    def SegDepart(self, sentence):
        StopWords = [line.strip() for line in open(self.SysPath + \
            "/stoptext.txt", encoding='utf-8').readlines()]
        SentenceDepart = jieba.cut(sentence.strip())
        output = []
        for word in SentenceDepart:
            if word not in StopWords:
                if word != '\n' and word != ' ':
                    output.append(word)

        return output

    def dict2file(self, result, name="result.txt"):
        open(name, "w").close()
        f = open(name, "a")
        
        for key, value in result.items():
            f.write(str(key) + ": " + str(value) + "\n")
        f.close()
        self.logger.info("Result saved in" + name)

    def input2list(self, input):
        result = []
        try:
            try:
                with open(input, encoding='utf-8') as f:
                    corpus = f.read()
            except UnicodeDecodeError:
                with open(input, encoding='gb18030') as f:
                    corpus = f.read()
        except UnicodeDecodeError:
            with open(input, encoding='gbk') as f:
                corpus = f.read()

        LineSplit = re.split(r'[。，；！？]', corpus.strip()) # 按符号分句

        for line in LineSplit:
            temp = self.SegDepart(line)
            result.extend(temp)
        return result

    def dir2list(self, input):
        importlib.reload(CacheFile)
        files = {}
        if input.count("/") > 0:
            TempDir = self.FileDir or input.rsplit("/")[0] + "/"
        else:
            TempDir = "./"
        for inputname in os.listdir(TempDir):
            TempName = TempDir + inputname
            if TempName in CacheFile.tfidfs:
                files[TempName] = CacheFile.tfidfs[TempName]
            else:
                if inputname.endswith(tuple(FormatList)):
                    listed = self.input2list(TempName)
                    files[TempName] = listed
                    self.cache(TempName, listed)
                else:
                    logging.debug("File Format Not Supported: " + inputname)

        return files

    def SortDict(self, input):
        return dict(sorted(input.items(), \
            key=lambda kv: kv[1], reverse=True))

    def HashString(self, s):
        h = hashlib.sha256(s.encode('utf-8'))
        return bin(int(h.hexdigest(), 16))[-self.feature:]

    # 公式 h(x) = (a*x + b) % c
    def HashAlg(self, k):
        MaxHash = 2**32 - 1
        #  Create a list of 'k' random values.
        RandomList = []
        
        while k > 0:
            #  Get a random shingle ID.
            random.seed(k)
            RandIndex = random.randint(0, MaxHash) 
        
            # 确保数字唯一
            while RandIndex in RandomList:
                RandIndex = random.randint(0, MaxHash) 
            
            # Append值
            RandomList.append(RandIndex)
            k = k - 1
            
        return RandomList
    
    def cache(self, input, tfidf):
        s = open("CacheFile.py", "r", encoding="utf-8").read().split(" #  End")
        f = open("CacheFile.py", "w", encoding="utf-8")
        s[0] = s[0][:-1]
        f.write(s[0] + "\t" + "\"" + input + "\"" + ": ")
        f.write(str(tfidf) + ",\n")
        f.write("} #  End" + s[1])
        f.close()

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
                for filel in lists.values():
                    if word in filel:
                        freq[word] += 1

        for word in freq:
            # IDF的公式
            TempIDF = total / (freq[word] + 1)
            if self.UseLog == True:
                idf[word] = math.log(TempIDF)
            else:
                idf[word] = TempIDF
        return idf

    def GetTFIDF(self, input):
        if isinstance(input, list) is True:
            tf = self.GetTF(input[self.InputTarget])
            idf = self.GetIDF(input[self.InputTarget], input)
        elif isinstance(input, str) is True:
            if os.path.isfile(input) is not True:
                raise Exception("Wrong File: " + input)
            files = self.dir2list(input)
            tf = self.GetTF(files[input])
            idf = self.GetIDF(files[input], files)
            
        result = {}

        for key, value in tf.items():
            result[key] = value * idf[key]

        return result
