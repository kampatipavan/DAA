def missing_k(arr,k):
    x=1
    while True:
        if x not in arr: k-=1
        if k==0:return x
        x+=1
print(missing_k([2,3,4,7,11],5)); print(missing_k([1,2,3,4],2))
