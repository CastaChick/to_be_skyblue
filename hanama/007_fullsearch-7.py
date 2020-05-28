n = int(input())

poles = []
for i in range(n):
    x, y = map(int, input().split())
    poles.append((x, y))

pole_set = set(poles)

ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        pole1 = poles[i]
        pole2 = poles[j]

        dx = pole2[0] - pole1[0]
        dy = pole2[1] - pole1[1]

        if (pole1[0] + dy, pole1[1] - dx) in pole_set:
            if (pole2[0] + dy, pole2[1] - dx) in pole_set:
                ans = max(ans, dx**2+dy**2)

print(ans)
