nums1=[2,3,2]; nums2=[1,2]
s2=set(nums2); s1=set(nums1)
print([sum(x in s2 for x in nums1), sum(x in s1 for x in nums2)])
