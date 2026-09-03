def selection_sort(a):
    a=a[:]
    for i in range(len(a)):
        p=i
        for j in range(i+1,len(a)):
            if a[j]<a[p]: p=j
        a[i],a[p]=a[p],a[i]
    return a
for a in ([5,2,9,1,5,6],[10,8,6,4,2],[1,2,3,4,5]): print(selection_sort(a))
print("Time Complexity: O(n^2)")
