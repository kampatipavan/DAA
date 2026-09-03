def insertion_sort(a):
    a=a[:]
    for i in range(1,len(a)):
        key=a[i]; j=i-1
        while j>=0 and a[j]>key: a[j+1]=a[j]; j-=1
        a[j+1]=key
    return a
print(insertion_sort([3,1,4,1,5,9,2,6,5,3]))
print("Insertion Sort is stable for equal elements.")
