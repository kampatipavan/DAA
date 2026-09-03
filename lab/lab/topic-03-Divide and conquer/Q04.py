def merge_sort(a):
    if len(a)<=1:return a,0
    m=len(a)//2; L,c1=merge_sort(a[:m]); R,c2=merge_sort(a[m:]); out=[]; i=j=0; c=c1+c2
    while i<len(L) and j<len(R):
        c+=1
        if L[i]<=R[j]:out.append(L[i]);i+=1
        else:out.append(R[j]);j+=1
    return out+L[i:]+R[j:],c
for a in ([12,4,78,23,45,67,89,1],[38,27,43,3,9,82,10]): print(merge_sort(a))
