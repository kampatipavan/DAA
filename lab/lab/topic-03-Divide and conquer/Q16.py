def karatsuba(x,y):
    if x<10 or y<10:return x*y
    n=max(len(str(x)),len(str(y))); m=n//2; p=10**m
    a,b=divmod(x,p); c,d=divmod(y,p)
    z0=karatsuba(b,d); z1=karatsuba(a+b,c+d); z2=karatsuba(a,c)
    return z2*p*p+(z1-z2-z0)*p+z0
print(karatsuba(1234,5678))
