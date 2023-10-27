from typing import List
from timeit import timeit


def combination_recursive(l:List[int]) -> List[List[int]]:
    if l:
        result = combination_recursive(l[:-1])
        return result + [c + [l[-1]] for c in result]
    else:
        return [[]]

def combination_iterative(l:List[int]) -> List[List[int]]:
    result = [[]]
    for x in l:
        result = result + [c + [x] for c in result]
    return result

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    #print(combination_recursive(l))
    #print(combination_iterative(l))
    t_0 = timeit(stmt='combination_recursive(l)', setup='from __main__ import combination_recursive, l')
    
    t_1 = timeit(stmt='combination_iterative(l)', setup='from __main__ import combination_iterative, l')
    
    print(f"recursive combination function for a list of lenght: {len(l)} takes time: {t_0}secs")
    print(f"iterative combination function for a list of lenght: {len(l)} takes time: {t_1}secs")
#recursive combination function for a list of lenght: 5 takes time: 2.477901332997135secs
#iterative combination function for a list of lenght: 5 takes time: 1.8377112500020303secs
#recursive combination function for a list of lenght: 6 takes time: 4.265175250002358secs
#iterative combination function for a list of lenght: 6 takes time: 3.2475934169997345secs
#recursive combination function for a list of lenght: 7 takes time: 8.233815041996422secs
#iterative combination function for a list of lenght: 7 takes time: 6.44483533300081secs
#recursive combination function for a list of lenght: 8 takes time: 16.39083566699992secs
#iterative combination function for a list of lenght: 8 takes time: 13.24050583299686secs
#recursive combination function for a list of lenght: 9 takes time: 32.47266958299588secs
#iterative combination function for a list of lenght: 9 takes time: 26.67574112500006secs