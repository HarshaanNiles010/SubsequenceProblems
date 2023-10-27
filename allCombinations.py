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