import sys
import math


p = float(input())

def func(t, p=p):
    return t + p * pow(2, -t/1.5)

# 三分探索

left = 0
right = p+1

while abs(func(left) - func(right)) > 1e-10:
    c1 = (2*left+right)/3
    c2 = (left+2*right)/3

    if func(c1) <= func(c2):
        right = c2
    else:
        left = c1

print(func(left))

# 微分して二分探索
def dfunc(t, p=p):
    return 1+math.pow(2, -t/1.5) * p * math.log(2) / -1.5

left = 0
right = p+1

if dfunc(left) > 0:
    print(func(left))
    sys.exit(0)

while abs(dfunc(left)) > 1e-8:
    mid = (left + right) / 2

    if dfunc(mid) > 0:
        right = mid

    else:
        left = mid

print(func(left))
