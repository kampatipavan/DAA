def subset_sum(a,target):
    n=len(a); half=n//2
    L=a[:half]; R=a[half:]
    left={0}
    for x in L:left|={s+x for s in list(left)}
    right={0}
    for x in R:right|={s+x for s in list(right)}
    return any(target-s in right for s in left)
print(subset_sum([1,3,9,2,7,12],15))
print(subset_sum([3,34,4,12,5,2],15))
