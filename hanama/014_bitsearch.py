n, k = map(int, input().split())

a = list(map(int, input().split()))

min_cost = float("inf")
for i in range(2**n):
    if bin(i).count("1") != k or not i & 1:
        continue

    min_h = a[0]
    cost = 0
    for j in range(1, n):
        if i >> j & 1:
            min_h += 1
            cost += max(0, min_h-a[j])

        min_h = max(min_h, a[j])

    min_cost = min(min_cost, cost)

print(min_cost)
