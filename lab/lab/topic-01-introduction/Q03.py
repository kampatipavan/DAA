nums=[1,2,1]
total=0
for i in range(len(nums)):
    seen=set()
    for j in range(i,len(nums)):
        seen.add(nums[j]); total += len(seen)**2
print(total)
