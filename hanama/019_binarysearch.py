d = int(input())
n = int(input())
m = int(input())

shop = [0, d]
for i in range(n-1):
    shop.append(int(input()))

shop.sort()

k = []
for i in range(m):
    k.append(int(input()))


ans = 0

for x in k:
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2

        if shop[mid] == x:
            break

        elif shop[mid] > x:
            right = mid

        elif shop[mid] < x:
            left = mid

        if right - left == 1:
            ans += min(x-shop[left], shop[right]-x)
            break
print(ans)
