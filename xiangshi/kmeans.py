from . import main
import random
import math
import multiprocessing

cal = main.calculator

class KmeansCalculator(cal):
    def __init__(self):
        super(KmeansCalculator, self).__init__()

    def mean(self, lst):
        result = []
        for i in range(len(lst[0])):
            TempLs = ([item[i] for item in lst])
            result.append(sum(TempLs) / len(TempLs))

        return result
                

    def EuclideanDistance(self, a, b):    
        ans = 0
        for i in range(len(a)):
            ans += pow(a[i] - b[i], 2)
            
        return ans

    def variation(self, dct):
        lengths = [len(v) for v in dct.values()]
        lengths.sort()

        average = sum(lengths) / len(lengths)
        power = [pow(i - average, 2) for i in lengths]
        try:
            power = sum(power) / (len(lengths) - 1)
            power = math.sqrt(power)

            return power / average
        except ZeroDivisionError:
            return math.inf

    def GetTFIDFs(self, dir):
        TFIDFFiles = {}
        for i in range(len(dir)):
            TFIDFFiles[dir[i]] = self.init(dir, target=i)

        """TFIDFFiles Looks Like:
            {Text1: {"Hey": 1, "Im": 2, "Here" :3}}
            {Text2: {"You" : 1, "Sure" :2, "?" :3}}
        """
        WordSet = {}
        # Merge所有Result
        for words in TFIDFFiles.values():
            WordSet.update(words)

        # 做一个Dict，每个词标上顺序
        WordDict = {}
        for i, word in enumerate(WordSet):
            WordDict[word] = i

        CompletedList = {}
        # 如果出现的话就为加权值，不出现的话为0
        for FKey, FValue in TFIDFFiles.items():
            ResultCut = [0] * len(WordDict)
            for word in FValue.keys():
                ResultCut[WordDict[word]] = FValue[word]

            CompletedList[FKey] = ResultCut

        return CompletedList

    def InitCluster(self, k, dir):
        tfidfs = self.GetTFIDFs(dir)

        DefaultClusters = {}
        clustered = {}

        random.seed(1)
        for _ in range(k):
            key, value = random.choice(list(tfidfs.items()))
            
            DefaultClusters[key] = value
            clustered[key] = []

        for TfidfsKey, TfidfsValue in tfidfs.items():
            lowest = math.inf
            SoonAdd = ""
            for DefaultKey, DefaultValue in DefaultClusters.items():
                if TfidfsKey in DefaultClusters.keys():
                    continue
                EucDis = self.EuclideanDistance(TfidfsValue, DefaultValue)
                if EucDis < lowest:
                    lowest = EucDis
                    SoonAdd = DefaultKey
            
            if SoonAdd != "":
                clustered[SoonAdd].append(TfidfsKey)

        return clustered, tfidfs

    def kcluster(self, k, dir):
        clustered, tfidfs = self.InitCluster(k, dir) #安排初始聚类
        num = len(list(tfidfs.values())[0])

        means = {}
        NeedCal = []

        # 计算DefaultCluster中的
        for DefaultCluster, DefaultValue in clustered.items():
            if len(DefaultValue) > 0:
                for lst in DefaultValue:
                    NeedCal.append(tfidfs[lst])
            
                means["Loop0-" + DefaultCluster] = self.mean(NeedCal)
                num = len(means["Loop0-" + DefaultCluster])
            else:
                means["Loop0-" + DefaultCluster] = [0] * num
            NeedCal = []

        """Means Looks Like:
            {New-Text1: [1, 2, 3, 4]}
            {New-Text2: [1, 2, 3, 4]}
        """
        
        i = 1
        save = {}
        while True:
            MeanedResult = {}

            for key in means.keys():
                MeanedResult[key] = []

            for TfidfsKey, TfidfsValue in tfidfs.items():
                lowest = math.inf
                SoonAdd = ""
                for MeanKey, MeanValue in means.items():
                    EucDis = self.EuclideanDistance(TfidfsValue, MeanValue)
                    if EucDis < lowest:
                        lowest = EucDis
                        SoonAdd = MeanKey
                
                MeanedResult[SoonAdd].append(TfidfsKey)

            if i > 2:
                truth = []
                for CheckKey, CheckValue in MeanedResult.items():
                    SaveKey = CheckKey.replace(str(i), str(i - 1), 1)

                    if list(CheckValue) == list(save[SaveKey]):
                        truth.append(True)

                if truth.count(True) == len(MeanedResult):
                    return MeanedResult

            means = {}
            save = MeanedResult

            for key, value in MeanedResult.items():
                for lst in value:
                    NeedCal.append(tfidfs[lst])

                if len(NeedCal) > 0:
                    means["Loop" + str(i + 1) + key[5:]] = self.mean(NeedCal)
                NeedCal = []
            
            i += 1

    def kmeans(self, k, dir):
        for _ in range(k):
            lowest = math.inf
            result = {}
            longest = self.kcluster(k, dir)

            if self.variation(longest) <= lowest:
                result = longest

        return result
            
    def calk(self, dir, MaxNum):
        inputs = []
        for i in range(1, MaxNum):
            inputs.append((i, dir))

        with multiprocessing.Pool(4) as p:
            dct = p.starmap(self.kmeans, inputs)

        diffs = []

        for mean in dct:
            diff = (MaxNum - i) * self.variation(mean) #要乘以(11 - i)是要让数字变大
            diffs.append(diff)
        

        d = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]

        # 找出最优K
        NumLowest = 0
        stop = 0
        for i, num in enumerate(d):
            if num < 0:
                num = num * - 1

            if num >= NumLowest and num != math.inf:
                NumLowest = num
                stop = i

        return stop + 1
