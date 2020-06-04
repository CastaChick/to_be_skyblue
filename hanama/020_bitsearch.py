import bisect
import numpy as np

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

small = []
big = []

for x in b:
    small.append(bisect.bisect_left(a, x))
    big.append(n-bisect.bisect(c, x))

small = np.array(small)
big = np.array(big)

print(np.sum(small*big))
