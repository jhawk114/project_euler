i,j = 999,999
ans = 0
while i > 99:
    j = 999
    while j > 99:
        k = i*j
        if str(k) == str(k)[::-1] and k > ans and k < n:
            ans = k
        j -= 1
    i -= 1

print(ans)
