# DAA Lab Exercise
# Topic 6 - Backtracking - Question 16

from itertools import combinations

# Q15/Q16 subsets
def subsets(a):
    return [list(c) for r in range(len(a)+1) for c in combinations(a,r)]
print("T6 Q15:",subsets([1,2,3]))
print("T6 Q16:",[x for x in subsets([2,3,4,5]) if 3 in x])
