n, m = map(int, input().split())

s = [0] * m

for i in range(m):
    k, *li = map(int, input().split())
    for j in range(k):
        s[i] += 2**(li[j]-1)

p = list(map(int, input().split()))


ans = 0

for i in range(2**n):
    tmp = True
    for j in range(m):
        if bin(i & s[j]).count("1") % 2 != p[j]:
            tmp = False
            break

    if tmp:
        ans += 1

print(ans)
