import itertools

n = int(input())

p = "".join(input().split())
q = "".join(input().split())

lst = []

for v in itertools.permutations(map(str, range(1, n+1)), n):
    lst.append("".join(v))

lst.sort()

d = {lst[i]: i for i in range(len(lst))}

print(abs(d[p] - d[q]))
