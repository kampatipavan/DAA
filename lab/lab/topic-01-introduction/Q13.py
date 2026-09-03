def climb(n):
    a,b=1,1
    for _ in range(n): a,b=b,a+b
    return a
print(climb(4)); print(climb(3))
