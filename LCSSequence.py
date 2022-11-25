from typing import List

class LCS:
    def __init__(self, nums1:List[int], nums2:List[int]):
        self.numsListA = nums1.copy()
        self.numsListB = nums2.copy()
        self.lengthListA = len(nums1)
        self.lengthListB = len(nums2)
        self.lcsLength = 0
        self.lcsList = []
    
    def LCSlength(self):
        L = [[None]*(self.lengthListB + 1) for i in range(self.lengthListA + 1)] 
        for i in range(self.lengthListA + 1 ):
            for j in range(self.lengthListB + 1 ):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif self.numsListA[i - 1] == self.numsListB[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        self.lcsLength = L[self.lengthListA][self.lengthListB]
        last = self.lcsLength
        i = self.lengthListA
        j = self.lengthListB
        while i > 0 and j > 0:
            if self.numsListA[i - 1] == self.numsListB[j - 1]:
                self.lcsList.append(self.numsListA[i - 1])
                i -= 1
                j -= 1
            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
            else:
                j -= 1
        self.lcsList = self.lcsList[::-1]
        return self.lcsLength

    def LCSprint(self):
        print(self.lcsList)


if __name__ == "__main__":
    nums1 = [2,3,4,5,6,7,8,9,10]
    nums2 = [1,2,4,6,8,9]
    lcsObject = LCS(nums1,nums2)
    print(lcsObject.LCSlength())
    lcsObject.LCSprint()
