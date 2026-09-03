def quick(a):
    if len(a)<=1:return a
    p=a[len(a)//2]; left=[x for x in a if x<p]; mid=[x for x in a if x==p]; right=[x for x in a if x>p]
    return quick(left)+mid+quick(right)
print(quick([19,72,35,46,58,91,22,31]))
print(quick([31,23,35,27,11,21,15,28]))
