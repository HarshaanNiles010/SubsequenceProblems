from typing import List
from LCSSequence import LCS
# LPS is nothing but LCS by using the same two strings again
class LPS(LCS):
    def __init__(self,nums:List[int]):
        self.numsList = nums
        self.lpsLength = 0
        self.lpsList = []
    
    def LPSlength(self):
        templcsObject = LCS(nums,nums[::-1])
        return templcsObject.LCSlength()

    def LPSPrint(self):
        templcsObject = LCS(nums,nums[::-1])
        templcsObject.LCSprint()

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,5,4,3]
    lpsObject = LPS(nums)
    print(lpsObject.LPSlength())
    lpsObject.LPSPrint()