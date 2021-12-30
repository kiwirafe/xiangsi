from . import main
import random
import math

cal = main.calculator

class KmeansCalculator(cal):
    def __init__(self):
        super(KmeansCalculator, self).__init__()
        self.n_init = 10
        self.max_iter = 100

    # x̄ = Σ item[i]
    def mean(self, lst):
        result = []
        for i in range(len(lst[0])):
            TempLst = ([item[i] for item in lst])
            result.append(sum(TempLst) / len(TempLst))

        return result
                

    def EuclideanDistance(self, a, b):    
        ans = 0
        for i in range(len(a)):
            ans += pow(a[i] - b[i], 2)
            
        return ans

    # Calculate the variation within clusters
    def variation(self, dct):
        tfidfs = self.GetTFIDFs(dir)
        variances = 0
        for key, value in dct.items():
            variance = 0
            for subvalue in value:
                variance += self.EuclideanDistance(tfidfs[key], tfidfs[subvalue])
            variances += variance / len(value)

        return variances / len(dct)

    def IfChanged(self, dict1, dict2):
        for CheckKey, CheckValue in dict1.items():
            if CheckValue != dict2[CheckKey]:
                return False
        return True

    def kneed(self, variances):
        diffs = []
        FirstVariance = variances[0]
        steep = FirstVariance / len(variances)
        for i, variance in enumerate(variances):
            diffs.append((FirstVariance - steep * i) - variance)
        return diffs

    def GetTFIDFs(self, dir):
        try:
            return self.tfidfs
        except AttributeError:
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

            self.tfidfs = CompletedList
            return CompletedList

    def InitCluster(self, k, dir):
        tfidfs = self.GetTFIDFs(dir)

        clustered = {}
        means = {}

        random.seed(1)
        for _ in range(k):
            key = random.choice(list(tfidfs.keys()))
            while key in clustered.keys():
                key = random.choice(list(tfidfs.keys()))
            clustered[key] = []

        for TfidfsKey, TfidfsValue in tfidfs.items():
            lowest = math.inf
            SoonAdd = ""
            for ClusterKey in clustered.keys():
                EucDis = self.EuclideanDistance(TfidfsValue, tfidfs[ClusterKey])
                if EucDis < lowest:
                    lowest = EucDis
                    SoonAdd = ClusterKey
            
            clustered[SoonAdd].append(TfidfsKey)

        # Find the mean of every cluster (x̄ = Σ item[i])
        for DefaultCluster, DefaultValue in clustered.items():
            NeedCal = []
            for lst in DefaultValue:
                NeedCal.append(tfidfs[lst])
        
            means[DefaultCluster] = self.mean(NeedCal)

        """Means Looks Like:
            {New-Text1: [1, 2, 3, 4]}
            {New-Text2: [1, 2, 3, 4]}
        """
        return means, clustered

    def kcluster(self, k, dir):
        tfidfs = self.GetTFIDFs(dir)
        means, save = self.InitCluster(k, dir) #安排初始聚类

        for _ in range(1, self.max_iter):
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

            # Check if nothing has changed
            # If True then exit
            if self.IfChanged(MeanedResult, save):
                return MeanedResult

            means = {}
            save = MeanedResult

            for key, value in MeanedResult.items():
                NeedCal = []
                for lst in value:
                    NeedCal.append(tfidfs[lst])

                means[key] = self.mean(NeedCal)
                NeedCal = []

        return MeanedResult
            

    def kmeans(self, k, dir, WithKeys=False):
        # Calculate the best kmeans clustering
        result = {}
        for _ in range(self.n_init):
            lowest = math.inf
            longest = self.kcluster(k, dir)

            if self.variation(longest) <= lowest:
                result = longest
        if WithKeys:
            return result
        else:
            return list(result.values())
    
            
    def calk(self, dir):
        variances = []
        for i in range(1, len(dir) + 1):
            variances.append(self.variation(self.kmeans(i, dir, True)))
        
    	# Find the difference in variation between different k values
        # This is to find the elbow point
        diffs = self.kneed(variances)

        # Added one because we started from 1 but the list's index starts with 0
        return diffs.index(max(diffs)) + 1
