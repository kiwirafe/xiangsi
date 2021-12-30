import math
import logging
import binascii
from . import func

funcs = func.functions

logging.getLogger("jieba").disabled = True
try:
    logging.basicConfig(filename="xiangshi.log",
    filemode='a',
    format='%(asctime)s - %(levelname)s %(message)s',
    datefmt='%D, %H:%M:%S',
    level=logging.DEBUG)
except PermissionError:
    logging.info("No Permission")

class calculator(funcs):
    def __init__(self):
        super(calculator, self).__init__()
        self.feature = 64
        self.HashNums = 16
        self.prime = 4294967311
        self.weight = "no"

    def cossim(self, input):
        # Vectorize the inputs
        result = self.init(input, 0)
        result2 = self.init(input, 1)

        # Merge the two results into a major list
        merge = result.copy()
        merge.update(result2)
        WordSet = list(merge.keys())

        # Make the merges results a dict (key: word, value:i) 
        WordDict = {}
        for i, x in enumerate(WordSet):
            WordDict[x] = i

        # Initialize two lists with 
        # default values of 0 and the length of the merged results
        Result1Cut = [0] * len(WordDict)
        Result2Cut = [0] * len(WordDict)

        # If the word appears in the merged result then assign the vector values
        # else it stays as 0
        for word in result.keys():
            Result1Cut[WordDict[word]] = result[word]

        for word in result2.keys():
            Result2Cut[WordDict[word]] = result2[word]

        # Calculate the Euclidean Distance
        TopSum = 0
        sq1 = 0
        sq2 = 0
        for i in range(len(Result1Cut)):
            TopSum += Result1Cut[i] * Result2Cut[i]
            sq1 += pow(Result1Cut[i], 2)
            sq2 += pow(Result2Cut[i], 2)

        # Calculate the Cosine Similarity
        try:
            FinalResult = TopSum / (math.sqrt(sq1) * math.sqrt(sq2))
        except ZeroDivisionError:
            FinalResult = 0.0

        FinalResult = round(FinalResult, 12)
        return FinalResult
    
    def ngram(self, input, num=2):
        result = [] 
        for i in range(len(input[0]) - num + 1):
            result.append(input[0][i:i + num]) 

        result2 = [] 
        for i in range(len(input[1]) - num + 1):
            result2.append(input[1][i:i + num]) 

        cnt = 0 
        for i in result:
            for j in result2:
                if i == j:
                    cnt += 1

        return (cnt / len(result) + cnt / len(result2)) / 2

    def simhash(self, input):
        # Vectorize the inputs
        TFIDFResult = self.SortDict(self.init(input, 0))
        TFIDFResult2 = self.SortDict(self.init(input, 1))

        # Use the first 64 words as the features to import speed
        # If the features are weighted then we have used the most important ones
        # otherwise we just have used random one
        # but it still won't significantý change our result
        result = {k: TFIDFResult[k] for k in list(TFIDFResult)[:self.feature]}
        result2 = {k: TFIDFResult2[k] for k in list(TFIDFResult2)[:self.feature]}

        # Hash the results into 64 bit binary
        HashResults = {}
        HashResults2 = {}
        
        for key, value in result.items():
            HashResults[bin(int(self.HashString(key), 16))[-self.feature:]] = value    
        for key, value in result2.items():
            HashResults2[bin(int(self.HashString(key), 16))[-self.feature:]] = value

        # Weight the binaries, 0 as neg and 1 as pos
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

        # Add the two binaries
        FinalResult = []
        FinalResult2 = []
        
        for i in range(self.feature):
            FinalResult.append(0)
            for x in result:
                FinalResult[i] += x[i]

            FinalResult2.append(0)
            for x in result2:
                FinalResult2[i] += x[i]

        # Weight the added binary, 0 as neg and 1 as pos
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

        # Calculate the Hamming Distance
        hamming = 0
        for i, x in enumerate(FinalString):
            if x != FinalString2[i]:
                hamming += 1

        # Calculate the Simhash Similarity(which is 1 - Hamming Distance)
        return 1 - hamming / self.feature

    def minhash(self, input):
        result = self.init(input, 0)
        result2 = self.init(input, 1)

        coeff1 = self.HashAlg(self.HashNums)
        coeff2 = self.HashAlg(self.HashNums)

        signature = {}
        signature2 = {}

        MinhashNum = self.prime
        MinhashNum2 = self.prime
        for i in range(0, self.HashNums):
            for x in result.keys():
                crc = binascii.crc32(x.encode('utf-8')) & 0xffffffff
                # Generating Hash
                HashCode = (coeff1[i] * crc + coeff2[i]) % self.prime
                #  Track the lowest hash code seen.
                if HashCode < MinhashNum:
                    MinhashNum = HashCode
                
                if MinhashNum not in signature:
                    signature[MinhashNum] = result[x]

            for y in result2.keys():
                crc = binascii.crc32(y.encode('utf-8')) & 0xffffffff
                HashCode2 = (coeff1[i] * crc + coeff2[i]) % self.prime
                if HashCode2 < MinhashNum2:
                    MinhashNum2 = HashCode2
                
                if MinhashNum2 not in signature2:
                    signature2[MinhashNum2] = result2[y]
        
        intersect = 0
        total = 0
        for x, y in signature.items():
            if x in signature2:
                intersect += y
            total += y

        return intersect / total