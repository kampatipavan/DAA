def quick(a):
    if len(a)<=1:return a
    p=a[0]; left=[x for x in a[1:] if x<=p]; right=[x for x in a[1:] if x>p]
    return quick(left)+[p]+quick(right)
print(quick([10,16,8,12,15,6,3,9,5]))
print(quick([12,4,78,23,45,67,89,1]))
