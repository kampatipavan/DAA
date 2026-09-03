def binary_search(arr,key):
    lo,hi=0,len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==key: return mid
        if arr[mid]<key: lo=mid+1
        else: hi=mid-1
    return -1
arr=[-9,3,4,6,8,9,10,30]
key=10
pos=binary_search(arr,key)
print(f"Element {key} is found at position {pos}")
print("Time Complexity: O(log n)")
