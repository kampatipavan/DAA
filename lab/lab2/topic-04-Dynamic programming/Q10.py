# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 10

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q10 Text Justification
def justify(words,width):
    out=[];i=0
    while i<len(words):
        j=i; letters=0
        while j<len(words) and letters+len(words[j])+(j-i)<=width:
            letters+=len(words[j]);j+=1
        gaps=j-i
        if j==len(words) or gaps==1:
            line=" ".join(words[i:j]).ljust(width)
        else:
            spaces=width-letters; q,r=divmod(spaces,gaps-1)
            line=(" ".join([]))
            for k in range(i,j-1): line+=words[k]+" "*(q+(k-i<r))
            line+=words[j-1]
        out.append(line);i=j
    return out
print("T4 Q10:",justify(["This","is","an","example","of","text","justification."],16))
