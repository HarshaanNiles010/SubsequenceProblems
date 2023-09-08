from typing import List, Dict
# from timeit import timeit

def freqDistro(nums: List[int]) -> Dict[int,int]:
    elements = list(set(nums))
    count = [0] * len(elements)
    distro = dict(zip(elements, count))
    for i in nums:
        distro[i] += 1
    return distro

# yeah this is the easier method, will test the time and put it out soon
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
    t_0 = timeit(stmt='freqDisto(nums)', setup='from __main__ import freqDistro, nums')
    t_1 = timeit(stmt='newFreqDistro(nums)', setup='from __main__ import newFreqDistro, nums')
    print(t_0)
    print(t_1)

# some ending thoughts:
    # I used timeit function to check for speed and the newer method is roughly 38% faster 
# forgot to mention I didn't run it on command line will do so in the future and publish the results here
