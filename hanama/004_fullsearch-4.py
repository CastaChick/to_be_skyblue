n, m = map(int, input().split())
ans = 0
a = []

for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    for j in range(i, m):
        p = 0
        for k in range(n):
            p += max(a[k][i], a[k][j])

        ans = max(ans, p)

print(ans)
