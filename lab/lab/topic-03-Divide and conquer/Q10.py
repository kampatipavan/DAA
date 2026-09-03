from collections import Counter
def four_sum_count(A,B,C,D):
    sums=Counter(a+b for a in A for b in B)
    return sum(sums[-c-d] for c in C for d in D)
print(four_sum_count([1,2],[-2,-1],[-1,2],[0,2]))
print(four_sum_count([0],[0],[0],[0]))
