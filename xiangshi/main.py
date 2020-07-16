import os
import re
import math
import jieba 

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
        StopWords = ["、","“", "”","#","$","：","‘","’", "(",")","*","+", "\n"]
        # 对文档中的每一行进行中文分词
        SentenceDepart = jieba.cut(sentence.strip(), cut_all=False)
        # 输出结果为output
        output = []
        # 去停用词
        for word in SentenceDepart:
            if word not in StopWords:
                if word != '\t':
                    output.append(word)
        return output

    def input2list(self, input):
        result = []
        
        if self.CheckInputType(input) == "f":
            with open(input, encoding='gbk') as f:
                corpus = f.read()
                LineSplit = re.split(r'[。！；？，]', corpus.strip()) #按符号分句
        else:
            LineSplit = re.split(r'[。！；？，]', input.strip()) #按符号分句

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
    def GetIDF(self, input, InputTarget=None, UseLog=True):
        tf = self.GetTF(InputTarget)

        freq = {}
        for x in tf:
            freq[x] = 0
            
        idf = {}
        
        FileLists = []
        if self.CheckInputType(input) == "f":
            FileDir = input.rsplit('/', 1)[0] + "/"

            for inputname in os.listdir(FileDir):
                FileLists.append(self.input2list(FileDir + inputname))
        
        else:
            for x in input:
                FileLists.append(self.input2list(x))
        
        total = len(FileLists)

        #对于每个文档
        for word in tf:
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
    
    def get(self, input, InputTarget=None, UseLog=True):
        """doc_id是语料库中文档的id，input是txt的路径"""

        if isinstance(InputTarget, str) == True:
            tf = self.GetTF(InputTarget)
            idf = self.GetIDF(input, InputTarget, UseLog)
        elif isinstance(InputTarget, int) == True and self.CheckInputType(input) == "l":
            tf = self.GetTF(input[InputTarget])
            idf = self.GetIDF(input, input[InputTarget], UseLog)
        else:
            raise Exception("Not appropriate InputTarget") 

        result = {}

        for key, value in tf.items():
            result[key] = value * idf[key]

        result = dict(sorted(result.items(), \
            key=lambda kv: kv[1], reverse=True))
        
        return result