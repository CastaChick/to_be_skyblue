import numpy as np

n = int(input())

balloons = np.array([list(map(int, input().split())) for i in range(n)])

h = balloons[:, 0]
s = balloons[:, 1]

time_range = np.arange(n)

left = 0
right = np.max(h + s*(n-1))
while right - left > 1:
    mid = (left + right) // 2

    limits = (mid - h) // s
    limits.sort()

    if (limits >= time_range).all():
        right = mid

    else:
        left = mid

print(right)
