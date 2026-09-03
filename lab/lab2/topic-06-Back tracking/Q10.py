# DAA Lab Exercise
# Topic 6 - Backtracking - Question 10

from itertools import permutations

# Q9/Q10 permutations
def perms(a):
    return list(permutations(a))
def unique_perms(a):
    return sorted(set(permutations(a)))
print("T6 Q9:",perms([1,2,3]))
print("T6 Q10:",unique_perms([1,1,2]))
