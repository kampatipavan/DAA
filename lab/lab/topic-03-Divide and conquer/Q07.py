def binary_search(a,key):
    lo,hi=0,len(a)-1; comparisons=0
    while lo<=hi:
        mid=(lo+hi)//2; comparisons+=1
        if a[mid]==key:return mid,comparisons
        if a[mid]<key:lo=mid+1
        else:hi=mid-1
    return -1,comparisons
a=[5,10,15,20,25,30,35,40,45]
print(binary_search(a,20))
print(binary_search([10,20,30,40,50,60],50))
