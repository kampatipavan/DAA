def rob_linear(a):
    prev=cur=0
    for x in a: prev,cur=cur,max(cur,prev+x)
    return cur
def rob_circle(nums):
    if len(nums)==1:return nums[0]
    return max(rob_linear(nums[:-1]),rob_linear(nums[1:]))
print(rob_circle([2,3,2]))
print(rob_circle([1,2,3,1]))
