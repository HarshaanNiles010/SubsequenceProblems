from typing import List, Dict


def freqDistro(nums: List[int]) -> Dict[int,int]:
    elements = list(set(nums))
    count = [0] * len(elements)
    distro = dict(zip(elements, count))
    for i in nums:
        distro[i] += 1
    return distro
def newFreqDistro(nums: List[int]) -> Dict[int,int]:
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

if __name__ == '__main__':
    nums = [(i + 1) for i in range(10)]
    print(freqDistro(nums))
