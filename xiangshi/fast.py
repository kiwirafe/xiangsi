import os
import re
import math
import jieba

class calculatorfast(object):

    # 对句子进行中文分词
    def SegDepart(self, sentence):
        SysPath = os.path.dirname(os.path.abspath(__file__))
        StopWords = [line.strip() for line in open(SysPath + \
            "/stoptext.txt", encoding='utf-8').readlines()]
        SentenceDepart = jieba.cut(sentence.strip())

        output = []
        for word in SentenceDepart:
            if word not in StopWords:
                if word != '\n':
                    output.append(word)
        return output

    def input2list(self, input):
        result = []
        
        try:
            with open(input, encoding='utf-8') as f:
                corpus = f.read()
        except:
            with open(input, encoding='gbk') as f:
                corpus = f.read()

        LineSplit = re.split(r'[。！；？，]', corpus.strip()) #按符号分句

        for line in LineSplit:
            temp = self.SegDepart(line)
            result.extend(temp)
        return result

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
    def GetIDF(self, input):
        corpus = self.input2list(input)

        freq = {}
        for x in corpus:
            freq[x] = 0
            
        idf = {}
        FileLists = []
        FileDir = input.rsplit('/', 1)[0] + "/"

        for inputname in os.listdir(FileDir):
            FileLists.append(self.input2list(FileDir + inputname))
        
        
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
            idf[word] = math.log(TempIDF)
        return idf
    
    def GetTFIDF(self, input):
        """doc_id是语料库中文档的id，input是txt的路径"""
        tf = self.GetTF(input)
        idf = self.GetIDF(input)

        result = {}

        for key, value in tf.items():
            result[key] = value * idf[key]
        
        return result

    def cossim(self, input1, input2):
        result = self.GetTFIDF(input1)
        result2 = self.GetTFIDF(input2)

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

        FinalResult = round(TopSum / (math.sqrt(sq1) * math.sqrt(sq2)), 4)
        return FinalResult
