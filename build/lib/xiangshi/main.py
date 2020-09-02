import os
import re
import math
import sys
import jieba
import random
import hashlib
import binascii


class calculator(object):
    def __init__(self):
        self.UseLog = True
        self.FileDir = ""
        self.InputTarget = 0
        self.feature = 64
        self.HashNums = 16
        self.prime = 4294967311
        self.MaxHash = 2**32 - 1

    def CheckInputType(self, input):
        if isinstance(input, str) == True:
            return "f"
        elif isinstance(input, list) == True:
            return "l"
        else:
            raise Exception("Only lists and files are supported by now.")

    #中文分词
    def SegDepart(self, sentence):
        StopWords = [line.strip() for line in open("stoptext.txt", encoding='utf-8').readlines()]
        SentenceDepart = jieba.cut(sentence.strip())

        output = []
        for word in SentenceDepart:
            if word not in StopWords:
                if word != '\n':
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
        
        if self.CheckInputType(input) == "f":
            try:
                with open(input, encoding='utf-8') as f:
                    corpus = f.read()
            except:
                with open(input, encoding='gbk') as f:
                    corpus = f.read()
        else:
            corpus = "".join(input)

        LineSplit = re.split(r'[。！；？，]', corpus.strip()) #按符号分句

        for line in LineSplit:
            temp = self.SegDepart(line)
            result.extend(temp)
        return result

    def SortDict(self, input):
        return dict(sorted(input.items(), \
            key=lambda kv: kv[1], reverse=True))

    def HashString(self, s):
        h = hashlib.sha256(s.encode('utf-8'))
        return bin(int(h.hexdigest(), 16))[-self.feature:]

    # Following h(x) = (a*x + b) % c
    def HashAlg(self, k):
        # Create a list of 'k' random values.
        RandomList = []
        
        while k > 0:
            # Get a random shingle ID.
            random.seed(k)
            RandIndex = random.randint(0, self.MaxHash) 
        
            # Ensure that each random number is unique.
            while RandIndex in RandomList:
                RandIndex = random.randint(0, self.MaxHash) 
            
            # Add the random number to the list.
            RandomList.append(RandIndex)
            k = k - 1
            
        return RandomList

    #计算TF值 
    def GetTF(self, input):
        corpus = self.input2list(input)
        tf = {}
        for x in corpus:
            tf[x] = corpus.count(x)
        
        wordsSum = sum(tf.values())
        for key, value in tf.items(): 
            tf[key] = value / wordsSum
        return tf

    #计算IDF值
    def GetIDF(self, input):
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
            if self.FileDir == "":
                self.FileDir = input.rsplit('/', 1)[0] + "/"

            for inputname in os.listdir(self.FileDir):
                FileLists.append(self.input2list(self.FileDir + inputname))
        
        else:
            FileLists = input
        
        total = len(FileLists)

        #对于每个文档
        for word in corpus:
            #对于文档中的每个词，统计其在文档中的出现频率
            for x in FileLists:
                if word in x:
                    freq[word] += 1

        for word in freq:
            #idf的公式
            TempIDF = total / (freq[word] + 1)
            if self.UseLog == True:
                idf[word] = math.log(TempIDF)
            else:
                idf[word] = TempIDF
        return idf
    
    def GetTFIDF(self, input):

        if self.CheckInputType(input) == "l":
            tf = self.GetTF(input[self.InputTarget])
            idf = self.GetIDF(input)
        elif self.CheckInputType(input) == "f":
            tf = self.GetTF(input)
            idf = self.GetIDF(input)
        else:
            raise Exception("Not appropriate InputTarget") 

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
    
    def simhash(self, input1, input2):
        TFIDFResult = self.SortDict(self.GetTFIDF(input1))
        TFIDFResult2 = self.SortDict(self.GetTFIDF(input2))

        FirstResults = {}
        FirstResults2 = {}

        i = 0
        for key, value in TFIDFResult.items():
            FirstResults[key] = value
            i += 1
            if i >= self.feature:
                break

        i = 0
        for key, value in TFIDFResult2.items():
            FirstResults2[key] = value
            i += 1
            if i >= self.feature:
                break

        result = FirstResults
        result2 = FirstResults2

        HashResults = {}
        HashResults2 = {}
        
        for key, value in result.items():
            HashResults[self.HashString(key)] = value
        
        for key, value in result2.items():
            HashResults2[self.HashString(key)] = value

        result = []
        result2 = []

        i = 0
        for key, value in HashResults.items():
            result.append([])
            for x in key:
                if int(x) == 0:
                    result[i].append(value * -1)
                else:
                    result[i].append(value)
            i += 1

        i = 0
        for key, value in HashResults2.items():
            result2.append([])
            for x in key:
                if int(x) == 0:
                    result2[i].append(value * -1)
                else:
                    result2[i].append(value)
            i += 1

        FinalResult = []
        FinalResult2 = []
        
        for i in range(self.feature):
            FinalResult.append(0)
            for x in result:
                FinalResult[i] += x[i]

            FinalResult2.append(0)
            for x in result2:
                FinalResult2[i] += x[i]

        FinalString = ""
        for x in FinalResult:
            if x > 0:
                FinalString += "1"
            else:
                FinalString += "0"

        FinalString2 = ""
        for x in FinalResult2:
            if x > 0:
                FinalString2 += "1"
            else:
                FinalString2 += "0"

        hamming = 0
        for i, x in enumerate(FinalString):
            if x != FinalString2[i]:
                hamming += 1
        
        return 1 - hamming / self.feature

    def minhash(self, input1, input2):
        result = self.GetTFIDF(input1)
        result2 = self.GetTFIDF(input2)


        coeff1 = self.HashAlg(self.HashNums)
        coeff2 = self.HashAlg(self.HashNums)

        signature = set()
        signature2 = set()

        MinhashNum = self.prime
        MinhashNum2 = self.prime
        for i in range(0, self.HashNums):
            for x in result.keys():
                crc = binascii.crc32(x.encode('utf-8')) & 0xffffffff
                #Generating Hash
                HashCode = (coeff1[i] * crc + coeff2[i]) % self.prime
                # Track the lowest hash code seen.
                if HashCode < MinhashNum:
                    MinhashNum = HashCode
                
                signature.add(MinhashNum)

            for y in result2.keys():
                crc = binascii.crc32(y.encode('utf-8')) & 0xffffffff
                HashCode2 = (coeff1[i] * crc + coeff2[i]) % self.prime
                if HashCode2 < MinhashNum2:
                    MinhashNum2 = HashCode2
                
                signature2.add(MinhashNum2)
            
        appear = 0
        AllSignature = list(signature) + list(signature2)
        for x in AllSignature:
            if x in signature and x in signature2:
                appear += 1
            
        return appear / len(AllSignature)