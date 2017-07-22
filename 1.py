l = [x for x in range(1,1000)]
s = [x for x in l if x % 3 == 0 or x % 5 == 0]
print(sum(s))
