import numpy as np

n = int(input())

a = []
b = []

for i in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y =y, x
    a.append(x)
    b.append(y)

items = sorted(a + b)

a = np.array(a)
b = np.array(b)
ans = float("inf")
for i in range(2*n-1):
    for j in range(i+1, 2*n):
        start = items[i]
        finish = items[j]

        time = np.sum(np.abs(a-start) + np.abs(a-b) + np.abs(b-finish))
        ans = min(ans, time)

print(ans)
