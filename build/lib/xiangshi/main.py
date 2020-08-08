import os
import re
import math
import jieba 
from decimal import Decimal
import time

class calculator(object):
    def CheckInputType(self, input):
        if isinstance(input, str) == True:
            return "f"
        elif isinstance(input, list) == True:
            return "l"
        else:
            raise Exception("Only lists and files are supported by now.")


    # 对句子进行中文分词
    def SegDepart(self, sentence):
        # 对文档中的每一行进行中文分词
        StopWords = [line.strip() for line in open("stoptext.txt", encoding='utf-8').readlines()]
        SentenceDepart = jieba.cut(sentence.strip(), cut_all=False)
        # 输出结果为output
        output = []
        # 去停用词
        for word in SentenceDepart:
            if word not in StopWords:
                if word != '\t':
                    output.append(word)
        return output

    def dict2file(self, result, name="result.txt"):
        open(name, "w").close()
        f = open(name, "a")
        
        for key, value in result.items():
            f.write(str(key) + ": " + str(value) + "\n")
        f.close()
        print("Result saved in", name)

    def input2list(self, input):
        result = []
        
        with open(input, encoding='gbk') as f:
            corpus = f.read()
            LineSplit = re.split(r'[。！；？，]', corpus.strip()) #按符号分句

        for line in LineSplit:
            temp = self.SegDepart(line)
            result.extend(temp)
        return result

    def SortDict(self, input):
        return dict(sorted(input.items(), \
            key=lambda kv: kv[1], reverse=True))

    #计算tf值 
    def GetTF(self, input):
        corpus = self.input2list(input)
        tf = {}
        for x in corpus:
            tf[x] = corpus.count(x)
        
        wordsSum = sum(tf.values())
        for key, value in tf.items(): 
            tf[key] = value / wordsSum
        return tf

    #计算idf值
    def GetIDF(self, input, UseLog=True, InputTarget=None):
        if self.CheckInputType(input) == "f":
            corpus = self.input2list(input)
        else:
            corpus = input

        freq = {}
        for x in corpus:
            freq[x] = 0
            
        idf = {}
        FileLists = []
        if self.CheckInputType(input) == "f":
            FileDir = input.rsplit('/', 1)[0] + "/"

            for inputname in os.listdir(FileDir):
                FileLists.append(self.input2list(FileDir + inputname))
        
        else:
            FileLists = input
        
        total = len(FileLists)

        #对于每个文档
        for word in corpus:
            #对于文档中的每个词，统计其在文档中的出现频率
            for x in FileLists:
                if word in x:
                    freq[word] += 1

        #将每个词的出现次数转换为idf值    
        for word in freq:
            #idf的公式
            TempIDF = total / (freq[word] + 1)
            if UseLog == True:
                idf[word] = math.log(TempIDF)
            else:
                idf[word] = TempIDF
        return idf
    
    def GetTFIDF(self, input, UseLog=True, InputTarget=None):
        """doc_id是语料库中文档的id，input是txt的路径"""

        if isinstance(InputTarget, str) == True:
            tf = self.GetTF(InputTarget)
            idf = self.GetIDF(input, UseLog, InputTarget)
        elif isinstance(InputTarget, int) == True and self.CheckInputType(input) == "l":
            tf = self.GetTF(input[InputTarget])
            idf = self.GetIDF(input, UseLog, input[InputTarget])
        elif InputTarget == None:
            tf = self.GetTF(input)
            idf = self.GetIDF(input)
        else:
            raise Exception("Not appropriate InputTarget") 

        result = {}

        for key, value in tf.items():
            result[key] = value * idf[key]
        
        return result

    def cal(self, input1, input2, UseLog=True, InputTarget1=None, InputTarget2=None):
        result = self.GetTFIDF(input1, UseLog, InputTarget1)
        result2 = self.GetTFIDF(input2, UseLog, InputTarget2)

        merge = result.copy()
        merge.update(result2)
        WordSet = list(dict.fromkeys(merge.keys()))
        WordDict = {}

        for i, x in enumerate(WordSet):
            WordDict[x] = i


        Result1Cut = [0] * len(WordDict)
        for word in result.keys():
            Result1Cut[WordDict[word]] = result[word]

        Result2Cut = [0] * len(WordDict)
        for word in result2.keys():
            Result2Cut[WordDict[word]] = result2[word]

        TopSum = 0
        sq1 = 0
        sq2 = 0
        for i in range(len(result)):
            TopSum += Result1Cut[i] * Result2Cut[i]
            sq1 += pow(Result1Cut[i], 2)
            sq2 += pow(Result2Cut[i], 2)

        FinalResult = round(Decimal(TopSum) / Decimal(math.sqrt(sq1) * math.sqrt(sq2)), 4)
        return FinalResult