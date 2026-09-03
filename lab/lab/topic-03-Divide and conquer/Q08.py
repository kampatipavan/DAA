def binary_search_steps(a,key):
    lo,hi=0,len(a)-1
    while lo<=hi:
        mid=(lo+hi)//2; print(f"low={lo}, high={hi}, mid={mid}, value={a[mid]}")
        if a[mid]==key:return mid
        if a[mid]<key:lo=mid+1
        else:hi=mid-1
    return -1
print("Index:",binary_search_steps([3,9,14,19,25,31,42,47,53],31))
print("Binary Search requires sorted data for correctness.")
