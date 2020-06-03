import itertools

k = int(input())

area = [["."]*8 for i in range(8)]

X = set(range(8))
Y = set(range(8))
A = set()
B = set()

for i in range(k):
    x, y = map(int, input().split())
    area[x][y] = "Q"

    X.remove(x)
    Y.remove(y)
    A.add(x-y)
    B.add(x+y)
for v in itertools.permutations(Y):
    ok = 1
    A_ = A.copy()
    B_ = B.copy()
    for x, y in zip(X, v):
        if x-y in A_ or x+y in B_:
            ok = 0
            break

        A_.add(x-y)
        B_.add(x+y)
    
    if ok:
        for x, y in zip(X, v):
            area[x][y] = "Q"
        break

for i in range(8):
    print("".join(area[i]))
