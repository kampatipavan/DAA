def find_peak(nums):
    lo,hi=0,len(nums)-1
    while lo<hi:
        mid=(lo+hi)//2
        if nums[mid]>nums[mid+1]: hi=mid
        else: lo=mid+1
    return lo
print(find_peak([1,2,3,1])); print(find_peak([1,2,1,3,5,6,4]))
print("Time Complexity: O(log n)")
