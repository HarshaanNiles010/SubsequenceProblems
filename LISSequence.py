from typing import List
# This is the problem dealing with Longest Increasing Subsequence
class LIS:
    def __init__(self, nums:List[int]):
        self.numList = nums
        self.lisLength = 0
        self.lisList = []
    
    def LISlength(self) -> int:
        L = [[] for _ in range(len(self.numList))]
        L[0].append(self.numList[0])
        for i in range(1,len(self.numList)):
            for j in range(i):
                if self.numList[i] > self.numList[j] and (len(L[i]) < len(L[j]) + 1):
                    L[i] = L[j].copy()
            L[i].append(self.numList[i])
        maxx = L[0]
        for x in L:
            if len(x) > len(maxx):
                maxx = x
        self.lisLength = len(maxx)
        self.lisList = maxx
        return len(maxx)
        

    def printLIS(self) -> None:
        print(self.lisList)



if __name__ == "__main__":
    nums = [5,4,6,2,1,2,3]
    #lisObject = LIS(nums)
    #print(lisObject.LISlength())
    #lisObject.printLIS()