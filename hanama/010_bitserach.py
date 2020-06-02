n = int(input())

a = list(map(int, input().split()))

q = int(input())

m = dict(zip(range(q), list(map(int, input().split()))))

ans = ["no"] * q

for i in range(2**n):
    now = 0
    for j in range(n):
        if i >> j & 1:
            now += a[j]

    if now in m.values():
        key_lst = [key for key, value in m.items() if value==now]
        for key in key_lst:
            ans[key] = "yes"

for i in range(q):
    print(ans[i])
