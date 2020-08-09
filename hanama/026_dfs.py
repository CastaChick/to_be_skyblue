import sys
sys.setrecursionlimit(10**6)

n, q = map(int, input().split())

nodes = [0] * n
edges = {i: set() for i in range(n)}

for i in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].add(b-1)
    edges[b-1].add(a-1)


for i in range(q):
    p, x = map(int, input().split())
    nodes[p-1] += x

seen = set()

def dfs(index):
    seen.add(index)
    for i in edges[index] - seen:
        nodes[i] += nodes[index]
        dfs(i)

for i in range(n):
    if i in seen:
        pass
    dfs(i)

print(" ".join(map(str, nodes)))
