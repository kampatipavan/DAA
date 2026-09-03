def select_k(a,k):
    if len(a)<=5:return sorted(a)[k-1]
    groups=[a[i:i+5] for i in range(0,len(a),5)]
    med=[sorted(g)[len(g)//2] for g in groups]
    pivot=select_k(med,(len(med)+1)//2)
    low=[x for x in a if x<pivot]; eq=[x for x in a if x==pivot]; high=[x for x in a if x>pivot]
    if k<=len(low):return select_k(low,k)
    if k<=len(low)+len(eq):return pivot
    return select_k(high,k-len(low)-len(eq))
for a,k in [([12,3,5,7,19],2),([12,3,5,7,4,19,26],3),([1,2,3,4,5,6,7,8,9,10],6)]: print(select_k(a,k))
