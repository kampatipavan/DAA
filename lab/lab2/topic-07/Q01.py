# DAA Lab Exercise
# Topic 7 - Tractability and Approximation - Question 1

from itertools import permutations

# Q1 Hamiltonian Path verification
def hamiltonian_path(V,E):
    adj={v:set() for v in V}
    for u,v in E:adj[u].add(v);adj[v].add(u)
    for p in permutations(V):
        if all(p[i+1] in adj[p[i]] for i in range(len(p)-1)):return True,p
    return False,None
print("T7 Q1:",hamiltonian_path(["A","B","C","D"],[("A","B"),("B","C"),("C","D"),("D","A")]))
