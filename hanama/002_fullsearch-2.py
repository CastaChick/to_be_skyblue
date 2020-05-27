n = int(input())

ans = 0
for i in range(1, n+1, 2):
    c = 0
    for k in range(1, i+1):
        if i % k == 0:
            c += 1
    if c == 8:
        ans += 1
print(ans)
