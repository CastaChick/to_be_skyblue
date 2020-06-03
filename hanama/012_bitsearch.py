n, m = map(int, input().split())

lst = {i:[] for i in range(n)}

for i in range(m):
    x, y = map(int, input().split())
    lst[y-1].append(x-1)

lst = {key: set(value) for key, value in lst.items()}
ans = 0
for i in range(2**n):
    group = []
    tmp = True
    for j in range(n):
        if i >> j & 1:
            group.append(j)

    l = len(group)

    for j in range(l-1):
        target = group.pop(-1)
        if not lst[target] >= set(group):
            tmp = False
            break

    if tmp:
        ans = max(ans, l)

print(ans)
