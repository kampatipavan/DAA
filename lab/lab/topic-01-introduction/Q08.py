def bubble_sort(a):
    a=a[:]
    for i in range(len(a)):
        swapped=False
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]; swapped=True
        if not swapped: break
    return a
print(bubble_sort([5,1,4,2,8]))
print("Time Complexity: O(n^2) worst case")
