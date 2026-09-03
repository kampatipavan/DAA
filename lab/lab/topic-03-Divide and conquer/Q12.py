def median_of_medians(arr,k):
    return select_k(arr,k)
def select_k(a,k):
    if len(a)<=5:return sorted(a)[k-1]
    med=[sorted(a[i:i+5])[(len(a[i:i+5])-1)//2] for i in range(0,len(a),5)]
    p=select_k(med,(len(med)+1)//2); lo=[x for x in a if x<p]; eq=[x for x in a if x==p]; hi=[x for x in a if x>p]
    return select_k(lo,k) if k<=len(lo) else p if k<=len(lo)+len(eq) else select_k(hi,k-len(lo)-len(eq))
print(median_of_medians([1,2,3,4,5,6,7,8,9,10],6))
print(median_of_medians([23,17,31,44,55,21,20,18,19,27],5))
