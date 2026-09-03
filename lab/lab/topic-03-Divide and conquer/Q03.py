def merge_sort(a):
    if len(a)<=1:return a
    m=len(a)//2; L=merge_sort(a[:m]); R=merge_sort(a[m:]); out=[]; i=j=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:out.append(L[i]);i+=1
        else:out.append(R[j]);j+=1
    return out+L[i:]+R[j:]
print(merge_sort([31,23,35,27,11,21,15,28]))
print(merge_sort([22,34,25,36,43,67,52,13,65,17]))
