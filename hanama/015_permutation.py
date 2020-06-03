import numpy as np
import itertools
import math

n = int(input())

towns = []

for i in range(n):
    towns.append(list(map(int, input().split())))

towns = np.array(towns)

l = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        l[i, j] = np.sum((towns[i] - towns[j])**2) ** 0.5

ans = 0
for order in itertools.permutations(range(n), n):
    now = order[0]
    f = 0
    for i in order[1:]:
        f += l[now, i]
        now = i
    ans += f
print(ans/math.factorial(n))
