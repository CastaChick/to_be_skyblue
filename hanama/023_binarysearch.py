import numpy as np
import bisect

n, m = map(int, input().split())

p = [int(input()) for i in range(n)]

p.append(0)

scores = set()

for i in p:
    for j in p:
        scores.add(i+j)

scores = list(scores)
scores.sort()

ans = 0

for target in scores:
    x = bisect.bisect_left(scores, m-target)

    if x:
        ans = min(max(ans, scores[x-1]+target), m)

print(ans)
