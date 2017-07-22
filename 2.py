def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b
s = [x for x in fib(4000000) if x % 2 == 0 and x > 0]
print(sum(s))
