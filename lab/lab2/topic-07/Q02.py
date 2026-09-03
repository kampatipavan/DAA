# DAA Lab Exercise
# Topic 7 - Tractability and Approximation - Question 2


# Q2 3-SAT
def sat(clauses,vars):
    for bits in range(1<<len(vars)):
        a={v:bool(bits>>i&1) for i,v in enumerate(vars)}
        if all(any((not a[v] if neg else a[v]) for v,neg in c) for c in clauses):return True,a
    return False,None
C=[[("x1",0),("x2",0),("x3",1)],[("x1",1),("x2",0),("x4",0)],[("x3",0),("x4",1),("x5",0)]]
print("T7 Q2:",sat(C,["x1","x2","x3","x4","x5"]))
