def bubble_sort(a):
    a=a[:]
    for end in range(len(a)-1,0,-1):
        swapped=False
        for j in range(end):
            if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]; swapped=True
        if not swapped: break
    return a
print(bubble_sort([5,1,4,2,8]))
