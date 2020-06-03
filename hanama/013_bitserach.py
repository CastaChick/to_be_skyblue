import numpy as np

r, c = map(int, input().split())

ami = []

for i in range(r):
    ami.append(list(map(int, input().split())))

ami = np.array(ami, dtype=bool)

ans = 0

for i in range(2**r):
    ami_ = np.copy(ami)
    for j in range(r):
        if i >> j & 1:
            ami_[j] = ~ami_[j]
    tmp = 0
    row = np.zeros((2, c), dtype=int)

    row[0] = np.sum(ami_, axis=0)
    row[1] = r - row[0]
    ans = max(ans, np.sum(np.max(row, axis=0)))
    
print(ans)
