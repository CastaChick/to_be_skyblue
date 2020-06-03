n = int(input())
s = list(map(int, input().split()))

q = int(input())
t = list(map(int, input().split()))

c = 0

for target in t:
    left = 0
    right = n-1

    while left <= right:
        mid = (left + right) // 2

        if s[mid] > target:
            right = mid - 1

        elif s[mid] < target:
            left = mid + 1

        else:
            c += 1
            break

print(c)
