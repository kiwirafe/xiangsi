import os
import re
import math
import sys
import logging
import jieba
import random
import time
import formats

FormatList = formats.FormatList

class calculator(object):
    def __init__(self):
        self.SysPath = os.path.dirname(os.path.abspath(__file__))
        self.UseLog = True
        self.FileDir = ""
        self.m = 1
        self.n = 1
        self.top = 700
        self.random = True

    #中文分词
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
        print("Result saved in" + name)

    def input2list(self, input):
        result = []
        try:
            try:
                with open(input, encoding='utf-8') as f:
                    corpus = f.read()
            except:
                with open(input, encoding='gbk') as f:
                    corpus = f.read()
        except:
            with open(input, encoding='gb18030') as f:
                    corpus = f.read()

        LineSplit = re.split(r'[。，；！？]', corpus.strip()) #按符号分句

        for line in LineSplit:
            temp = self.SegDepart(line)
            result.extend(temp)
        return result

    def dir2list(self, input):
        files = {}
        TempDir = self.FileDir
        for inputname in os.listdir(TempDir):
            if inputname.endswith(tuple(FormatList)):
                files[TempDir + inputname] = self.input2list(TempDir + inputname)
            else:
                logging.debug("File Format Not Supported: " + inputname)

        return files

    def SortDict(self, input):
        return dict(sorted(input.items(), \
            key=lambda kv: kv[1], reverse=True))

    #计算TF值 
    def GetTF(self, corpus):
        WordsSum = len(corpus)

        tf = {}
        for word in corpus: 
            wordtf = corpus.count(word) / WordsSum
            tf[word] = pow(wordtf, self.m)

        return tf

    #计算IDF值
    def GetIDF(self, corpus, lists):
        freq = dict.fromkeys(corpus, 0)
            
        idf = {}
        total = len(lists)

        #对于文档中的每个词，统计其在文档中的出现频率
        for word in corpus:
            if freq[word] == 0:
                for filel in lists.values():
                    if word in filel:
                        freq[word] += 1

        for word in freq:
            #IDF的公式
            TempIDF = total / (freq[word] + 1)
            if self.UseLog == True:
                wordidf = pow(math.log(TempIDF), self.n)
                idf[word] = wordidf
            else:
                wordidf = pow(TempIDF, self.n)
                idf[word] = wordidf
        return idf
    
    def GetTFIDF(self, input):
        if os.path.isfile(input) != True:
            raise Exception("Wrong File: " + input)
        files = self.dir2list(input)
        tf = self.GetTF(files[input])
        idf = self.GetIDF(files[input], files)

        result = {}

        for key, value in tf.items():
            result[key] = value * idf[key]

        return result


    def FilterResult(self, input1, input2):
        result = self.GetTFIDF(input1)
        result2 = self.GetTFIDF(input2)

        output = dict()
        output2 = dict()

        if self.top != "All":
            if self.random == True:
                #随机选前top个值
                try:
                    output = dict(random.sample(result.items(), self.top))
                except:
                    print("self.top is larger than text 1 but handled")
                    output = result
                
                try:
                    output2 = dict(random.sample(result2.items(), self.top))
                except:
                    print("self.top is larger than text 2 but handled")
                    output2 = result2
            else:
                #按顺序选前top个值
                sorted = list(self.SortDict(result).items())[:self.top]
                sorted2 = list(self.SortDict(result2).items())[:self.top]

                output = dict(sorted)
                output2 = dict(sorted2)

            return output, output2
        else:
            print("All = True, returned the same")
            return result, result2


    def cossim(self, input1, input2):
        #取TFIDF值
        result, result2 = self.FilterResult(input1, input2)

        #Merge两个Result
        merge = result.copy()
        merge.update(result2)
        WordSet = list(merge.keys())

        #做一个Dict，每个词标上顺序
        WordDict = {}
        for i, x in enumerate(WordSet):
            WordDict[x] = i

        #做两个List，目前全为0
        Result1Cut = [0] * len(WordDict)
        Result2Cut = [0] * len(WordDict)

        #如果出现的话就为加权值，不出现的话为0
        for word in result.keys():
            Result1Cut[WordDict[word]] = result[word]

        for word in result2.keys():
            Result2Cut[WordDict[word]] = result2[word]

        #欧几里得距离
        TopSum = 0
        sq1 = 0
        sq2 = 0
        for i in range(len(Result1Cut)):
            TopSum += Result1Cut[i] * Result2Cut[i]
            sq1 += pow(Result1Cut[i], 2)
            sq2 += pow(Result2Cut[i], 2)

        #余弦相似度
        try:
            FinalResult = TopSum / (math.sqrt(sq1) * math.sqrt(sq2))
        except ZeroDivisionError:
            FinalResult = 0.0

        FinalResult = round(FinalResult, 12)
        return FinalResult




sim = calculator()

#m为TF的次方，默认值为1
#sim.m = 12
#m为IDF的次方，默认值为1
#sim.n = 13

#top为前n个数，默认值为All（全选）
#sim.top = "All" / 12

#是否random，默认值True
#sim.random = True / False

#目录，默认值 "/""
#sim.FileDir = ""

#是否用Log，，默认值True
#sim.UseLog = True / False

res = sim.cossim("NoDupData/text1.txt", "NoDupData/text10.txt")
print(res)