from math import sqrt,floor
n = 25

def fp(n):
    if n % 2 == 0:
        if n == 2:
            return 2
        return fp(n/2)
    sqn = floor(sqrt(n))+1
    for x in range(3,sqn,2):
        if n % x == 0:
            if n/x > x:
                return fp(int(n/x))
            return x
    return int(n)
print(fp(n))
